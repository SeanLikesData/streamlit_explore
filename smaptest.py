import streamlit as st
import folium

def create_map(lat,lon,zoom):
    m = folium.Map(location=[lat,lon], zoom_start=zoom)
    return m

st.title("My Map App Built with Streamlit and Folium")

lat = st.number_input("Latitude", value = 37.79048192546293)
lon = st.number_input("Longitude", value = -122.3996870713028)
zoom = st.slider("Zoom Level", 1, 20, 10)

map = create_map(lat,lon,zoom)

st.write(map._repr_html_(), unsafe_allow_html=True)

