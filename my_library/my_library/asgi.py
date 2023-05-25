"""
ASGI config for my_library project.                                                     # การกำหนดค่า ASGI สำหรับโปรเจค my_library

It exposes the ASGI callable as a module-level variable named ``application``.          # มันเปิดเผย ASGI ที่เรียกใช้เป็นตัวแปรระดับโมดูลชื่อ `application`.        

For more information on this file, see                                                  # สำหรับข้อมูลเพิ่มเติมเกี่ยวกับไฟล์นี้ ดูที่
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/    
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_library.settings')

application = get_asgi_application()
