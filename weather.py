# import required modules
import requests, json
import translateFile
 
# Enter your API key here
api_key = "###modify"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
def getWeather(city_name) -> str:
    # complete_url variable to store
    # complete url address
    city_name=translateFile.translateToEnglish(city_name)

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = translateFile.translateToRomanian(z[0]["description"])
        weather_description = translateFile.translateToRomanian(weather_description)
        weather_description = weather_description.split('w', 1)[0]
        # print following values
        return(" Temperatura in Celsius = " +
                        str(int(current_temperature-273.15))  +
            "\n Umiditate = " +
                        str(current_humidity) + "%" +
            "\n Descriere = " +
                        str(weather_description))
    
    else:
        return(" Orasul nu a fost gasit ")
