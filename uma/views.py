from datetime import datetime
from time import sleep

from django.http import JsonResponse, HttpRequest
from django.views import View


class TwoSecondsView(View):

    def get(self, request: HttpRequest):
        sleep(9)
        return JsonResponse({'data': request.GET, 'test': '%r' % datetime.now()})
