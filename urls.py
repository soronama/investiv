"""investiv URL Configuration
Including another URLconf
"""
from django.conf.urls import url, include
from django.contrib import admin
from investivgroup import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^investivgroup/', include('investivgroup.urls')),
]

