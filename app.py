import streamlit as st
import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "de"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"🌤 Wetter in {city}: {weather}, {temperature}°C"
    else:
        return f"❌ Fehler: {data.get('message', 'Unbekannter Fehler')}"

# UI
st.set_page_config(page_title="Wetter App", page_icon="🌤️")
st.title("🌤️ Wetter-App")
city = st.text_input("Stadt eingeben", "Berlin")

if city:
    api_key = st.secrets["api_key"]
    if st.button("Wetter anzeigen"):
        result = get_weather(city, api_key)
        st.success(result)
