import os
import requests
import json

# pulled from the github repo: https://github.com/bobby-didcoding/did_django_google_maps_api
# from following YouTube video: https://www.youtube.com/watch?app=desktop&v=wCn8WND-JpU


'''
Handles directions from Google
'''
def Directions(*args, **kwargs):

	lat_a = kwargs.get("lat_a")
	long_a = kwargs.get("long_a")
	lat_b = kwargs.get("lat_b")
	long_b = kwargs.get("long_b")

	origin = f'{lat_a},{long_a}'
	destination = f'{lat_b},{long_b}'

	result = requests.get(
		'https://maps.googleapis.com/maps/api/directions/json?',
		 params={
		 'origin': origin,
		 'destination': destination,
		 "key": os.environ.get("GOOGLE_MAPS_API_KEY")
		 })

	directions = result.json()

	if directions["status"] == "OK":

		route = directions["routes"][0]["legs"][0]
		origin = route["start_address"]
		destination = route["end_address"]
		distance = route["distance"]["text"]
		duration = route["duration"]["text"]

		steps = [
			[
				s["distance"]["text"],
				s["duration"]["text"],
				s["html_instructions"],

			]
			for s in route["steps"]]


	return {
		"origin": origin,
		"destination": destination,
		"distance": distance,
		"duration": duration,
		"steps": steps
		}