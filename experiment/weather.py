import requests
import json
import cv2

#OpenWeatherで取得したAPI
API_KEY = "666708fef8117515796190856e53dc51"
#OpenWeatherのURL
url = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={q}&APPID={key}"

def weather_get(place):
    #天気を取得したい都市名
    city = place

    #送信用URLの作成？
    url1 = url.format(q = city, key = API_KEY)
    #データの要求
    response = requests.get(url1)

    #受信データをjson形式に変換
    data = response.json()
    #データを見やすいように変換
    jsontext = json.dumps(data,indent=4)
    #画面に表示
    #print(jsontext)

    #受信データから一部のみを抽出して表示
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]
    if weather == "Clear":
        weather = "sun"
    elif weather == "Clouds" or weather == "Thunderstorm":
        weather = "cloud"
    elif weather == "rain" or weather == "Drizzle":
        weather = "rain"
    elif weather == "snow":
        weather = "snow"
    else:
        weather = "moya"

    weather = cv2.imread("weather/"+weather+".png")

    return temp, weather
    
#if __name__ == '__main__':
    #temp, weather = weather_get("Hokkaido")
    #print("気温："+str(int(temp))+"℃")
    #print("天気："+weather)