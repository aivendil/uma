from django.conf.urls import url

from uma.views import TwoSecondsView

urlpatterns = [
    url(r'', TwoSecondsView.as_view())
]
