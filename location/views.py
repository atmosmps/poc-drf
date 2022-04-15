from django.conf import settings
from django.shortcuts import render

from location.client import LocationClient

client = LocationClient()


def my_location(request):
    data = client.get()
    return render(
        request,
        "location/index.html",
        {"ip": data["ip"], "country": data["country_name"]},
    )


def my_ip_address(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        data = client.get_data_from_my_ip()
        request.session['geodata'] = data

    geodata = request.session['geodata']
    return render(
        request,
        "location/index.html",
        {
            "ip": geodata["ip"],
            "country": geodata["country_name"],
            "latitude": geodata["latitude"],
            "longitude": geodata["longitude"],
            "api_key": settings.GMAPS_API_KEY,
            'is_cached': is_cached
        },
    )
