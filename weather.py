from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import gc
import ujson
from machine import Timer
import time 



lcd.clear()

setScreenColor(0XFFFFFF)
emojis={ "default":"res/default.jpg", "extreme": "res/red_hot.jpg", "sunny": "res/sun.jpg",  "best": "res/best.jpg",
"rainy": "res/umbrella.jpg", "snowy": "res/snow.jpg"}

lcd.image(112, 40, "res/best.jpg", scale=0, type=lcd.JPG) #image is of 100x 91 pixels


label0 = M5TextBox(114, 156, "10", lcd.FONT_DejaVu72, 0x222222, rotate=0)
label1 = M5TextBox(24, 84,"10°C", lcd.FONT_UNICODE, 0x222222, rotate=0)
label2 = M5TextBox(245, 84, "10°C", lcd.FONT_UNICODE, 0x222222, rotate=0)

def currTemp(t):
  try:
    
    response=urequests.get(url)
    data=ujson.loads(response.text)
    curr_tempr=str(int(data["main"]["feels_like"]-273.15))
    
    label0.setText(curr_tempr)
    ##image for the current temperature

    
    
    
    response.close()
    gc.collect()
    
  except:
    label0.setText("Error!")
    





def forecastTemp(p):
  try:
    forecast_data=urequests.get(accu_api)
    forecast=ujson.loads(forecast_data.text)

    temp_min= str(int((forecast["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]-32)/1.8))
    temp_max= str(int((forecast["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]-32)/1.8))
    
    label1.setText( temp_min+"°C")
    label2.setText(temp_max+"°C")
    

    precipitation= forecast["DailyForecasts"][0]["Day"]["HasPrecipitation"]


    if temp_max > 30:
        alert= extreme
    elif precipitation:
        if forecast["DailyForecasts"][0]["Day"]["PrecipitationType"].lower() == "rain":
            alert= "rainy"
        elif forecast["DailyForecasts"][0]["Day"]["PrecipitationType"].lower() == "snow":
            alert= "snowy"

    elif 22<temp_max<30:
        alert= "sunny"

    elif 15<temp_max<=22:
        alert= "best"
        
    else:
        alert= "default"

    lcd.image(112, 60, emojis[alert], scale=0, type=lcd.JPG) 
    forecast_data.close()
    gc.collect()
        
  except:
      print("error")


currTemp(None)
forecastTemp(None)



tim=Timer(1)
tim.init(period=1800000,mode=tim.PERIODIC, callback=currTemp)



time1=Timer(2)
time1.init(period=86400000, mode=time1.PERIODIC, callback=forecastTemp)




























