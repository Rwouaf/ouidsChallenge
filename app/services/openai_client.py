import base64
from openai import OpenAI
from io import BytesIO

class HalloweenImageTransformer:
    """
    Classe pour transformer des images en version Halloween avec OpenAI.
    Initialise le client OpenAI une seule fois avec la clé d'API.
    """

    # Liste des thèmes possibles
    THEMES = {
        "vampire": "vampire élégant",
        "sorcière": "sorcière moderne",
        "zombie": "zombie rigolo en costume de bureau",
        "citrouille": "citrouille humanoïde souriante",
        "squelette": "squelette dansant",
    }

    # Prompt de base pour la transformation
    BASE_PROMPT = """
    Transforme la personne sur cette image en une version cartoon semi-réaliste d’elle-même pour Halloween.
    Garde le visage reconnaissable (forme du visage, yeux, cheveux).
    Donne-lui un costume de {theme}.
    Style illustration numérique colorée, ambiance lumineuse d’Halloween (orange, violet, vert).
    Amusant et festif, pas effrayant. Fond stylisé Halloween (citrouilles, brume, lune).
    """

    def __init__(self, api_key: str):
        """
        Initialise le client OpenAI avec la clé API fournie.
        :param api_key: Clé API OpenAI
        """
        if not api_key:
            raise ValueError("La clé API OpenAI est manquante.")
        self.client = OpenAI(api_key=api_key)

    def transform_face(self, effect: str, image_bytes: bytes) -> bytes:
        """
        Transforme une image en version Halloween selon le thème choisi.
        :param effect: Thème choisi (ex: "vampire", "zombie", etc.)
        :param image_bytes: Image en bytes (upload ou caméra)
        :return: Image transformée (bytes PNG)
        """
        theme = self.THEMES.get(effect.lower(), "créature d’Halloween")
        prompt = self.BASE_PROMPT.format(theme=theme)

        try:
            image_file = BytesIO(image_bytes)
            image_file.name = "input.jpg"

            response = self.client.images.edit(
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