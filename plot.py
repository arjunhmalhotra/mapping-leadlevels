import matplotlib as mp1
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

filename = 'soil.txt' #This code opens and reads the .txt document with the lead levels
f = open(filename, 'r')
contents = f.readline()

latitudes = []
longitudes = []
leadlvl = []
for line in f:
    row = line.split(',') #Splitting the rows of data and appending their values to fall under Latitude, Longitude, or Leadlvl
    latitudes.append(float(row[0]))
    longitudes.append(float(row[1]))
    leadlvl.append(float(row[2]))
f.close()

colors = []
for lead in leadlvl: #Appending the lead values to fall under a certain color for the scatterplot
    if lead < 400:
        colors.append('blue')
    elif lead < 1000:
        colors.append('yellow')
    elif lead < 2000:
        colors.append('orange')
    else:
        colors.append('red')
        
#Setting the boundaries and center of the map with longitude and lattitude values    
map = Basemap(llcrnrlon=-82.373,llcrnrlat=40.05,urcrnrlon=-82.387,urcrnrlat=40.07,
            resolution='i', projection='tmerc', lon_0=-82.38, lat_0 = 40.06)

map.drawmapboundary() #Inputting map variables (none of these matter because our map became so small)
map.drawparallels(np.arange(-90.,91.,30.))
map.drawmeridians(np.arange(-180.,181.,60.))

plt.title("Newark Ohio Lead Levels")
x, y = map(longitudes, latitudes) #plotting the scatter plot with the colors/variables we defined in the above code
map.scatter(x, y, color = colors)
plt.show()

   
