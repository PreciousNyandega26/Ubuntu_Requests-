import os
import requests
from urllib.parse import urlparse

def get_image_filename(url):
    """Extract filename from URL or generate one if not available."""
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = 'downloaded_image.jpg'
    return filename

def main():
    url = input("Enter the image URL: ").strip()
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    filename = get_image_filename(url)
    save_path = os.path.join(save_dir, filename)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Image saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
