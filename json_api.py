import json
import urllib.parse
import requests
import time



#start = time.time()


main_addr = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Address : ')

url = main_addr + urllib.parse.urlencode({'address' : address})


json_Data = requests.get(url).json()

#print(json_Data)


json_status = json_Data['status']

print("API status " + json_status +'\n')

if json_status == 'OK':


	json_address = json_Data['results'][0]['formatted_address']
	print(json_address)

	for i in json_Data['results'][0]['address_components']:


		print(i['long_name'])
	


else:


	print("please enter a valid address")


#end = time.time()

#print(end - start)
