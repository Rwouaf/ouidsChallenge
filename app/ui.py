import streamlit as st
from io import BytesIO

# -- IMPORTS FUTURS --
# from app.services.openai_client import transform_face
# from app.services.storage import save_image_bytes
# from app.services.mailer import send_image

# --- CONFIG DE BASE ---
st.set_page_config(page_title="🎃 Halloween Transformer", page_icon="🎃", layout="centered")
st.title("🎃 Halloween Face Transformer")

st.markdown("Transforme-toi en créature d’Halloween avec l’IA 🧙‍♀️")

# --- CHOIX DE L'EFFET ---
effect = st.selectbox(
    "Choisis ton effet",
    ["zombie", "vampire", "squelette", "sorcière", "citrouille"]
)

# --- UPLOAD / CAMÉRA ---
st.markdown("### 📸 Prends une photo ou envoie-en une :")
col1, col2 = st.columns(2)
with col1:
    cam_img = st.camera_input("Prendre une photo")
with col2:
    up_img = st.file_uploader("Uploader une photo", type=["png", "jpg", "jpeg"])

image = cam_img or up_img

if image:
    st.image(image, caption="Image d’origine", use_container_width=True)

# --- ACTION ---
st.markdown("---")
btn = st.button("🧛‍♂️ Transformer maintenant !", type="primary", disabled=not image)

if btn and image:
    with st.spinner("Transformation en cours..."):
        # Ici tu appelleras la méthode de ton backend :
        # transformed_bytes = transform_face(effect, image.getvalue())
        # save_image_bytes(transformed_bytes, effect)
        # (pour l’instant on simule le résultat)

        st.success(f"Effet {effect} appliqué avec succès ! ✨")
        st.image(image, caption=f"Résultat simulé ({effect})", use_container_width=True)

        # Téléchargement (fictif pour le moment)
        st.download_button(
            label="📥 Télécharger le résultat",
            data=image.getvalue(),
            file_name=f"halloween_{effect}.png",
            mime="image/png"
        )

