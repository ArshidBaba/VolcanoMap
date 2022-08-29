import folium
import pandas as pd

map4 = folium.Map(location=[1.7400339, -16.2444486], zoom_start=15, tiles='Stamen Terrain')
currentFile = open('volcano_data.csv', 'rt', encoding='latin1')
df = pd.read_csv(currentFile)

df.dropna(inplace=True)
df['VolcanoName'] = df['VolcanoName'].str.replace("'", "$#39;")

def color(elev):
	if elev < 0:
		col = 'black'
	elif elev in range(0,1000):
		col = 'green'
	elif elev in range(1001, 1999):
		col = 'blue'
	elif elev in range(2000, 2999):
		col = 'orange'
	else:
		col = 'red'
	return col


for lat,lon,name,elev in zip(df['Latitude'], df['Longitude'], df['VolcanoName'], df['Elevation']):
	folium.Marker(location=[lat,lon], popup=name, icon=folium.Icon(color=color(elev), icon='cloud')).add_to(map4)

print(map4.save('map.html'))