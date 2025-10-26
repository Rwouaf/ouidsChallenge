import base64
from openai import OpenAI
from io import BytesIO

# ----------------- CONFIGURATION -----------------
client = OpenAI(api_key="OPENAI_API_KEY")

# Liste de thèmes Halloween
themes = {
    "vampire": "vampire élégant",
    "sorcière": "sorcière moderne",
    "zombie": "zombie rigolo en costume de bureau",
    "citrouille": "citrouille humanoïde souriante",
    "squelette": "squelette dansant",
}

# Prompt de base
BASE_PROMPT = """
Transforme la personne sur cette image en une version cartoon semi-réaliste d’elle-même pour Halloween.
Garde le visage reconnaissable (forme du visage, yeux, cheveux).
Donne-lui un costume de {theme}.
Style illustration numérique colorée, ambiance lumineuse d’Halloween (orange, violet, vert).
Amusant et festif, pas effrayant. Fond stylisé Halloween (citrouilles, brume, lune).
"""

def transform_face(effect: str, image_bytes: bytes) -> bytes:
    """
    Transforme une image en version Halloween selon le thème choisi.
    :param effect: Thème choisi (ex: "vampire", "zombie", etc.)
    :param image_bytes: Image en bytes (upload ou caméra)
    :return: Image transformée (bytes PNG)
    """
    theme = themes.get(effect.lower(), "créature d’Halloween")
    prompt = BASE_PROMPT.format(theme=theme)

    try:
        image_file = BytesIO(image_bytes)
        image_file.name = "input.jpg"

        response = client.images.edit(
            model="gpt-image-1",
            image=image_file,
            prompt=prompt,
            size="1024x1024",
            quality="medium",
        )

        # Récupération de l'image générée (base64)
        edited_image_base64 = response.data[0].b64_json
        edited_image_bytes = base64.b64decode(edited_image_base64)
        return edited_image_bytes

    except Exception as e:
        print(f"[ERREUR] Transformation échouée : {e}")
        raise
