from django.shortcuts import render
import datetime

# Create your views here.



def index1(request):
    current_year: str = str(datetime.datetime.now()).split(' ')[0].split('-')[0]
    
    context: dict[str] = {
        'current_year': current_year
    }
    return render(request, "index.html", context)