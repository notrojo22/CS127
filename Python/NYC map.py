#Rojas Shrestha
#rojas.shrestha85@myhunter.cuny.edu
#April 15, 2024
#This program uses foilum to print out a map of NYC

import folium

nyc_map = folium.Map(location = [40.75, -74.125], zoom_start = 12)

hunter_location = [40.7687, -73.9645]
folium.marker(hunter_location, popup = "Hunter College").add_to(nyc_map)
nyc_map.save("nycMap.html")
