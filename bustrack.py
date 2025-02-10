import passiogo

system_id= 4834

system= passiogo.getSystemFromID(system_id)


routes= system.getRoutes()



for i in range(42):
    print(routes[i].__dict__['shortName'],i)


# print(routes[11].__dict__)

# route id upto 42
 
#for bus 11, route id is 22, 28, 
#for bus 12, route id is 32, 37

