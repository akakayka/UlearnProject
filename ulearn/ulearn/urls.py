"""
URL configuration for ulearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Akaka.views import Home, Popular, Areas, Skills, LastVacancies


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('popular/', Popular.as_view(), name='popular'),
    path('area/', Areas.as_view(), name='areas'),
    path('skills/', Skills.as_view(), name='skills'),
    path('last-vacancies/', LastVacancies.as_view(), name='last-vacancies')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
