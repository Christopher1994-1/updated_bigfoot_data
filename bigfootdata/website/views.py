from django.shortcuts import render
import datetime
from . import getting_reports

# Create your views here.




def index1(request):
    current_year: str = str(datetime.datetime.now()).split(' ')[0].split('-')[0]
    
    context: dict[str] = {
        'current_year': current_year
    }
    return render(request, "index.html", context)







def state_selection(request, state_name):
    
    return_recent_reports_dict = getting_reports.getting_recent_reports(state_name)
    counties = getting_reports.getting_counties(state_name)
    
    
    print(return_recent_reports_dict)
    
    
    total_sightings = return_recent_reports_dict['total_sightings']
    
    context: dict[str] = {
        'state_name': state_name.title(),
        'total_counties': counties,
        "total_sightings": total_sightings,
        
    }
    
    return render(request, "pages/state_selection.html", context)