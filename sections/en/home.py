import streamlit as st

# Función para añadir un párrafo recibiendo un texto como parametro
def parrafo(text):
    st.markdown(text)

# Función para añadir un enlace
def enlace(enlace, titulo):
    st.page_link(enlace, label=titulo)

st.markdown(
    """
    <h2 style="text-align: center; color: #4CAF50;">
        MAP Girls for TECH
    </h2>
    """, 
    unsafe_allow_html=True
)

# Texto: Presentación del equipo

st.markdown(
    "Hello, we are **Maite**, **Ana**, and **Pilar**, and together we form the team MAP Girls for Tech. We are participating for the third consecutive year in the Technovation Girls project, whose goal is to bring technology closer to girls and young women aged 8 to 18. The idea is to increase the presence of women in STEM careers through this initiative."
)
parrafo("We must find a problem in our community that meets one or more of the UN Sustainable Development Goals 2030. During 12 weeks we must work to give a solution to that problem and create a mobile App or a Web App with that solution. ")

parrafo("In this program, teams of girls from all over the world participate and compete in three categories, Beginner, Junior and Senior. ")

parrafo("We girls learn among many other things to program, train AI models and to present our ideas and work in public.")

parrafo("You can learn more about this program through the following link:")

# Crear un enlace con apariencia de botón
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
    <a href="https://technovationchallenge.org/" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 5px 20px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
            Technovation Girls Program
        </button>
    </a>
    </div>
    """, 
    unsafe_allow_html=True
)

parrafo(" ")

parrafo("One problem that has come to our attention is that there are no women's sports shoes for female soccer players. It is crucial to use appropriate footwear when playing sports, as the use of sports shoes that are not suitable for women's feet can cause serious injuries. This has happened to our colleague Pilar, as well as to many other women, who due to the lack of footwear adapted to their feet suffer injuries, sometimes serious, as they are forced to resort to men's footwear. This is Pilar's testimony:")

# Centrar la cita, pero alineada a la izquierda
st.markdown(
    """
    <div style="display: flex; justify-content: center; width: 80%;">
        <blockquote style="text-align: left; font-style: italic; font-size: 1em; border-left: 5px solid #ccc; padding-left: 10px;">
            “I have played soccer since I was 5 years old and I love sports, but I have never found boots designed specifically for girls. I have suffered from several ankle injuries, but my last injury was the most serious of all, specifically to my knee and I had to be on total rest for 4 months.”
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True
)

parrafo(" ")

parrafo("Faced with this problem, the lack of sports footwear suitable for women's feet in many women's sports, is where we are going to focus our project this season.")

parrafo("We have created a questionnaire with a series of questions that will help us shape the project and try to find a solution to this problem. ")

st.markdown("<h4 style='text-align: center;'>WE NEED YOUR HELP!!!!!</h4>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Could you answer our questionnaire?</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center;'>Thank you very much</h5>", unsafe_allow_html=True)

# Crear un enlace con apariencia de botón
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
    <a href="https://technovationchallenge.org/" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 5px 20px; font-size: 16px; border: none; cursor: pointer; border-radius: 5px;">
            Go to Questionnaire
        </button>
    </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# Crear una columna para centrar la imagen
col1, col2, col3 = st.columns([1, 3, 1])  # Tres columnas, el centro tiene el triple de peso
# Usar la columna central para colocar la imagen
with col2:
    st.image("./images/Logo-Circular-WEB_OK.png", use_container_width=True)