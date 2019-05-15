from os import environ
from django.http import JsonResponse


def main_page(request):
    json_object = {'status': 'PRODUCTION' if int(environ.get('DEBUG')) == 0 else 'DEVELOPMENT' }
    return JsonResponse(json_object)
