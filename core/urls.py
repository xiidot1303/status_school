
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
)

from app.views.application import *

urlpatterns = [
    path('xiidot1303/', admin.site.urls),

    # auth
    path('accounts/login/', LoginView.as_view()),

    # application
    path('', application_registr, name='application_registr'),
    path('application/registr', application_registr, name='application_registr'),
    path('application/list', application_list, name='application_list'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
