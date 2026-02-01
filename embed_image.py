import base64
import io
# You need to install the Pillow library to run this: pip install Pillow
from PIL import Image

# This is a base64 encoded string representing a small red dot image.
# You can convert your own images to base64 strings to embed them directly in the code.
image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="

def display_embedded_image():
    # Decode the base64 string back to bytes
    image_data = base64.b64decode(image_base64)
    
    # Create an image object from the bytes
    image = Image.open(io.BytesIO(image_data))
    
    # Display the image
    image.show()

if __name__ == "__main__":
    display_embedded_image()