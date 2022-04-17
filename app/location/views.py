from app.location.extensions import IPStackBackend
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def get_data_from_my_ip(request):
    backend = IPStackBackend()
    is_cached = "geodata" in request.session

    if not is_cached:
        my_ip_data = backend.get_data_from_my_ip()
        request.session["geodata"] = my_ip_data

    geodata = request.session["geodata"]
    return render(
        request,
        "location/index.html",
        {
            "ip": geodata["ip"],
            "country": geodata["country_name"],
            "latitude": geodata["latitude"],
            "longitude": geodata["longitude"],
            "api_key": settings.GMAPS_API_KEY,
            "is_cached": is_cached,
        },
    )


def get_data_from_my_ip_json_response(request):
    backend = IPStackBackend()
    is_cached = "geodata" in request.session

    if not is_cached:
        my_ip_data = backend.get_data_from_my_ip()
        request.session["geodata"] = my_ip_data

    geodata = request.session["geodata"]
    return JsonResponse(geodata)
