from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'Generators/Home.html')

def welcome(request):
    return render(request,'Generators/welcome.html')
# def password(request):
    # return render(request,'Generators/Password.html',{'password':'sdhfbgsjgf43w34sf'})
 # def Ram(request):
 #    return HttpResponse(" u should stay hear")
 #
 # def syam(request):
 #    return HttpResponse("I am ur brother")
def password(request):

     characters=list('abcdefghijklmnopqrstuvwxyz')
     if request.GET.get('Upercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('SpecialSymbol'):
        characters.extend(list('!@#$%&^*<>?-+'))
     if request.GET.get('numbers'):
        characters.extend(list('123456789'))

     length = int(request.GET.get('length',12))
     the_new_password=''
     for x in range(length):
         the_new_password += random.choice(characters)
     return render(request,'Generators/Password.html',{'Password':the_new_password})
