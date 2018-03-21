from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.models import FuncTickFormatter
import json
from pprint import pprint
import os

def get_traffic_for_day(data):
    list = []
    for record in data:
        list.append(record)
    return list

def get_traffic_for_hour(data, hour):
    list = []
    for record in data:
        list.append(record['data'][hour])
    return list

google_data = json.load(open('googletraffic.json'))
output_file("bars.html")

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = ['11 am', '12 pm', '1 pm', '2 pm', '3 pm', '4 pm', '5 pm', '6 pm', '7 pm', '8 pm', '9 pm']
populartimes = google_data[0]['populartimes']


"""
monday_data = get_traffic_for_day(populartimes[0]['data'])
tuesday_data = get_traffic_for_day(populartimes[1]['data'])
wednesday_data = get_traffic_for_day(populartimes[2]['data'])
thursday_data = get_traffic_for_day(populartimes[3]['data'])
friday_data = get_traffic_for_day(populartimes[4]['data'])
saturday_data = get_traffic_for_day(populartimes[5]['data'])
sunday_data = get_traffic_for_day(populartimes[6]['data'])

"""

eleven_am = get_traffic_for_hour(populartimes, 12)
twelve_pm = get_traffic_for_hour(populartimes, 13)
one_pm = get_traffic_for_hour(populartimes, 14)
two_pm = get_traffic_for_hour(populartimes, 15)
three_pm = get_traffic_for_hour(populartimes, 16)
four_pm = get_traffic_for_hour(populartimes, 17)
five_pm = get_traffic_for_hour(populartimes, 18)
six_pm = get_traffic_for_hour(populartimes, 19)
seven_pm = get_traffic_for_hour(populartimes, 20)
eight_pm = get_traffic_for_hour(populartimes, 21)
nine_pm = get_traffic_for_hour(populartimes, 22)

pprint(eleven_am)


data = {'weekdays' : weekdays,
        '11 am'   : eleven_am,
        '12 pm'   : twelve_pm,
        '1 pm'   : one_pm,
        '2 pm'   : two_pm,
        '3 pm'   : three_pm,
        '4 pm'   : four_pm,
        '5 pm'   : five_pm,
        '6 pm'   : six_pm,
        '7 pm'   : seven_pm,
        '8 pm'   : eight_pm,
        '9 pm'   : nine_pm}


# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (weekday, hour) for weekday in weekdays for hour in hours ]
counts = sum(zip(data['11 am'], data['12 pm'], data['1 pm'], data['2 pm'], data['3 pm'], data['4 pm'], data['5 pm'], data['6 pm'], data['7 pm'], data['8 pm'], data['9 pm']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=300, plot_width=1000, title="Traffic by hour",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)

p.y_range.start = 0
p.x_range.range_padding = 0
p.xaxis.major_label_orientation = 1.5
p.xgrid.grid_line_color = None
p.yaxis.visible = False

show(p)