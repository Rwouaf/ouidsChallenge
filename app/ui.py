import streamlit as st
from services.simulate_client import transform_face

# --- CONFIG ---
st.set_page_config(page_title="🎃 Halloween Transformer", page_icon="🎃", layout="centered")

# --- INIT SESSION ---
if "page" not in st.session_state:
    st.session_state.page = "camera"
if "photo" not in st.session_state:
    st.session_state.photo = None
if "effect" not in st.session_state:
    st.session_state.effect = None
if "result" not in st.session_state:
    st.session_state.result = None


# --- NAVIGATION ---
def go_to(page: str):
    st.session_state.page = page
    # Pas de st.rerun ici : Streamlit relancera automatiquement le script au prochain cycle


# ------------------------------
# PAGE 1 : Prendre ou uploader une photo
# ------------------------------
if st.session_state.page == "camera":
    st.title("📸 Prends ta photo")

    cam_img = st.camera_input("Prendre une photo")
    up_img = st.file_uploader("Ou choisis une photo", type=["png", "jpg", "jpeg"])

    image = cam_img or up_img

    # 🚀 Dès qu'on a une photo, on passe à l'étape suivante automatiquement
    if image:
        st.session_state.photo = image
        go_to("filter")
        st.rerun()

    st.divider()
    st.button("🔒 Confidentialité / RGPD", on_click=lambda: go_to("rgpd"))


# ------------------------------
# PAGE 2 : Choisir un filtre
# ------------------------------
elif st.session_state.page == "filter":
    st.title("🧙‍♀️ Choisis ton filtre")

    st.image(st.session_state.photo, caption="Ta photo", width="stretch")

    effect = st.radio(
        "Sélectionne ton effet d’Halloween",
        ["zombie", "vampire", "squelette", "sorcière", "citrouille"],
        horizontal=True,
        key="filter_choice",
    )

    st.session_state.effect = effect

    st.button("👻 Transformer maintenant !", type="primary", on_click=lambda: go_to("transform"))
    st.button("↩️ Reprendre une photo", on_click=lambda: go_to("camera"))


# ------------------------------
# PAGE 3 : Transformation
# ------------------------------
elif st.session_state.page == "transform":
    st.title("🎃 Transformation en cours...")

    image = st.session_state.photo
    effect = st.session_state.effect

    with st.spinner(f"Application de l’effet **{effect}**..."):
        try:
            transformed_bytes = transform_face(effect, image.getvalue())
            st.session_state.result = transformed_bytes
            go_to("result")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Erreur : {e}")
            st.button("↩️ Revenir", on_click=lambda: go_to("camera"))


# ------------------------------
# PAGE 4 : Résultat final
# ------------------------------
elif st.session_state.page == "result":
    st.title("✨ Voici ton résultat !")

    if st.session_state.result:
        st.image(
            st.session_state.result,
            caption=f"Effet : {st.session_state.effect.capitalize()}",
            width="stretch",
        )

        st.download_button(
            label="📥 Télécharger le résultat",
            data=st.session_state.result,
            file_name=f"halloween_{st.session_state.effect}.png",
            mime="image/png",
        )
    else:
        st.warning("Aucune image transformée disponible. Essaie de recommencer.")

    st.button("🔁 Refaire une photo", on_click=lambda: go_to("camera"))
    st.button("🔒 Confidentialité / RGPD", on_click=lambda: go_to("rgpd"))


# ------------------------------
# PAGE 5 : RGPD / Confidentialité
# ------------------------------
elif st.session_state.page == "rgpd":
    st.title("🔒 Confidentialité & RGPD")

    st.markdown(
        """
        ## Notre engagement pour ta vie privée 🎃  

        Ce site respecte entièrement le **Règlement Général sur la Protection des Données (RGPD)**.  
        Voici les points essentiels :

        - 🖼️ **Aucune photo n’est conservée** :  
          Les images que tu prends ou importes sont **traitées uniquement en mémoire**, puis **immédiatement supprimées** après la transformation.

        - 🧠 **Aucune donnée personnelle n’est enregistrée** :  
          Nous ne stockons **aucune information d’utilisateur**, ni adresse IP, ni métadonnée, ni historique d’utilisation.

        - ⚙️ **Traitement local ou éphémère côté serveur** :  
          Les images sont transmises uniquement pour appliquer l’effet sélectionné, puis détruites instantanément après envoi du résultat.

        - 🚫 **Aucune utilisation commerciale, aucun tracking** :  
          Pas de cookies de suivi, pas d’analyse de comportement, pas de publicité.

        ---

        👻 *En résumé : ton visage t’appartient, et il disparaît du serveur aussitôt transformé.*  
        """
    )

    st.divider()
    st.button("⬅️ Retour", on_click=lambda: go_to("camera"))
