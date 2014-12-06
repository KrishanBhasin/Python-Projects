from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt

geolocator = Nominatim()

def haversine(lon1,lat1,lon2,lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1,lat1,lon2,lat2])
	
	dlon = lon1-lon2
	dlat = lat1-lat2
	
	a = sin(dlat/2)*sin(dlat/2)+cos(lat1)*cos(lat2)*sin(dlon/2)*sin(dlon/2)
	c = 2*asin(sqrt(a))
	
	return 6378.1*c #6378.1km == radius of earth

def city_locator():
	city1 = geolocator.geocode(str(input("Please enter the name of city 1:\n")))
	print(city1.address)
	city2 = geolocator.geocode(str(input("Please enter the name of city 2:\n")))
	print(city2.address)
	
	distance = haversine(city1.longitude,city1.latitude,city2.longitude,city2.latitude)
	
	print("")
	print("%s \nand\n%s\nare %.3f km apart"%(city1.address, city2.address,distance))
	
	
	
city_locator()