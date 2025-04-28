import streamlit as st
import requests 

def get_data(city_name, n):
    KEY_API = "560038586685f35d59ab56cea1145ec4"
    url  = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={KEY_API}"
    response = requests.get(url)
    data = response.json()
    filter_data = [data['list']]

    temps = []
    dates = []
    for entry in filter_data[0][:n]:  # data[0] contains the list of weather records
        temp = entry["main"]["temp"]
        temp -= 273.15
        temps.append(temp)
        date = entry["dt_txt"]
        dates.append(date)

    st.write(temps)
    st.write(dates)



st.title("Weather Forecast fot the Next Day")

city = st.text_input(label="place",
              placeholder = "Enter City")

date = st.slider("Forecast Days",min_value=1,
          max_value=50,
          value=1)
n = date * 8

option = st.selectbox(
    "Select date to view",
    ("Temperature", "Sky"),
    placeholder="Select option"
)
st.write("You selected:", option)

st.subheader(f"{option} for the next {date} days in {city}")

if city:
    get_data(city, n)

# st.session_state
