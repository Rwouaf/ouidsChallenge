from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance
import random

def transform_face(effect: str, image_bytes: bytes) -> bytes:
    """Mock de transformation d'image — simule un effet selon le thème choisi."""
    img = Image.open(BytesIO(image_bytes)).convert("RGB")

    # Applique un effet pour tester l'UI
    if effect == "zombie":
        img = ImageOps.colorize(ImageOps.grayscale(img), black="green", white="yellow")
    elif effect == "vampire":
        img = ImageOps.colorize(ImageOps.grayscale(img), black="red", white="white")
    elif effect == "squelette":
        img = ImageOps.invert(img)
    elif effect == "sorcière":
        img = ImageEnhance.Color(img).enhance(2.5)
    elif effect == "citrouille":
        img = ImageOps.colorize(ImageOps.grayscale(img), black="orange", white="black")
    else:
        img = img

    # Ajoute une légère variation aléatoire pour tester visuellement
    img = ImageEnhance.Brightness(img).enhance(random.uniform(0.8, 1.2))

    output = BytesIO()
    img.save(output, format="PNG")
    return output.getvalue()
