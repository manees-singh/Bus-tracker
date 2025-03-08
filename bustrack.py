import time
import os
from dotenv import load_dotenv
import passiogo
from message import TwilioCall


load_dotenv()
auth_token = os.getenv("AUTH_TOKEN")
account_sid = os.getenv("ACCOUNT_SID")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
to_phone_number = os.getenv("TO_PHONE_NUMBER")


#system id for Lawrence Transit
system_id= 4834

system= passiogo.getSystemFromID(system_id)
routes= system.getRoutes()
target_route= routes[37] 
print(target_route.__dict__['name']) # route for Bus 12, route 37 somehow works


stops = target_route.getStops()
target_stop=stops[5] 
target_stop_id= target_stop.id### 'name'= 323 - Clinton @ Hawthorn

print(vars(target_route))



#twilio=TwilioCall(account_sid, auth_token, twilio_phone_number)
buses=system.getVehicles()
# for bus in buses:
#     print (vars(bus))


for bus in buses:
    if bus.routeName== "Central Station / 27th & Wakarusa":
        print(f"{bus.name}, Longitude:{bus.longitude}, {vars(bus)}")


#This is all the information that can be gained by tracking the bus
'''
{'id': 16410, 'name': '364', 'type': None, 'system': <passiogo.TransportationSystem object at 0x7f8041c9edd0>, 'calculatedCourse': '1.7087058734558127', 'routeId': '53924', 'routeName': 'Central Station / 27th & Wakarusa', 'color': '#f7b7d3', 'created': '08:42 PM', 'longitude': '38.956884500', 'speed': None, 'paxLoad': None, 'outOfService': 0, 'more': '101', 'tripId': '750423'}
'''


# def track_bus():
#     while True:
#         buses= system.getVehicles()
#         for bus in buses:
#             if bus.stopID ==target_stop_id:
#                 print("bus is here")
#                 twilio.make_call(to_phone_number)


#track_bus()   

# for stop in stops:
#     print(f"Stop Name: {stop.name}, Latitude: {stop.latitude}, Longitude: {stop.longitude}")



# for i in range(42):
#     print(routes[i].__dict__['name'], routes[i].__dict__['shortName'],i )

#print(routes[22].__dict__)

# use this longitude: Longitude:38.942722900 for the location to get the notice from
# use bus name to check on the passiogo app, its easier
# use bus routeName== "Central Station / 31st & Iowa via KU" which is the bus to be tracked










# for i in range(31):
#     print(buses[i].__dict__)
#print(routes[22].__dict__)

# route id upto 42
# number of buses upto 31 


### Longitude of concern
#for bus 11, route id is 22, 28, 
#for bus 12, route id is 32, 37


###Routes####


