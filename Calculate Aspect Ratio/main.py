## Create a function that calculates aspect ratio from the given numbers
## It also should be able to tell you the aspect ratio of a given image
## from a provided URL
from fractions import Fraction
import urllib.request as urlr
from PIL import Image

def get_image_from_web(url):
    image_name =  url.split("/")[-1]
    urlr.urlretrieve(url, image_name)

    return image_name

def get_image_width_height(image_name):
    image = Image.open(image_name)
    
    return image.size


def calculate_aspect_ratio(width, height):
    asp_ratio = "%.15f" % (width / height)
    asp_ratio = Fraction(asp_ratio).limit_denominator()
    return asp_ratio

def get_aspect_ratio_from_url(url):
    image_name = get_image_from_web(url)

    image_size = get_image_width_height(image_name)

    return calculate_aspect_ratio(image_size[0], image_size[1])

# Main
if __name__ == "__main__":
    url = input("URL of the image: ")
    print(f"Size of the image -> {get_image_width_height(get_image_from_web(url))}\nAspect ratio -> {get_aspect_ratio_from_url(url)}")