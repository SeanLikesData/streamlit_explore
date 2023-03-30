import streamlit as st
import folium
import geopandas as gpd

# Load the Shapefile
gdf = gpd.read_file("geo_export_844c2f95-cd14-43b0-b47a-8613f7501b2e.shp")

# Function to define the style of the polygons
def style_function(feature):
    return {
        'fillColor': '#3186cc',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    }

def create_map(gdf, lat,lon,zoom, style_function):
    m = folium.Map(
        location=[lat,lon], 
        zoom_start=zoom
    )

    # Add the shapefile overlay to the map using GeoJson
    folium.GeoJson(
        gdf,
        style_function=style_function,
        tooltip = folium.GeoJsonTooltip(fields=['name'], aliases=['name'])
        ).add_to(m)
    return m

st.title("San Francisco Neighborhoods")

lat = st.number_input("Latitude", value = 37.79048192546293)
lon = st.number_input("Longitude", value = -122.3996870713028)
zoom = st.slider("Zoom Level", 1, 20, 10)

map = create_map(gdf,lat,lon,zoom, style_function)

st.write(map._repr_html_(), unsafe_allow_html=True)

