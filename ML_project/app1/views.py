from django.shortcuts import render
from app1.models import Person
from openai import OpenAI
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

client = OpenAI(api_key="your_key_here)")


def gpt_process(string_value):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant, explain the answer in easy words"},
        {"role": "user", "content": string_value}
    ]
    )

    return str(completion.choices[0].message.content)

# Create your views here.
@login_required
def welcome(request):
    result=None
    if request.method == 'POST':
        mynum = int(request.POST.get('number', 0))
        result=mynum*100
        print(mynum)
        myname = (request.POST.get('name',''))
        print(myname)
        myemail = (request.POST.get('email',''))
        print(myemail)
        mypassword = (request.POST.get('password',''))
        print(mypassword)

        myinstances = person(userinputvalues=mynum, myvalue= result)
        myinstances.save()      

    return render(request,"base.html", {'result': result})
@login_required
def aboutme_fun(request):
    return render(request, "aboutme.html")
@login_required
def contactus_fun(request):
    return render(request, "contactus.html")
@login_required
def user_input(request):
    

    if request.method == 'POST':

        
        user_input_text=str(request.POST['text'])
        try:
            gpt_output=gpt_process(user_input_text)
            result = gpt_output
            
            myinstance = Person(userinputvalue = user_input_text , mycalvalue = gpt_output)
            myinstance.save()
        except:
            pass

    return render(request,'chatBot.html' , {'result' : result })

#SIGNUP & LOGIN FUNCTIONS
@login_required
def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('base')
    else:
        form=UserCreationForm
    return render(request,'signup.html',{'form':form})

@login_required
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('base')
    else:
        form=UserCreationForm
    return render(request,'login.html',{'form':form})


def logout_fun(request):
        logout(request)
        return redirect('login') 
