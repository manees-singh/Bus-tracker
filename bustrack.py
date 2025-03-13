import time
import os
from dotenv import load_dotenv
import passiogo
from twilio.rest import Client

# Set up for twilio call. 
load_dotenv()
auth_token = os.getenv("AUTH_TOKEN")
account_sid = os.getenv("ACCOUNT_SID")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
to_phone_number = os.getenv("TO_PHONE_NUMBER")

client= Client(account_sid, auth_token)


#system id for Lawrence Transit
system_id= 4834

system= passiogo.getSystemFromID(system_id)
routes= system.getRoutes()
target_route= routes[37] 
 # route for Bus 12, route 37 somehow works



#explored using stops but didn't work as stop information not provided for the bus.
# stops = target_route.getStops()
# target_stop=stops[5] 
# target_stop_id= target_stop.id### 'name'= 323 - Clinton @ Hawthorn





#twilio=TwilioCall(account_sid, auth_token, twilio_phone_number)
buses=system.getVehicles()



#calculated course of the bus can be used to find the direction of the bus travel. 
for bus in buses:
    if bus.routeName== "Central Station / 27th & Wakarusa": #sometimes drivers forget to change from bus 11 to 12 so use both 
        print(f"{bus.name}, Longitude:{bus.longitude}, {vars(bus)}")
        if   38.942000000 < float(bus.longitude) < 38.942722950 and  0 < float(bus.calculatedCourse) < 90: # the range of longitude where the function should get activated
            print('hello there.')
            call=client.calls.create(
                to=to_phone_number,
                from_=twilio_phone_number,
                twiml="<Response><Say>Hello! Your bus is arriving soon.</Say></Response>"
            )


#This is all the information that can be gained by tracking the bus
'''
{'id': 16410, 'name': '364', 'type': None, 'system': <passiogo.TransportationSystem object at 0x7f8041c9edd0>, 'calculatedCourse': '1.7087058734558127', 'routeId': '53924', 'routeName': 'Central Station / 27th & Wakarusa', 'color': '#f7b7d3', 'created': '08:42 PM', 'longitude': '38.956884500', 'speed': None, 'paxLoad': None, 'outOfService': 0, 'more': '101', 'tripId': '750423'}
'''









#print(routes[22].__dict__)

# use this longitude: Longitude:38.942722900 for the location to get the notice from
# use bus name to check on the passiogo app, its easier
# use bus routeName== "Central Station / 31st & Iowa via KU" which is the bus to be tracked






