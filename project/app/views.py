from django.shortcuts import render
from django.http import HttpResponse
from app.models import video



def index(request):
    data=video.objects.all()

    context={
        'data':data
    }
    return render(request, "index.html", context)
    # return HttpResponse("hi..the first program")


def contact(request):
    return render(request, "contact.html")


#def about(request):
    #return render(request, "About.html")

def qualification(request):
    return render(request, "qualification.html")

def login(request):
    return render(request, "login.html")



# def contact(request):
# def contact(request):

# return render(request, "contact.html")


# Create your views here.
def views():
    return None
