import base64
from openai import OpenAI
from io import BytesIO
from PIL import Image

class HalloweenImageTransformer:
    """
    Classe pour transformer des images en version Halloween avec OpenAI,
    puis ajouter un bandeau en bas de l’image.
    """

    THEMES = {
        "vampire": "vampire élégant",
        "sorcière": "sorcière moderne",
        "zombie": "zombie rigolo en costume de bureau",
        "citrouille": "citrouille humanoïde souriante",
        "squelette": "squelette dansant",
    }

    BASE_PROMPT = """
    Transforme la personne sur cette image en une version cartoon semi-réaliste d’elle-même pour Halloween.
    Garde le visage reconnaissable (forme du visage, yeux, cheveux).
    Donne-lui un costume de {theme}.
    Style illustration numérique colorée, ambiance lumineuse d’Halloween (orange, violet, vert).
    Amusant et festif, pas effrayant. Fond stylisé Halloween (citrouilles, brume, lune).
    """

    def __init__(self, api_key: str, banner_path: str = "assets/logo.png"):
        if not api_key:
            raise ValueError("La clé API OpenAI est manquante.")
        self.client = OpenAI(api_key=api_key)
        self.banner_path = banner_path

    def transform_face(self, effect: str, image_bytes: bytes) -> bytes:
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

            edited_image_base64 = response.data[0].b64_json
            edited_image_bytes = base64.b64decode(edited_image_base64)

            result_img = self._add_banner(edited_image_bytes)

            output = BytesIO()
            result_img.save(output, format="PNG")
            return output.getvalue()

        except Exception as e:
            print(f"[ERREUR] Transformation échouée : {e}")
            raise

    def _add_banner(self, image_bytes: bytes) -> Image.Image:
        """Ajoute un bandeau (logo Halloween) en bas de l’image avec fond gris transparent."""
        base_img = Image.open(BytesIO(image_bytes)).convert("RGBA")
        banner = Image.open(self.banner_path).convert("RGBA")

        target_height = int(base_img.height * 0.20)
        aspect_ratio = banner.width / banner.height
        target_width = int(target_height * aspect_ratio)

        banner = banner.resize((target_width, target_height), Image.LANCZOS)

        gray_bg = Image.new("RGBA", (base_img.width, target_height), (1, 11, 29, 150))

        y_pos = base_img.height - target_height
        x_pos = (base_img.width - target_width) // 2

        base_img.alpha_composite(gray_bg, (0, y_pos))
        base_img.alpha_composite(banner, (x_pos, y_pos))

        return base_img