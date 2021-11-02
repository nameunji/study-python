from django.contrib   import admin
from django.urls      import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls),
]
