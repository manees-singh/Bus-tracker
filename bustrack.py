import passiogo

system_id= 4834

system= passiogo.getSystemFromID(system_id)


routes= system.getRoutes()
print(routes)

