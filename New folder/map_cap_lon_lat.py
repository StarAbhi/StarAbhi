import folium
from folium import plugins
import pandas as pd


df = pd.read_csv('capitals_lat_lon.csv')
df.head()
m = folium.Map([39.93333333,32.866667], zoom_start=3)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], 
                  popup=row['Capital'],
                  icon=folium.Icon(icon='cloud')).add_to(m)

m.save('Capitals.html')
