from django.shortcuts import render
from django.conf import settings

# pulled from the github repo: https://github.com/bobby-didcoding/did_django_google_maps_api
# from following YouTube video: https://www.youtube.com/watch?app=desktop&v=wCn8WND-JpU


from .mixins import Directions
'''
Basic view for routing 
'''
def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'directions/route.html', context)


'''
Basic view for displaying a map 
'''
def map(request):

	lat_a = request.GET.get("lat_a")
	long_a = request.GET.get("long_a")
	lat_b = request.GET.get("lat_b")
	long_b = request.GET.get("long_b")
	directions = Directions(
		lat_a= lat_a,
		long_a=long_a,
		lat_b = lat_b,
		long_b=long_b
		)

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,

	}
	return render(request, 'directions/maps.html', context)