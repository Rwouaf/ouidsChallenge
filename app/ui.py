import streamlit as st
from io import BytesIO
from services.simulate_client import transform_face

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
    st.image(image, caption="Image d’origine", width="stretch")

# --- ACTION ---
st.markdown("---")
btn = st.button("🧛‍♂️ Transformer maintenant !", type="primary", disabled=not image)

if btn and image:
    with st.spinner("Transformation en cours..."):
        try:
            transformed_bytes = transform_face(effect, image.getvalue())

            st.success(f"Effet {effect} appliqué avec succès ! ✨")
            st.image(transformed_bytes, caption=f"Résultat ({effect})", width="stretch")

            st.download_button(
                label="📥 Télécharger le résultat",
                data=transformed_bytes,
                file_name=f"halloween_{effect}.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
