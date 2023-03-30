# Create a streamlit web app that displays the san francisco neighborhood polygons on a follium map

import streamlit as st
import geopandas as gpd
import folium

st.header("San Francisco Neighborhoods")
st.subheader("A map of the neighborhoods in San Francisco")

# Load the Shapefile
neighborhoods = gpd.read_file("~/sf_polygons/geo_export_844c2f95-cd14-43b0-b47a-8613f7501b2e.shp")

st.dataframe(neighborhoods)








# Calculate the map's center point
center_point = neighborhoods.geometry.centroid.unary_union.centroid

# Create a base map centered on San Francisco
sanfrancisco_map = folium.Map(
    location=[center_point.y, center_point.x],
    zoom_start=12,
    control_scale=True
)

# Function to define the style of the polygons
def style_function(feature):
    return {
        'fillColor': '#3186cc',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    }


# Convert the GeoDataFrame to a GeoJSON format
neighborhoods_geojson = neighborhoods.to_json()

# Add the neighborhood polygons to the map
folium.GeoJson(
    neighborhoods_geojson,
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['name'])
).add_to(sanfrancisco_map)

sanfrancisco_map