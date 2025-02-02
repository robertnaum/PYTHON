import folium
import os

m = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

folium.CircleMarker(
    location=[37.7749, -122.4194],
    radius=50,
    popup='San Francisco',
    color="blue",
    fill = True,
    fill_color = 'blue').add_to(m)

m.save('map.html')
os.system('start map.html')

