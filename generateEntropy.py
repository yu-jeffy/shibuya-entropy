import hashlib
from PIL import Image
import base64
import random
from shibuyaStream import download_frame

def image_to_alphanumeric_code(image_path):
    # Load the image
    img = Image.open(image_path)
    # Convert image to RGB (if not already in that format)
    rgb_img = img.convert('RGB')
    
    # Create a byte array from the RGB values of all pixels
    data_bytes = bytearray()
    for x in range(rgb_img.width):
        for y in range(rgb_img.height):
            r, g, b = rgb_img.getpixel((x, y))
            data_bytes.extend([r, g, b])
    
    # Compute SHA-256 hash of the pixel data
    hasher = hashlib.sha256()
    hasher.update(data_bytes)
    hash_digest = hasher.digest()

    # Encode the hash digest to produce a base64 alphanumeric code
    base64_encoded = base64.urlsafe_b64encode(hash_digest).decode('utf-8').rstrip('=')

    # Randomly select 32 characters from the base64 string
    if len(base64_encoded) > 32:
        selected_characters = ''.join(random.sample(base64_encoded, 32))
    else:
        selected_characters = base64_encoded  # In case the length is unexpectedly short

    return selected_characters

def main():
    # Specify the image file name
    image_file = 'shibuya.jpg'
    # Download the frame
    download_frame()
    # Generate alphanumeric code from the image
    code = image_to_alphanumeric_code(image_file)
    print()
    print("Generated Value:", code)
    print()

if __name__ == "__main__":
    main()
