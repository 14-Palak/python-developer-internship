# Weatherly – Weather Application

Weatherly is a web-based weather application built using Python Flask and the OpenWeather API. It allows users to search for a city and view its current weather information.

## Features

- Search weather by city name
- Display temperature and feels-like temperature
- Show humidity and wind speed
- Display weather conditions and icons
- Handle invalid city names
- Handle API errors and connection issues
- Secure API key management using environment variables

## Technologies Used

- Python
- Flask
- OpenWeather API
- Requests
- Python-dotenv
- HTML5
- CSS3

## Project Structure

```text
04_Weather_App/
├── app.py
├── config.py
├── .env
├── .gitignore
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How to Run

1. Open the project folder in VS Code.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project folder.
4. Add your OpenWeather API key:

   ```env
   WEATHER_API_KEY=your_api_key_here
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open the local URL displayed in the terminal.

## Important Security Note

Never upload your actual `.env` file or API key to GitHub. The `.env` file is excluded using `.gitignore`.

## Learning Outcomes

- Integrating third-party REST APIs
- Working with Flask
- Managing environment variables
- Handling API responses and errors
- Building a dynamic web application

## Author

Palak Digarse

**Internship:** Python Developer Internship – Auspify Technologies