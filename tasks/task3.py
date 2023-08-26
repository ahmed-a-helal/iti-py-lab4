import requests
from tasks.checks import *
class weatherapi():
    def __init__(self,apikey:int):
        if not checkhex(apikey):
            raise ValueError("The apikey must be non-empty hexdecimal string")
        self.__apikey=apikey
        self.url="https://api.weatherapi.com/v1/{method}?key={key}&q={city}{Parameters}"
        
    def get_current_temperature(self,city:str):
        method="current.json"
        checkstring(string=city,name="city")
        url = self.url.format(method=method,key=self.__apikey,city=city,Parameters="")
        apiresponse = requests.get(url).json()
        checkapi(apiresponse)
        return apiresponse['current']['temp_c']
    
    def get_temperature_after(self,city:str,days:int,hour=None):
        method="forecast.json"
        if not checkint(days):
            raise ValueError(f"days must be integer or numerical string")
        elif not (int(days)>= 1 and  int(days)<= 14):
            raise ValueError(f"days must be between 1 and 14")
        else:
            days_Parameter = f"&days={days}"

        if not hour:
            hour_Parameter=""
        elif  not checkint(hour):
            raise ValueError(f"hour must be integer or numerical string")
        elif int(hour) > 24:
            raise ValueError(f"hour must be less than 24")
        else:
            hour_Parameter=f"&hour={hour}"
        checkstring(string=city,name="city")
        url = self.url.format(method=method,key=self.__apikey,city=city,Parameters=days_Parameter+hour_Parameter)
        apiresponse = requests.get(url).json()
        checkapi(apiresponse)
        out=[]
        for item in apiresponse['forecast']["forecastday"]:
            forecastday=dict()
            forecastday["date"]=item["date"]
            forecastday["day"]=dict()
            forecastday["hour"]=[]
            forecastday["day"]["maxtemp_c"]=item["day"]["maxtemp_c"]
            forecastday["day"]["mintemp_c"]=item["day"]["mintemp_c"]
            forecastday["day"]["avgtemp_f"]=item["day"]["avgtemp_f"]
            for hour_item in item['hour']:
                forecasthour=dict()
                forecasthour["time"]=hour_item["time"]
                forecasthour["temp_c"]=hour_item["temp_c"]
                forecastday["hour"].append(forecasthour)
            out.append(forecastday)
        return out
    
    def get_lat_and_long(self,city):
        method="current.json"
        checkstring(string=city,name="city")
        url = self.url.format(method=method,key=self.__apikey,city=city,Parameters="")
        apiresponse = requests.get(url).json()
        checkapi(apiresponse)
        return {"lat":apiresponse['location']['lat'],"lon":apiresponse['location']['lon']}

if __name__ == "__main__":
    api=weatherapi(apikey="") #please Insert Your Key
    #print(api.get_current_temperature("alexandria"))
    #print(api.get_temperature_after("alexandria","12"))
    print(api.get_lat_and_long("alexandria"))