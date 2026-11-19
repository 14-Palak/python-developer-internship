
from flask import Flask, render_template, request
import requests
from config import API_KEY

app = Flask(__name__)

# OpenWeather API URL
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."

        else:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            try:
                response = requests.get(
                    WEATHER_URL,
                    params=params,
                    timeout=10
                )

                if response.status_code == 200:
                    data = response.json()

                    weather = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "wind": data["wind"]["speed"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"]
                    }

                elif response.status_code == 404:
                    error = "City not found. Please try another city."

                elif response.status_code == 401:
                    error = "Invalid or inactive API key. Please check your API key."

                else:
                    error = "Unable to fetch weather data. Please try again."

            except requests.exceptions.Timeout:
                error = "Weather service took too long to respond."

            except requests.exceptions.RequestException:
                error = "Please check your internet connection."

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
