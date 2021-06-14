from django.shortcuts import render
from django.conf import settings


def address_formatter(address):
	# cealns the addresses plassed in by URL to make it human-readable
	
	cleaned_address = address.split('-')
	while 'None' in cleaned_address:
		cleaned_address.remove('None')
	
	return ', '.join(cleaned_address)

'''
Basic view for displaying a map 
'''
def map(request):
	start_address = address_formatter(request.GET['start'])
	end_address = address_formatter(request.GET['end'])
	context = {"google_api_key": settings.GOOGLE_API_KEY, 'start': start_address, 'end': end_address}
	
	return render(request, 'directions/maps.html', context)