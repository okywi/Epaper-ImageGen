import json
import os.path
from aiohttp import web
import sys

class Rest:
    def __init__(self, image_generator):
        self.image_generator = image_generator
        try:
            with open('config.json', 'r') as config_file:
                config_data = json.load(config_file)
                cfg = config_data['config']['rest_api']
        except OSError as e:
            print("Configfile not found - Please check the File!", e)
            sys.exit()

        self.address = cfg['address']
        self.port = cfg['port']

    def start(self):
        try:
            app = web.Application()
            app.router.add_get("/health", self.health)
            app.router.add_get('/image', self.image)
            web.run_app(app, host=self.address, port=self.port)
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    async def health(request):
        return web.json_response({
            "status": "green",
        })

    async def image(self, request):
        room = request.rel_url.query["room"]
        path = self.image_generator.get_image_path(room)

        if not os.path.exists(path):
            return web.json_response({
                "response": "The file does not exist. Did you spell the room correctly?'"
            })

        return web.FileResponse(
            self.image_generator.get_image_path(room)
        )

