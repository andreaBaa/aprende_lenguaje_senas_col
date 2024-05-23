import paho.mqtt.client as paho
import time
import json
import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

def on_publish(client, userdata, result):  # create function for callback
    print("El dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("LengManos")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker, port)

model_path = "models/keras_model.h5"
model = load_model(model_path)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

labels_path = "models/labels.txt"

with open(labels_path, "r") as file:
    labels = file.read().splitlines()

st.title("¡Aprende lenguaje de señas colombiano!")
st.header("Básico: el abecedario")

st.markdown("""
En esta sección te enseñaremos el abecedario de LSC por medio de un video e imágenes para que luego puedas replicarlo y poder practicar el nuevo conocimiento adquirido.
""")

st.markdown("""
El Lenguaje de Señas Colombiano (LSC) está conformado por varios elementos y características que lo hacen un sistema de comunicación completo y estructurado. La configuración de la mano (Quirémica) se refiere a las formas que adoptan las manos al realizar diferentes señas. Existen configuraciones básicas que se utilizan como base para formar las señas, y cada una tiene su propia estructura y posición de los dedos. La orientación puede variar hacia adelante, hacia atrás, hacia arriba, hacia abajo, hacia los lados, etc. Los movimientos pueden ser lineales, circulares, repetitivos, y pueden variar en velocidad e intensidad.
""")

st.image("images/1.png", width=500)
st.image("images/2.png", width=500)
st.image("images/3.png", width=500)
st.video("https://www.youtube.com/watch?v=SKeBZpjWTko")

st.subheader("¡Ponlo en práctica!")
st.markdown("""
Antes de empezar, asegúrate de que Streamlit tenga acceso a tu cámara. Te daremos algunas letras para que practiques la posición de la mano. Identifica la letra que estamos pidiendo y posiciona tu mano a 15 cm de la cámara. Por favor, asegúrate de que solo se muestre tu mano, preferiblemente con un fondo blanco (puedes posicionar tu mano enfrente de una pared o de un pedazo de papel). Cuando estés listo, haz clic en “Tomar foto” y espera a tu resultado. Si hiciste la seña correctamente, se encenderá un LED de color verde y se escuchará un sonido indicando que lo has logrado. Si lo has hecho de forma incorrecta, el LED que se encenderá será el rojo.
""")

st.session_state["letter"] = st.selectbox('Elige una letra para practicar:', labels)

run = st.checkbox('Usar cámara')
FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

if run:
    while True:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

        # Create a button to take a picture
        if st.button('Tomar foto'):
            if ret:
                # Save the frame as an image
                img = Image.fromarray(frame)
                size = (224, 224)
                image = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
                data[0] = normalized_image_array

                prediction = model.predict(data)
                index = np.argmax(prediction)
                class_name = labels[index]
                confidence_score = prediction[0][index]

                st.write(f"Letra detectada: {class_name}")
                st.write(f"Confianza: {confidence_score * 100:.2f}%")

                if class_name == st.session_state["letter"]:
                    client1.publish("IMIA", json.dumps({"Act1": "verde"}))
                    st.write("¡Correcto!")
                else:
                    client1.publish("IMIA", json.dumps({"Act1": "rojo"}))
                    st.write("Intenta de nuevo")

cap.release()

