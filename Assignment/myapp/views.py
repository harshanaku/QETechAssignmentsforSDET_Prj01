import requests
from django.shortcuts import render
import json
from django.http import JsonResponse

# API Base URL
REQRES_API_BASE = "https://reqres.in/api"

API_ENDPOINTS = {
    "GET SINGLE USER NOT FOUND": f"{REQRES_API_BASE}/users/23",
    "GET USER LIST": f"{REQRES_API_BASE}/users",
    "POST CREATE USER": f"{REQRES_API_BASE}/users",
}


def home(request):
    selected_option = request.GET.get("option")
    api_details = None

    if request.method == "POST" and request.POST.get("option") == "POST CREATE USER":
        name = request.POST.get("name")
        job = request.POST.get("job")
        url = API_ENDPOINTS["POST CREATE USER"]
        response = requests.post(url, json={"name": name, "job": job})
        api_details = {
            "request": url,
            "response": response.status_code,
            "data": json.dumps(response.json(), indent=4)
        }
        # return JsonResponse(response.json(), status=response.status_code)

    if request.method == "GET" and request.POST.get("option") == "GET USER LIST":
        url = API_ENDPOINTS[selected_option]
        response = requests.get(url)
        api_details = {
            "request": url,
            "response": response.status_code,
            "data": json.dumps(response.json(), indent=4)
        }
        # return JsonResponse(response.json(), status=response.status_code)

    if request.method == "GET" and request.POST.get("option") == "GET SINGLE USER NOT FOUND":
        url = API_ENDPOINTS[selected_option]
        response = requests.get(url)
        api_details = {
            "request": url,
            "response": response.status_code,
            "data": json.dumps(response.json(), indent=4)
        }
        # return JsonResponse(response.json(), status=response.status_code)

    return render(request, "home.html",
                  {"api_endpoints": API_ENDPOINTS, "selected_option": selected_option, "api_details": api_details})


def support(request):
    return render(request, "support.html")
