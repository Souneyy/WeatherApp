import requests


# functie om het weer terug te krijgen 
def getWeather(city, APIKey):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}&units=metric'
    
    res = requests.get(url)


    # failsafe voor als er iets zou fout gaan(200 -> succesvolle get req)
    if res.status_code == 200:
        try:
            data = res.json()   # Json parsen en data in dictionary steken
        except ValueError:
            print('Response data is geen geldige JSON formaat.')

        # relevante data extraheren
        weatherDescription = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        
        print(f"Het weer in {city}:")
        print(f"Temperatuur: {temperature}°C")
        print(f"Vochtigheid: {humidity}%")
        print(f"Beschrijving: {weatherDescription}")
    else:
        print('Stad werd niet terug gevonden of de API Key is verkeerd.')


def main():
    APIKey = ''
    city = input('Van welke stad wil je het weer zien?')
    getWeather(city, APIKey)

# voor als je het zou importen in een andere project
if __name__ == "__main__":
    main()