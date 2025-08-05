# from m5stack import *
# from m5ui import *
# from uiflow import *
# import urequests
# import gc
# import ujson
# from machine import Timer

# lcd.clear()


# lcd.clear()
# response=urequests.get(url)
# data=ujson.loads(response.text)
# curr_tempr=str(int(data["main"]["feels_like"]-273.15))

# forecast_data=urequests.get(accu_api)


# forecast=ujson.loads(forecast_data.text)

# min= str(int((forecast["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]-32)/1.8))
# max= str(int((forecast["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]-32)/1.8))






# label0 = M5TextBox(114, 84, curr_tempr, lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
# label0.setText("29")
# label0.setText("54")

# label1 = M5TextBox(24, 195, min+"°C", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)
# label2 = M5TextBox(245, 203, max+"°C", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)












import requests
import json

response=requests.get(accu_api)

data=response.json()

min= int((data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]-32)/1.8)
max= int((data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]-32)/1.8)

print(min, max)
response.close()

