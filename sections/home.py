import streamlit as st
from translations import translations
t = translations[st.session_state.language]
# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text,unsafe_allow_html=True)

# Función para añadir un enlace
def enlace(enlace, titulo):
    st.page_link(enlace, label=titulo)

parrafo(
    f"""
    <h2 style="text-align: center; color: #4CAF50;">
        {t["home"]["title"]}
    </h2>
    """
)

# Crear un enlace con apariencia de botón
def buttonLink(label, link):
    st.markdown(
       f"""
        <div style="display: flex; justify-content: center;">
        <a href="{link}" target="_blank">
            <button style="background-color: #4CAF50; color: white; padding: 5px 20px; margin-bottom: 10px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
                {label}
            </button>
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Texto: Presentación del equipo

parrafo(t["home"]["presentation"])


buttonLink(t["home"]["linkToProgram"], "https://technovationchallenge.org/")

parrafo(t["home"]["introductionToTestimony"])

# Centrar la cita, pero alineada a la izquierda
parrafo(
    f"""
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
             {t["home"]["testimony"]}
        </blockquote>
    </div>
    """
)

parrafo(t["home"]["projectFocus"])

parrafo(t["home"]["questionnaire"])

parrafo(f"<h4 style='text-align: center;'>{t['home']['needYourHelp']}</h4>")

parrafo(f"<h5 style='text-align: center;'>{t['home']['questionnaireRequest']}</h5>")

parrafo(f"<h5 style='text-align: center;'>{t['home']['thankYou']}</h5>")

buttonLink(t["home"]["questionnaireLink"], "https://technovationchallenge.org/")

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Logo-Circular-WEB_OK.png", use_container_width=True)