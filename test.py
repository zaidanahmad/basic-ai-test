import datetime
import requests


import pyttsx3

# --- Initialize the Speaker ---
engine = pyttsx3.init()

def speak(text):
    """Makes the assistant speak the given text."""
    print(f"Assistant: {text}") # We still print for debugging
    engine.say(text)
    engine.runAndWait()



# --- CONFIGURATION ---
API_KEY = "53d3d32e3cac74ff0b91abe3fbdc4292" 

# --- weather api functions
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"]
            weather_desc = data["weather"][0]["description"]
            print(f"The weather in {city.title()} is:")
            print(f"  Temperature: {temperature}°C")
            print(f"  Description: {weather_desc}")
        else:
            print("City not found. Please check the spelling.")
    except requests.exceptions.RequestException:
        print("Could not connect to the weather service.")


#--- other Function Definition
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"The current time is {current_time}.")
def tell_joke():
  speak("I am Batman hahaha haha")

def say_hello():
  speak("Hello there!")

def mention_creator():
  speak("Zark")

print("AI Assistant is online. Type 'exit' to quit.")
while True:
  command=input("What is your command? : ").lower()
  if command == "exit":
        print("Bye")
        break
  elif command == "hello":
        say_hello()
  elif command == "time":
         tell_time()
  elif command == "joke":
         tell_joke()
  elif command == "creator":
        mention_creator()
  elif "weather in" in command:
        # This extracts the city name from the command
        city = command.replace("weather in", "").strip()
        if city:
            get_weather(city)
        else:
            print("Please specify a city. For example: 'weather in London'")
  else:
         speak("I dont understand !!")