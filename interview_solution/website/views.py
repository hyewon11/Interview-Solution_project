from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User, Teacher, SchoolInfo
import json
import logging

@csrf_exempt
def studentSignup(request):
    if request.method == "POST":
        userID = request.POST['userID']
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        passwordChk = request.POST.get('passwordChk', '')
        phone = request.POST.get('phone', '')
        school = request.POST.get('school','')
        grade = request.POST.get('grade', '')
        sClass = request.POST.get('sClass', '')

        if password != passwordChk:
            return render(request, 'signup.html',{'message':'입력한 비밀번호가 일치하지 않습니다.'})
        else:
            User.objects.create_user(userID=userID, username=username, password = password, phone = phone,school= school, grade= grade, sClass= sClass)
            return redirect(reverse('website:studentSignin'))
    else:
        return render(request, 'signup.html',{'message':'회원가입 실패'})

def teacherSignup(request):
    if request.method == "POST":
        userID = request.POST['userID']
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        passwordChk = request.POST.get('passwordChk', '')
        phone = request.POST.get('phone', '')
        school = request.POST.get('school','')
        grade = request.POST.get('grade', '')
        sClass = request.POST.get('sClass', '')

        if password != passwordChk:
            return render(request, 'signup.html',{'message':'입력한 비밀번호가 일치하지 않습니다.'})

        else:
            Teacher.objects.create_teacher(userID=userID, username=username, password = password, phone = phone,school= school, grade= grade, sClass= sClass)
            return redirect(reverse('website:teacherSignin'))
    else:
        return render(request, 'signup.html',{'message':'회원가입 실패'})

def studentcheckID(request):
    try:
        user= User.objects.get(userID=request.GET['userID'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        'data':"not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def teachercheckID(request):
    try:
        user= Teacher.objects.get(userID=request.GET['userID'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        'data':"not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def ajax_schoolInfo_autocomplete(request):
    if 'term' in request.GET:
        search_name = request.GET.get('term','')
        tags = SchoolInfo.objects.filter(name__icontains=search_name)
        print(tags)
        results = []
        for tag in tags:
            tag_json = {}
            tag_json['id'] = tag.id
            tag_json['label'] = tag.name
            tag_json['value'] = tag.name 
            results.append(tag_json)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
    return HttpResponse()

@csrf_exempt
def studentSignin(request):
    if request.method == "POST":
        userID = request.POST.get('userID', '')
        password = request.POST.get('password', '')

        try:
            user = User.objects.get(userID=userID)
            if check_password(password, user.password):
                request.session['user'] = user.userID
                return render(request, 'signin.html', {'error' : '성공'})
            else:
                return render(request,'signin.html',{'error':'username or password is incorrect'})
        except:
            return render(request, 'signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'signin.html')

def teacherSignin(request):
    if request.method == "POST":
        userID = request.POST.get('userID', '')
        password = request.POST.get('password', '')

        try:
            user = Teacher.objects.get(userID=userID)
            if check_password(password, user.password):
                request.session['user'] = user.userID
                return render(request, 'signin.html', {'error' : '성공'})
            else:
                return render(request,'signin.html',{'error':'username or password is incorrect'})
        except:
            return render(request, 'signin.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'signin.html')
