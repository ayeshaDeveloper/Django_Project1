from django.shortcuts import render
from app1.models import Person
from openai import OpenAI

client = OpenAI(api_key="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")


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

def aboutme_fun(request):
    return render(request, "aboutme.html")

def contactus_fun(request):
    return render(request, "contactus.html")

def user_input(request):
    result = None
    print("hi")

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