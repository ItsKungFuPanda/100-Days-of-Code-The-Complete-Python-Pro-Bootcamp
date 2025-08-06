import requests
from prettytable import PrettyTable

# Function to get weather data
def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        table = PrettyTable(["City", "Temperature (°C)", "Weather", "Humidity (%)"])
        table.add_row([data["name"], data["main"]["temp"], data["weather"][0]["description"], data["main"]["humidity"]])
        print(table)
    else:
        print("City not found or API error!")

# Main program
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
