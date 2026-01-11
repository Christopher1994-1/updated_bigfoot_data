from django.shortcuts import render
import datetime
from . import getting_reports

# Create your views here.

current_year: str = str(datetime.datetime.now()).split(' ')[0].split('-')[0]


basic_context: dict[str] = {
    "current_year": current_year
}


state_slogans: dict[str] = {
    'alabama': 'Sweet Home Alabama',
    'alaska': 'North to the Future',
    'arizona': 'The Grand Canyon State',
    'arkansas': 'The Natural State',
    'california': 'The Golden State',
    'colorado': 'The Centennial State',
    'connecticut': 'The Constitution State',
    'delaware': 'The First State',
    'florida': 'The Sunshine State',
    'georgia': 'The Peach State',
    'hawaii': 'The Aloha State',
    'idaho': 'The Gem State',
    'illinois': 'Land of Lincoln',
    'indiana': 'The Hoosier State',
    'iowa': 'The Hawkeye State',
    'kansas': 'The Sunflower State',
    'kentucky': 'The Bluegrass State',
    'louisiana': 'The Pelican State',
    'maine': 'The Pine Tree State',
    'maryland': 'The Old Line State',
    'massachusetts': 'The Bay State',
    'michigan': 'The Great Lakes State',
    'minnesota': 'The North Star State',
    'mississippi': 'The Magnolia State',
    'missouri': 'The Show Me State',
    'montana': 'Big Sky Country',
    'nebraska': 'The Cornhusker State',
    'nevada': 'The Silver State',
    'new hampshire': 'Live Free or Die',
    'new jersey': 'The Garden State',
    'new mexico': 'The Land of Enchantment',
    'new york': 'The Empire State',
    'north carolina': 'The Tar Heel State',
    'north dakota': 'The Peace Garden State',
    'ohio': 'The Buckeye State',
    'oklahoma': 'The Sooner State',
    'oregon': 'The Beaver State',
    'pennsylvania': 'The Keystone State',
    'rhode island': 'The Ocean State',
    'south carolina': 'The Palmetto State',
    'south dakota': 'The Mount Rushmore State',
    'tennessee': 'The Volunteer State',
    'texas': 'The Lone Star State',
    'utah': 'The Beehive State',
    'vermont': 'The Green Mountain State',
    'virginia': 'The Old Dominion State',
    'washington': 'The Evergreen State',
    'west virginia': 'The Mountain State',
    'wisconsin': "America's Dairyland",
    'wyoming': 'The Equality State'
}


state_shorthands: dict[str] = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'new york': 'NY',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode island': 'RI',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virginia': 'VA',
    'washington': 'WA',
    'west virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}





def index1(request):
    
    context: dict[str] = {}
    context.update(basic_context)
    return render(request, "index.html", context)







def case(request, case_number):
    
    number_one_case = getting_reports.one_case('', '', case_number)[0]
    state = number_one_case['state']
    county = number_one_case['county']
    stateL = state_slogans[state.lower()]
    image = f'{state.lower()}.png'
    
    secondry_case = str(case_number).split('.')[0]
    
    context: dict[str] = {
        'case_number': case_number,
        'secondry_case': secondry_case,
        'report': number_one_case,
        'state_name': state,
        'county': county,
        'state_slogan': stateL,
        'image': image
        
    }
    context.update(basic_context)
    
    return render(request, "pages/case.html", context)




def county_cases(request, state, county):
    counties = getting_reports.showing_reports(state, county)
    
    state_shorthand2: str = state_shorthands[str(state).lower()]
    
    number_of_counties: str = str(len(counties))
    
    context = {
        'state_shorthand': state_shorthand2,
        'choosen_county': county,
        'all_counties': counties,
        'state_name': state,
        'number_of_counties': number_of_counties
        
    }
    context.update(basic_context)
    return render(request, 'pages/county_cases.html', context)



def state_selection(request, state_name):
    
    state_name2: str = ''
    if ' ' in state_name:
        state_name2 = str(state_name).replace(' ', '-')
    else:
        state_name2 = state_name
    
    return_recent_reports_dict = getting_reports.getting_recent_reports(state_name)
    counties = getting_reports.getting_counties(state_name)
    
    total_sightings = return_recent_reports_dict['total_sightings']
    
    updated_recent_report = return_recent_reports_dict.pop('total_sightings', None)
    
    stateSlogan = state_slogans[state_name]
    
    counties = getting_reports.getting_counties(state_name)
    
    
    
    context: dict[str] = {
        'state_name': state_name.title(),
        'total_counties': counties,
        "total_sightings": total_sightings,
        "recent_reports": return_recent_reports_dict,
        "county": counties,
        "image_state_name": state_name2,
        'state_slogan': stateSlogan,
    }
    context.update(basic_context)
    
    return render(request, "pages/state_selection.html", context)