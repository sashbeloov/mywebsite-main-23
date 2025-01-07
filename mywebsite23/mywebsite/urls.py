"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from sys import prefix

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from home import views as h_views
from course import views as c_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', h_views.selectlanguage, name="selectlanguage"),
    path('i18/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('home/',h_views.index, name='home'),
    path('',h_views.index, name='home'),
    path('course/',c_views.index, name='course'),
    path('about/',h_views.about, name='about'),
    path('contact/',h_views.contact, name='contact'),
    path('tutors/', h_views.tutors, name='tutors'),
    path('students/', h_views.tutors, name='students'),
    path('subjects/', h_views.subjects, name='subjects'),
    path('subject/<int:id>/<slug:slug>',h_views.subjectdatail, name='subjectdatail')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




