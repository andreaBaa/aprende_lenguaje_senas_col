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

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("¡Aprende lenguaje de señas colombiano!")
st.header("Básico: el abecedario")


st.markdown("""
En esta sección te enseñaremos el abecedario de LSC por medio de un video e imágenes para que luego puedas replicarlo y poder practicar el nuevo conocimiento adquirido.
""")


st.markdown("""
El Lenguaje de Señas Colombiano (LSC) está conformado por varios elementos y características que lo hacen un sistema de comunicación completo y estructurado. La configuración de la mano (Quirémica) se refiere a las formas que adoptan las manos al realizar diferentes señas. Existen configuraciones básicas que se utilizan como base para formar las señas, y cada una tiene su propia estructura y posición de los dedos. La orientación puede variar hacia adelante, hacia atrás, hacia arriba, hacia abajo, hacia los lados, etc. Los movimientos pueden ser lineales, circulares, repetitivos, y pueden variar en velocidad e intensidad.
""")

st.image("1.png", width = 500)
st.image("2.png", width = 500)
st.image("3.png", width = 500)
st.video("https://www.youtube.com/watch?v=SKeBZpjWTko")

st.subheader("¡Ponlo en práctica!")
st.markdown("""
Antes de empezar, asegúrate de que Streamlit tenga acceso a tu cámara. Te daremos algunas letras para que practiques la posición de la mano. Identifica la letra que estamos pidiendo y posiciona tu mano a 15 cm de la cámara. Por favor, asegúrate de que solo se muestre tu mano, preferiblemente con un fondo blanco (puedes posicionar tu mano enfrente de una pared o de un pedazo de papel). Cuando estés listo, haz clic en “Tomar foto” y espera a tu resultado. Si hiciste la seña correctamente, se encenderá un LED de color verde y se escuchará un sonido indicando que lo has logrado. Si lo has hecho de manera incorrecta, aparecerá en pantalla la palabra “Incorrecto”. Puedes tomar la foto cuantas veces quieras y practicar múltiples veces.
""")

st.title("A")

camera_input_key = f"camera_input_A"
img_file_buffer = st.camera_input(f"Toma una Foto de A", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0] > 0.4:
        st.header("A")
        st.image("A.png", width = 500)
        payload = json.dumps({'abc': 'A'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("A.png", width = 500)

st.title("B")
camera_input_key = f"camera_input_B"
img_file_buffer = st.camera_input(f"Toma una Foto de B", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][1] > 0.4:
        st.header("B")
        st.image("B.png")
        payload = json.dumps({'abc': 'B'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("B.png")

st.title("C")
camera_input_key = f"camera_input_C"
img_file_buffer = st.camera_input(f"Toma una Foto de C", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][2] > 0.4:
        st.header("C")
        st.image("C.png", width = 500)
        payload = json.dumps({'abc': 'C'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("C.png", width = 500)

st.title("D")
camera_input_key = f"camera_input_D"
img_file_buffer = st.camera_input(f"Toma una Foto de D", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][3] > 0.4:
        st.header("D")
        st.image("D.png", width = 500)
        payload = json.dumps({'abc': 'D'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("D.png", width = 500)

st.title("I")
camera_input_key = f"camera_input_I"
img_file_buffer = st.camera_input(f"Toma una Foto de I", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][4] > 0.3:
        st.header("I")
        st.image("I.png", width = 500)
        payload = json.dumps({'abc': 'I'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("I.png", width = 500)

st.title("K")
camera_input_key = f"camera_input_K"
img_file_buffer = st.camera_input(f"Toma una Foto de K", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][5] > 0.4:
        st.header("K")
        st.image("K.png", width = 500)
        payload = json.dumps({'abc': 'K'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("K.png", width = 500)

st.title("L")
camera_input_key = f"camera_input_L"
img_file_buffer = st.camera_input(f"Toma una Foto de L", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][6] > 0.4:
        st.header("L")
        st.image("L.png", width = 500)
        payload = json.dumps({'abc': 'L'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("L.png", width = 500)

st.title("N")
camera_input_key = f"camera_input_N"
img_file_buffer = st.camera_input(f"Toma una Foto de N", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][7] > 0.3:
        st.header("N")
        st.image("N.png", width = 500)
        payload = json.dumps({'abc': 'N'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("N.png", width = 500)

st.title("O")
camera_input_key = f"camera_input_O"
img_file_buffer = st.camera_input(f"Toma una Foto de O", key=camera_input_key)

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][8] > 0.4:
        st.header("O")
        st.image("O.png", width = 500)
        payload = json.dumps({'abc': 'O'})
        client1.publish("LengSenas", payload, qos=0, retain=False)
        time.sleep(0.2)
    else:
        st.text("Incorrecto")
        st.image("O.png", width = 500)




   #if prediction[0][0]>0.3:
      #st.header('R')
      #client1.publish("LengSenas","{'abc': 'R'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('U')
      #client1.publish("LengSenas","{'abc': 'U'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('V')
      #client1.publish("LengSenas","{'abc': 'V'}",qos=0, retain=False)
      #time.sleep(0.2)
   #if prediction[0][0]>0.3:
      #st.header('Y')
      #client1.publish("LengSenas","{'abc': 'Y'}",qos=0, retain=False)
      #time.sleep(0.2)
