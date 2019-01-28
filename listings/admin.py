from django.contrib import admin
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
  """ ให้หน้า admin แสดงตารางเต็มๆ """
  list_display = ('id','title','is_published','price','list_date','realtor')
  list_display_links = ('id','title')
  """ ให้ id, title เป็นลิงค์ คลิกเข้าไปดูได้ """
  list_filter = ('realtor',)
  """ ระวัง! ถ้าเป็น tuple สมาชิกตัวเดียว ให้ใส่ comma ต่อท้าย ไม่งั้นจะ error """
  list_editable = ('is_published',)
  """ ให้แก้ไขข้อมูลได้เลย ไม่ต้องคลิกเข้าไปที่ record เพื่อแก้ """ 
  search_fields = ('title','description','address','city','state','zipcode','price')
  """ สร้างกล่องค้นหาใน admin """
  list_per_page = 25

admin.site.register(Listing,ListingAdmin)
""" อย่าลืม register มันด้วย """

