from django.shortcuts import get_object_or_404,render
from .models import Listing

from django.core.paginator import Paginator,EmptyPage
""" ทำลิงค์ไปแสดงข้อมูลเป็นหน้าๆ """

from .choices import price_choices, bedroom_choices, state_choices


def index(request):
  """ ดึงข้อมูลจาก database """
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  """ จะขึ้น error เพราะ vs code ไม่รู้จัก special function ของ django """
  """ filter คือจะให้แสดงเมื่อติ๊กที่ช่อง is_published ในหน้า admin """

  paginator = Paginator(listings, 6) # ส่งข้อมูลผ่าน listings
  page = request.GET.get('page')

  """ จะดึงข้อมูลจาก database """
  paged_listings = paginator.get_page(page)
  """ แสดงหน้าเว็บให้ template ดึง page_listings ไปใช้ """ 

  context = {
    'listings' : paged_listings,  
  }
  # listings ส่งผ่าน paged_listings
  return render(request,'listings/listings.html',context)

def listing(request,listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  """ ** new ให้แสดงข้อมูลของ listing กรณีหา id ไม่เจอจะขึ้นหน้าเหลือง """ 

  context ={
    'listing' : listing,
  }

  return render(request,'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    """ keywords มาจาก templates จะเป็น and ทั้งหมด เพราะงั้นยังไงก็หาได้ """
    keywords = request.GET['keywords']
    if keywords:
      """ check หาก feild ไม่ว่าง """
      queryset_list = queryset_list.filter(description__contains=keywords)
      """ field__lookuptype=value หาบางส่วนของคำ ไม่ใช่ทั้งประโยค และไม่เป็น Case sensitive"""
  
  # City
  if 'city' in request.GET:
    city = request.GET['city']
    """ fields ของ name ใน templates """
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)
      """ iexcat ต้องหาจากทั้งประโยคถึงจะเจอ แต่ไม่ใช่ case sensitive"""

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)
      """ iexcat ต้องหาจากทั้งประโยคถึงจะเจอ แต่ไม่ใช่ case sensitive"""

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
      """ lte คือหาไม่เกินที่ต้องการ ใส่ 4 ห้องน้ำ 2,3 มาหมด"""

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)
      """ lte คือหาไม่เกินที่ต้องการ ใส่ 4 ห้องน้ำ 2,3 มาหมด"""
  
      
  context = {
    'state_choices' : state_choices,
    'bedroom_choices' : bedroom_choices,
    'price_choices' : price_choices,
    'listings' : queryset_list,
    'values' : request.GET,
  }

  return render(request,'listings/search.html',context)