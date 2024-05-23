import streamlit as st
import os
import random
import paho.mqtt.client as paho
import time
import json

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):  # create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

# Título y Subtítulo
st.title("¡Aprende lenguaje de señas colombiano!")
st.subheader("Básico: tu nombre")

# Cuerpo de Texto
st.write("""
En la comunidad de personas sordas, la presentación de los nombres se realiza mediante el uso del alfabeto manual del lenguaje de señas, que vimos en el módulo anterior. Al presentarse, las personas sordas deletrean su nombre letra por letra utilizando cualquiera de sus dos manos. Este método de deletreo permite una comunicación clara y precisa, asegurando que el nombre sea entendido.

Por ejemplo: si una persona se llama "Ana" y quiere presentarse, deletreará  "A-N-A" en lenguaje de señas.
""")

# Imagen
st.image("ejemplodeletreo.png")

st.write("""
A continuación, encontrarás un video muy corto que enseña cómo saludar, decir "mi nombre es" y el ejemplo de cómo deletrear un nombre.
""")

# Video
st.video("deletreonombre.mp4")

# Subtítulo y Texto
st.subheader("¡Ponlo en práctica!")
st.write("""
Escribe tu nombre y luego verás unas imágenes en desorden que corresponden a las señas de cada una de las letras de tu nombre. Con tus conocimientos previos del abecedario, identifica cada seña y elige la letra de tu nombre que le corresponde:
""")

# Input para escribir el nombre
nombre = st.text_input("Escribe solo tu primer nombre (sin tildes)", key="nombre").upper()

# Obtener las letras únicas del nombre ingresado
letras_nombre = set(nombre)

# Arreglo con las letras del abecedario que están contenidas en el nombre ingresado
abecedario = sorted(list(letras_nombre))

# Diccionario para mapear cada letra con su imagen correspondiente
letras_imagenes = {}

# Directorio donde se encuentran las imágenes
directorio = "letras"

# Iterar sobre cada letra y asignarle la imagen correspondiente
for letra in abecedario:
    imagen = f"{letra}.png"
    ruta_imagen = os.path.join(directorio, imagen)
    letras_imagenes[letra] = ruta_imagen

# Mezclar las letras del nombre para mostrarlas en desorden
letras_nombre_desordenadas = list(letras_nombre)
random.shuffle(letras_nombre_desordenadas)

# Mostrar las imágenes y menús desplegables en un formato de cuadrícula
columnas = 3
contador = 0

# Lista para almacenar las opciones seleccionadas por el usuario
opciones_seleccionadas = {}

for letra in letras_nombre_desordenadas:
    if letra in letras_imagenes:
        # Crear una columna para la imagen y el menú desplegable
        col1, col2 = st.columns([1, 4])

        # Mostrar la imagen de la letra
        with col1:
            st.image(letras_imagenes[letra], width=170)

        # Generar un identificador único para el menú desplegable
        identificador_widget = f"selectbox_{letra}"

        # Mostrar el menú desplegable para seleccionar la letra
        with col2:
            opcion_seleccionada = st.selectbox(f"Selecciona la letra de tu nombre que corresponde a la seña", [""] + abecedario, index=0, key=identificador_widget)
            opciones_seleccionadas[letra] = opcion_seleccionada

        contador += 1
        if contador % columnas == 0:
            st.write("")  # Agregar un salto de línea después de cada fila de imágenes

# Verificar si se ha ingresado el nombre y mostrar el botón "Verificar"
if nombre:
    if st.button("Verificar"):
        todas_correctas = True
        for letra in nombre:
            if letra in opciones_seleccionadas:
                opcion_seleccionada = opciones_seleccionadas[letra]
                if opcion_seleccionada == letra:
                    st.success(f"¡Muy bien! Has seleccionado la letra {letra} correctamente.")
                else:
                    st.error(f"Incorrecto. La seña correcta para la letra {letra} es:")
                    st.image(letras_imagenes[letra], width=170)
                    todas_correctas = False
        
        color = "verde" if todas_correctas else "rojo"
        
        client1 = paho.Client("GIT-HUB")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"color": color})
        ret = client1.publish("cmqtt_s", message)

if st.button('ON'):
    act1 = "ON"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
else:
    st.write('')

if st.button('OFF'):
    act1 = "OFF"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_s", message)
else:
    st.write('')

values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

if st.button('Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_a", message)
else:
    st.write('')

# Subtítulo y presentación del deletreo del nombre
st.subheader("Por tanto, el deletreo de tu nombre debe verse así en lengua de señas:")
st.write("Practícalas e intenta presentarte.")

for letra in nombre:
    if letra in letras_imagenes:
        st.write(f"{letra}")
        st.image(letras_imagenes[letra], width=100)

st.subheader("¡Continuemos!")
st.write("Ya puedes dirigirte al siguiente módulo 'Básico: Tu Propia Seña'")
st.markdown("[Siguiente módulo: Básico: Tu Propia Seña](https://aprendelenguajesenascol.streamlit.app/B%C3%A1sico:_tu_propia_se%C3%B1a)", unsafe_allow_html=True)

