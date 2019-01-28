from django.db import models
from datetime import datetime
from realtors.models import Realtor
""" เอา models มาจากอีก app นึง """

class Listing(models.Model):
  """ admin area จะแสดงแค่ field เดียว """
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  """ ForeignKey ไปหาตาราง Realtor """
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True) # ปล่อยว่างได้
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2,decimal_places=1)  # กำหนดตัวเลข 2 หลัก ทศนิยม 1 ตำแหน่ง
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main =  models.ImageField(upload_to='photos/%Y/%m/%d/') # ใน database เก็บ string แต่ใน django มี datatype เก็บ photo อยู่ จะเก็บในโฟลเดอร์ media/media/date (admin area) แล้วอัพขึ้น server 
  photo_1 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  photo_2 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  photo_3 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  photo_4 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  photo_5 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  photo_6 =  models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True) 
  is_published = models.BooleanField(default=True)  # ปกติจะแสดง
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    """ แสดงใน admin """
    return self.title
  