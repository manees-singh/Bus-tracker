from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import gc
import ujson
from machine import Timer
import time 


lcd.clear()


label0 = M5TextBox(114, 84, "0", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
label1 = M5TextBox(24, 195,"0", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)
label2 = M5TextBox(245, 203, "0", lcd.FONT_UNICODE, 0xFFFFFF, rotate=0)

def currTemp(t):
  try:
    
    response=urequests.get(url)
    data=ujson.loads(response.text)
    curr_tempr=str(int(data["main"]["feels_like"]-273.15))
    
    label0.setText(curr_tempr)
    
    
    response.close()
    gc.collect()
    
  except:
    label0.setText("Error!")
    
tim=Timer(1)
tim.init(period=1800000,mode=tim.PERIODIC, callback=currTemp)




def forecastTemp(p):
  try:
    forecast_data=urequests.get(accu_api)
    forecast=ujson.loads(forecast_data.text)

    min= str(int((forecast["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]-32)/1.8))
    max= str(int((forecast["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]-32)/1.8))
    
    label1.setText( min+"°C")
    label2.setText(max+"°C")

    
  except:
    print("error")
    
    
time1=Timer(2)
time1.init(period=86400000, mode=time1.PERIODIC, callback=forecastTemp)































import requests
import json

response=requests.get(accu_api)

data=response.json()

min= int((data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]-32)/1.8)
max= int((data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]-32)/1.8)

print(min, max)
response.close()

