from src.image_generator import ImageGenerator
from src.rest_api import Rest

if __name__ == '__main__':
    image_generator = ImageGenerator()
    rest = Rest(image_generator)

    rest.start()