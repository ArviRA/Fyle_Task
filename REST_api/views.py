from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import psycopg2

from .module import *
cur = {'status':False}
# Create your views here.
@csrf_exempt
def autoComplete(request):

    if request.method == 'GET':
        global cur
        if request.method == "GET":
            global cur
            if cur['status'] != 200:
                cur = getConnection()
                if cur['status'] == 200:
                    pass
                else:
                    return JsonResponse(cur)
        response = request.GET.dict()
        query = response['q'].upper()
        limit = response['limit']
        offset = response['offset']
        code = "select * from bank where branch like '%{}%' order by ifsc limit {} offset {}".format(query,limit,offset)
        final_res = getRecord(cur['data'],code)
        return JsonResponse({'Status Code':'200','result':final_res})
    else:
        return JsonResponse({"Status Code":'405','Message':"Wrong Method"})
def search(request):
    if request.method == "GET":
        global cur
        if cur['status'] != 200:
            cur = getConnection()
            if cur['status'] == 200:
                pass
            else:
                return JsonResponse(cur)
        response = request.GET.dict()
        query = response['q'].upper()
        limit = response['limit']
        offset = response['offset']
        code = "select * from bank where ifsc like '%{0}%' or bank_id like '%{0}%' or branch like '%{0}%' or address like '%{0}%' or city like '%{0}%' or district like '%{0}%' or state like '%{0}%' or bank_name like '%{0}%'  order by ifsc limit {1} offset {2} ".format(query,limit,offset)
        print(code)
        final_res = getRecord(cur['data'],code)
        codeCount = "select count(*) from bank where ifsc like '%{0}%' or bank_id like '%{0}%' or branch like '%{0}%' or address like '%{0}%' or city like '%{0}%' or district like '%{0}%' or state like '%{0}%' or bank_name like '%{0}%'".format(query)
        finalCount = getCount(cur['data'],codeCount)[0]
        print(finalCount)
        return JsonResponse({'Status Code':'200','result':final_res,'totalCount':finalCount})
    else:
        return JsonResponse({"Status Code":'405','Message':"Wrong Method"})

def empty(request):
    return JsonResponse({'Status Code':'404','Message':"Page Not Found"})

def Fav(request):
    print("got in views")
    if request.method == "GET":
        global cur
        if cur['status'] != 200:
            cur = getConnection()
            if cur['status'] == 200:
                pass
            else:
                print(cur)
                return JsonResponse(cur)
    response = request.GET.dict()
    query = response['q']
    r = setFav(query,cur['data'])
    print("cur",cur)
    return JsonResponse({'status':200,'result':r})
