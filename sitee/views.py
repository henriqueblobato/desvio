from django.shortcuts import render

from sitee.models import Camera, Image


def index(request):
    images = Image.objects.order_by("?")
    return render(
        request, "index.html",
        {
            "images": [
                {
                    "url": i.url,
                    "name": i.name,
                }
                for i in images
            ],
        }
    )


def random_camera_view(request):
    cameras = Camera.objects.order_by("?")[:1]

    return render(
        request, "random_camera.html",
        {
            "cameras": [
                {
                    "mime": c.mime,
                    "data": c.data,
                    "name": c.name,
                    "location": c.location,
                }
                for c in cameras
            ]
        }
    )
