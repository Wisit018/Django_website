"""
URL configuration for my_library project.                                                       # การกำหนดค่า URL สำหรับโปรเจค my_library
                                                                                                # แปลภาษาไทย
The `urlpatterns` list routes URLs to views. For more information please see:                   # รายการ `urlpatterns` นำเสนอ URL ไปยังมุมมอง สำหรับข้อมูลเพิ่มเติมโปรดดู:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/                                     # https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:                                                                                       # ตัวอย่าง:
Function views                                                                                  # ฟังก์ชันมุมมอง
    1. Add an import:  from my_app import views                                                 # 1. เพิ่มการนำเข้า: จาก my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')                             # 2. เพิ่ม URL ไปยัง urlpatterns: path('', views.home, name='home')
Class-based views                                                                               # มุมมองที่ใช้คลาส
    1. Add an import:  from other_app.views import Home                                         # 1. เพิ่มการนำเข้า: จาก other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')                         # 2. เพิ่ม URL ไปยัง urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf                                                                       # รวม URLconf อื่น ๆ
    1. Import the include() function: from django.urls import include, path                     # 1. นำเข้าฟังก์ชัน include (): from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))                           # 2. เพิ่ม URL ไปยัง urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
]


