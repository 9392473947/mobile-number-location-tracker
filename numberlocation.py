import phonenumbers
from main import number
from phonenumbers import geocoder
key="2e194ef6a1d84020b72f6dcf94f7f0e3"
import folium

chainumber=phonenumbers.parse(number)
yourloc=geocoder.description_for_number(chainumber,"en")
print(yourloc)

from phonenumbers import carrier

service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourloc)
results=geocoder.geocode(query)
print(results)

lat=(results[0]['geometry']['lat'])
lng=(results[0]['geometry']['lng'])
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourloc).add_to((myMap))

myMap.save("mylocation.html")