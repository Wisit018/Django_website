"""
WSGI config for my_library project.                                                         # การกำหนดค่า WSGI สำหรับโปรเจค my_library

It exposes the WSGI callable as a module-level variable named ``application``.              # มันเปิดเผย WSGI ที่เรียกใช้เป็นตัวแปรระดับโมดูลชื่อ `application`.                

For more information on this file, see                                                      # สำหรับข้อมูลเพิ่มเติมเกี่ยวกับไฟล์นี้ ดูที่        
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_library.settings')

application = get_wsgi_application()
