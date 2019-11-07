from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from uma.views import TwoSecondsView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', TwoSecondsView.as_view())
]
