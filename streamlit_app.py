import streamlit as st

translations = {
    "en": {"home": "Home",  "image_identifier": "Image Identifier", "foro": "Forum"},
    "es": {"home": "Inicio",  "image_identifier": "Identificador de pisada", "foro": "Foro"},	
}

# Helper para traducir los textos
def translate(text):
    return translations[st.session_state.language][text]


languages_options = {"en": "English", "es": "Español"}
# Helper para obtener el label del idioma en base al indice
def format_func(option):
    return languages_options[option]

# Inicializar estado global si no existe
if "language" not in st.session_state:
    st.session_state.language = "es"  # Idioma por defecto

# Genera el selector de idiomas
with st.sidebar:
    selected_language = st.selectbox("language selector",list(languages_options.keys()), index=list(languages_options.keys()).index(st.session_state.language), label_visibility="collapsed",format_func=format_func)
# Guarda el idioma seleccionado en el estado de sesión
if selected_language != st.session_state.language:
    st.session_state.language = selected_language

home = st.Page(f'sections/home.py',
                       title=translations[selected_language]["home"], default=True)
imageIdentifier = st.Page(
    "imageIdentifier.py", title=translate("image_identifier"), icon="🔥"
)

foro = st.Page(
    'sections/foro.py', title=translate("foro")
)

# Funciona como router, desde aca se renderizan las paginas

# Con esto configuro a mano las paginas pudiendo customizar el titulo e icono
pg = st.navigation(
    {
        "": [home, imageIdentifier, foro]

    }
)

pg.run()