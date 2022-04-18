from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):

    context ={
        "variable":"Anand Sahu"
    }
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

def contact(request):

 
    return render(request,'contact.html')
    # return HttpResponse("this is homepage")