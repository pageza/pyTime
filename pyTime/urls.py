"""pyTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.timeClock.models import User as U, Job, Location, Clock_in, Clock_out, Company_notices

class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)
class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(Job, JobAdmin)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']
admin.site.register(Location, LocationAdmin)
class Clock_inAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clock_in, Clock_inAdmin)
class Clock_outAdmin(admin.ModelAdmin):
    pass
admin.site.register(Clock_out, Clock_outAdmin)
class Company_noticesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Company_notices, Company_noticesAdmin)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.timeClock.urls'))
]
