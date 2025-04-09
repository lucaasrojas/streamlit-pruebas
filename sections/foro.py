import streamlit as st
from translations import translations
t = translations[st.session_state.language]

# Datos de ejemplo
foros = {
    "1": {
        "title": "Shoes",
        "description": "Descripción breve del tema 1", 
        "comments": [
            {
                "id": 1, 
                "text": "Comentario 1", 
                "user":{
                    "name":"Usuario 1", 
                    "id":1
                }
            },
            {
                "id": 2, 
                "text": "Comentario 2", 
                "user":{
                    "name":"Usuario 3", 
                    "id":3
                }
            }
        ]
    },	
}

# Página principal
st.title(t["foro"]["title"])

# Mostrar tarjetas con títulos y descripciones
for key, values in foros.items():
    if st.button(f"{values["title"]} - {values['description']}"):
        st.session_state["tema_actual"] = key
        # st.experimental_rerun()

# Página de discusión
if "tema_actual" in st.session_state:
    tema = st.session_state["tema_actual"]
    st.header(foros[tema]["title"])
    st.write(foros[tema]["description"])
    
    # Mostrar comentarios
    st.subheader(t["foro"]["comments"])
    for comentario in foros[tema]["comments"]:
        st.write(f"- {comentario["text"]} (por {comentario["user"]["name"]})")

    # Agregar nuevo comentario
    # nuevo_comentario = st.text_input("Añade tu comentario")
    # if st.button("Enviar"):
    #     foros[tema]["comentarios"].append(nuevo_comentario)
    #     # st.experimental_rerun()