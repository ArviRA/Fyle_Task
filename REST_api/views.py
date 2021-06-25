from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def autoComplete(request):

    if request.method == 'GET':
        response = request.GET.dict()
        print("resu:::",response['q'])
        return JsonResponse({'status':'200'})
    else:
        return JsonResponse({"Status Code":'405'})

def empty(request):
    return JsonResponse({'empty':'404'})