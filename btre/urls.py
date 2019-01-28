from django.contrib import admin
from django.urls import path,include
# เพิ่มมาหลังจากสร้าง folder media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # My pages app
    path('',include('pages.urls')),
    # listings app
    path('listings/',include('listings.urls')),
    # accounts app
    path('accounts/',include('accounts.urls')),
    # contacts app
    path('contacts/',include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
