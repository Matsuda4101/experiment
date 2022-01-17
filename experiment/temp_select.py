# -*- coding: utf-8 -*-
import weather
import cloth_image

def cloth_choice(plan,place,cl,sl):
    # 天気情報を取得
    t, w = weather.weather_get(place)
    a,b,c = cloth_image.select(plan,cl,t,sl)
        
    return a,b,c