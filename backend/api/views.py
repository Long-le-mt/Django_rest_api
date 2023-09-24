import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data

    print(body)
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data, dict(request.GET), dict(request.POST) )

    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)