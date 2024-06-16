import requests
import json

def get_data():
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWA-5F8604E0-D10A-4921-AE89-18C150B0E908",
        "locationName": "新竹市",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]['time'][0]["startTime"]
        end_time = weather_elements[0]['time'][0]["endTime"]
        weather_state = weather_elements[0]['time'][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]['time'][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]['time'][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]['time'][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]['time'][0]["parameter"]["parameterName"]
        return tuple([location, start_time, end_time, weather_state, 
                      rain_prob, min_tem, comfort, max_tem])
    else:
        return tuple()

def line_notify(data):
    token = "UPlTL9fbYiRYLFyoPMDXTeuR54GePXuLDEPpFqMtj8G"
    message = ""

    if len(data) == 0:
        message += "\n[Error] 無法取得天氣資訊"
    else:
        message += f"\n{data[0]}今天天氣: {data[3]}\n"
        message += f"預測區間: {data[1]} ~ {data[2]}\n"
        message += f"溫度: {data[5]}°C - {data[7]}°C\n"
        message += f"降雨機率: {data[4]}%\n"
        message += f"舒適度: {data[6]}\n"

        if int(data[4]) > 70:
            message += "今天可能會下雨，記得帶傘出門!\n"
        if int(data[7]) > 30:
            message += "今天天氣炎熱，外出小心中暑\n"
        if int(data[5]) < 10:
            message += "今天天氣寒冷，外出小心保暖\n"

    # Line notify 所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message,
        "stickerPackageId": 6632,
        "stickerId": 11825376,
    }

    requests.post(url=line_url, headers=line_header, data=line_data)

if __name__== '__main__':
    data = get_data()
    line_notify(data)