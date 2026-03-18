import requests
from datetime import datetime
import os

IMAGE_URL = "https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg" 
SAVE_DIR = "images"

os.makedirs(SAVE_DIR, exist_ok=True)

def download_image():
    try:
        response = requests.get(IMAGE_URL, timeout=30)
        response.raise_for_status()

        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(SAVE_DIR, f"image_{timestamp}.jpg")

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_image()
