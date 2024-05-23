import streamlit as st
from PIL import Image 

st.title(" ¡Aprende lenguaje de señas colombiano!" )

st.write("""
### Descubre el poder más allá de las palabras

Bienvenido a nuestra plataforma de aprendizaje del Lenguaje de Señas Colombiano (LSC). 
En Colombia y el mundo, el lenguaje de señas es una herramienta vital para la comunicación inclusiva. 
Esta plataforma tiene como objetivo facilitar el aprendizaje de LSC, permitiendo a más personas comunicarse efectivamente con la comunidad sorda.
""")

image = Image.open('LenguajeSeñas1.jpg')
new_width = 500
new_height = 300
image_resized = image.resize((new_width, new_height))
st.image(image_resized)

st.write("""
### ¿Por qué es importante aprender LSC?

El Lenguaje de Señas Colombiano es la lengua materna de muchas personas sordas en nuestro país, Colombia cuenta con 439.772 ciudadanos sordos, según la Encuesta Nacional de Calidad de Vida 2022. Aprender LSC se vuelve vital porque:

- Promueve la inclusión y la comunicación efectiva.
- Fortalece las relaciones personales y profesionales.
- Ayuda a derribar barreras de comunicación y a crear una sociedad más justa.
""")

video_url = "https://www.youtube.com/watch?v=tJz9iwuU6aY" 
st.video(video_url)

st.write("""
### ¿Qué podrás aprender y encontrar en esta plataforma? 

El propósito  es proporcionar una plataforma accesible y amigable para aprender LSC de manera facil. A través de nuestros módulos, aprenderás:

1. *Básico: El Abecedario*:
Comenzarás con lo más esencial, el abecedario.

2. *Básico: Tu nombre*:
Aprenderás a deletrear tu nombre y presentarte.

3. *Básico: Tu propia seña*:
Crearás tu propia seña, será una forma única de ser reconocida y comunicarte en la comunidad sorda.
""")


st.subheader("¡Continuemos!") 

st.write("Ya puedes dirigirte al siguiente módulo **'Básico: Abecedario'**")

st.markdown("[Siguiente módulo: Básico: Abecedario](https://aprendelenguajedesenas.streamlit.app/B%C3%A1sico:_abecedario)")
        
