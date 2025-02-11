import passiogo

system_id= 4834

system= passiogo.getSystemFromID(system_id)


routes= system.getRoutes()


buses= system.getVehicles()

# for i in range(42):
#     print(routes[i].__dict__['shortName'],i)

#print(routes[22].__dict__)


for bus in buses:
    if bus.routeName== "Central Station / 31st & Iowa via KU":
        print("Longitude:"+ bus.longitude)


# target_route= routes[22]
# for bus in buses:
#     if bus.==target_route.id:
#         print (bus.name, bus.longitude)

# for i in range(31):
#     print(buses[i].__dict__)
#print(routes[22].__dict__)

# route id upto 42
# number of buses upto 31


### Longitude of concern
#for bus 11, route id is 22, 28, 
#for bus 12, route id is 32, 37


###Routes####

# stops = target_route.getStops()
# for stop in stops:
#     print(f"Stop Name: {stop.name}, Latitude: {stop.latitude}, Longitude: {stop.longitude}")
