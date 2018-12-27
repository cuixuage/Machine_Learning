# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from MessageFilter.controller import loadModel

# 表单  访问./目录时调用此方法
def search_form(request):
    return render_to_response('index.html')    #render_to_response是DJango的重定向

# 接收请求数据        @csrf_exempt 取消Django CSRF的加密检查从而使用post
@csrf_exempt
def search_query(request):
    request.encoding='utf-8'
    testdata=[]
    if request.POST:
        message =  request.POST['json_message'].encode('utf-8')     #json数据的key json_message
        print message
        testdata.append(message)
        result = loadModel.nbClassifier_getresult(testdata)
    else:
        result = '你提交了空表单'

    # return HttpResponse(message)            #结果返回到当前界面 ./
    return JsonResponse({'message':result})


# 提交数据时更常用POST方法。我们下面使用该方法，并用一个URL和处理函数，同时显示视图和处理请求