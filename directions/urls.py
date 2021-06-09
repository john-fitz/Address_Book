from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	# path('<str:start_address>/<str:end_address>', views.route, name="route"),
	path('', views.route, name="route"),
	path('map/', views.map, name="map"),
	]