import requests
from django.core.management.base import BaseCommand, CommandError

from desvio.settings import shodan_api
from sitee.models import Camera, Image


def get_cameras_url():
    shodan_query = 'screenshot.label:webcam country:"BR"'
    results = shodan_api.search(shodan_query, limit=50)
    cameras = [
        Camera.objects.create({
            "name": f"c{i+1}",
            "url": result["url"],
            "screenshot": result["screenshot"],
            "location": result["location"],
        })
        for i, result in enumerate(results["matches"])
    ]
    # add into the database the cameras
    return cameras


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        # shodan_query = 'screenshot.label:webcam country:"BR"'
        # results = shodan_api.search(shodan_query, limit=50)
        # for i, result in enumerate(results["matches"]):
        #     ss = result["screenshot"]
        #     mime = ss.get("mime")
        #     data = ss.get("data")
        #     g = Camera.objects.get_or_create(
        #         name=f"c{i+1}",
        #         # screenshot=screenshot,
        #         mime=mime,
        #         data=data,
        #         location=result["location"],
        #     )
        #     self.stdout.write(self.style.SUCCESS(f"Successfully created camera {i+1}"))

        for c in range(50):
            final_url = requests.get("https://picsum.photos/500/500", allow_redirects=True).url
            g = Image.objects.get_or_create(
                name=f"i{c+1}",
                url=final_url,
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully created image {c+1}"))
