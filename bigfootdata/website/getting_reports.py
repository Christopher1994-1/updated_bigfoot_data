import pandas as pd
import math


# bigfoot_locations = pd.read_csv('bfro_locations.csv')
# bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
# bigfoot_reports = pd.read_csv('bfro_reports.csv')


# function that gets the 3 most recent sightings from whatever state that is selected
def getting_recent_reports(state):
    months = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December",
    }
    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    
    state = str(state).title()
    
    # try:
    specific_date = pd.to_datetime('2022-01-01')

    df = bigfoot_geo_reports
    df_state = df.loc[(bigfoot_geo_reports['state'] == state)]

    json_rows = []
    for a, row in df_state.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row['date'])
    number_of_sightings = len(json_rows) # return this
    
    dates = pd.to_datetime(json_rows)
        
    # find the nearest date before and after the specific date
    nearest_before = dates[dates <= specific_date].to_list()
    times = sorted(nearest_before)
    times2 = times[::-1][:3]
        
    date1 = str(times2[0]).split(' ')[0]
    
    
    # first recent sighting
    where_date1 = df.loc[(bigfoot_geo_reports['date'] == date1)]
    
    date_info = []
    for a, row in where_date1.iterrows():
        json_row = row.to_dict()
        date_info.append(json_row)
    
    first_report_title = str(date_info[0]['title']).split(':')[1].strip() # return this
    first_report_YEAR = date1.split('-')[0]
    first_report_MONTH = months[date1.split('-')[1]]
    first_report_county = date_info[0]['county']
    
    first_report_return_a_tag = f"{first_report_MONTH} {first_report_YEAR}, {first_report_county}" # return this
    first_report_class = date_info[0]['classification'] # return this
    first_number = date_info[0]['number'] # return this


    
    # # second recent sighting
    date2 = str(times2[1]).split(' ')[0]
    
    where_date2 = df.loc[(bigfoot_geo_reports['date'] == date2)]
    
    date_info2 = []
    for a, row in where_date2.iterrows():
        json_row = row.to_dict()
        date_info2.append(json_row)
    
    second_report_title = str(date_info2[0]['title']).split(':')[1].strip() # return this
    second_report_YEAR = date2.split('-')[0]
    second_report_MONTH = months[date2.split('-')[1]]
    county = date_info2[0]['county']
    
    second_report_return_a_tag = f"{second_report_MONTH} {second_report_YEAR}, {county}" # return this
    second_report_class = date_info2[0]['classification'] # return this
    second_number = date_info2[0]['number'] # return this
    
    
    # # second recent sighting
    date3 = str(times2[2]).split(' ')[0]
    
    where_date3 = df.loc[(bigfoot_geo_reports['date'] == date3)]
    
    date_info3 = []
    for a, row in where_date3.iterrows():
        json_row = row.to_dict()
        date_info3.append(json_row)
    
    third_report_title = str(date_info3[0]['title']).split(':')[1].strip() # return this
    third_report_YEAR = date3.split('-')[0]
    third_report_MONTH = months[date3.split('-')[1]]
    county = date_info3[0]['county']
    
    third_report_return_a_tag = f"{third_report_MONTH} {third_report_YEAR}, {county}" # return this
    third_report_class = date_info3[0]['classification'] # return this
    third_number = date_info3[0]['number'] # return this


    return {
    "report_one": {"title1": first_report_title, "first_atag": first_report_return_a_tag, "first_class": first_report_class, "number": first_number},
    "report_two": {"title2": second_report_title, "second_atag": second_report_return_a_tag, "second_class": second_report_class, "number": second_number},
    "report_three": {"title3": third_report_title, "third_atag": third_report_return_a_tag, "third_class": third_report_class, "number": third_number},
    "total_sightings": number_of_sightings,
    }


# function to get all of the counties
def getting_counties(state):

    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    
    state = str(state).title()

    df = bigfoot_geo_reports
    df_state = df.loc[(bigfoot_geo_reports['state'] == state) & (bigfoot_geo_reports['date'].isna() == False)]

    json_rows = []
    for a, row in df_state.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)

    county_values = df_state['county'].value_counts()
    counties = county_values.to_dict()

    return counties
    


def showing_reports(state, county):
    months = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December",
    }

    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    
    state = str(state).title()

    df = bigfoot_geo_reports
    df_state = df.loc[(bigfoot_geo_reports['state'] == state) & (bigfoot_geo_reports['county'] == county)]

    json_rows = []
    for a, row in df_state.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
        
    new_list = []
    value = ''
    for d1 in json_rows:
        new_dict = {}
        for key in ('date', 'title', 'classification', 'number'):
            value = d1[key]

            new_dict[key] = value
        new_list.append(new_dict)

    # Remove dictionaries with NaN values
    cleaned_list = [d for d in new_list if not any(isinstance(v, float) and math.isnan(v) for v in d.values())]

    # Sort by date
    sorted_cleaned_list = sorted(cleaned_list, key=lambda x: str(x['date']), reverse=True)
    
    
    
    title_list = []
    for dic in sorted_cleaned_list:
        title_dict = {}
        for key in ('date', 'title', 'classification', 'number'):
            title = str(dic[key])
            if ":" in title:
                new_title = str(title).split(":")
                main_title = new_title[1].strip()
                title_dict[key] = main_title
            else:
                title_dict[key] = title
        title_list.append(title_dict)
        
    
    
    date_list = []
    for tim in title_list:
        last_dict = {}
        for key in ('date', 'title', 'classification', 'number'):
            date = str(tim[key])
            if '-' in date and len(date) == 10:
                date_split = str(date).split('-')
                YEAR = date_split[0]
                MONTH = months[date_split[1]]
                new_date = f"{MONTH} {YEAR}"
                last_dict[key] = new_date
            else:
                last_dict[key] = date
        date_list.append(last_dict)
        
    return date_list
    
    
    
# function that gets the data for one case
def one_case(state, county, id_number):

    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    
    state = str(state).title()
    id_number = float(id_number)

    df = bigfoot_geo_reports
    df_state = df.loc[(bigfoot_geo_reports['state'] == state) & (bigfoot_geo_reports['county'] == county) & (bigfoot_geo_reports['number'] == id_number)]

    json_rows = []
    for a, row in df_state.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
        

        
    return json_rows



# Function that gets the four states with the most sightings for index
def the_four_states():
    
    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    df = bigfoot_geo_reports

    rates = df['state'].value_counts().to_dict()    
    
    return rates



# Function that is only used for when user clicks on most recent reports links
def recent_reports(state, number):
    months = {
        "01":"January",
        "02":"February",
        "03":"March",
        "04":"April",
        "05":"May",
        "06":"June",
        "07":"July",
        "08":"August",
        "09":"September",
        "10":"October",
        "11":"November",
        "12":"December",
    }
    bigfoot_geo_reports = pd.read_csv('bfro_reports_geocoded.csv')
    
    state = str(state).title()
    number = float(number)
    
    # try:
    specific_date = pd.to_datetime('2022-01-01')

    df = bigfoot_geo_reports
    df_state = df.loc[(bigfoot_geo_reports['state'] == state) & (bigfoot_geo_reports['number'] == number)]

    json_rows = []
    for a, row in df_state.iterrows():
        json_row = row.to_dict()
        json_rows.append(json_row)
    number_of_sightings = len(json_rows) # return this
    
    

        
    return json_rows[0]['county']


