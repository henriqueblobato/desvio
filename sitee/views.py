import requests
from django.shortcuts import render

from desvio.settings import RANDOM_IMAGE


def get_image_url(image_path):
    response = requests.get(image_path, allow_redirects=True)
    final_url = response.url
    return final_url


def index(request):
    images = [
        {
            "name": f"i{i+1}",
            "url": get_image_url(RANDOM_IMAGE),
        }
        for i in range(6)
    ]
    return render(request, "index.html", {"images": images})