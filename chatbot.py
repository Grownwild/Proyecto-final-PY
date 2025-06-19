import streamlit as st
import groq

def crear_cliente_groq():
    
    groq_api_key = st.secrets["GROQ_API_KEY"]
    return groq.Groq(api_key=groq_api_key)



st.set_page_config(page_title="IA CHAD", page_icon="​​🤑​")

MODELOS = ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"]

def configurar_pagina():
    st.title("chatbotMC")

def mostrar_sidebar():
    st.sidebar.title("Lista de Modelos")
    modelo = st.sidebar.selectbox(label="Seleccionado:", options=MODELOS, index=0)
    st.write(f"**MODELO UTILIZADO** : {modelo}")
    return modelo 

##cliente de groq:
def crear_cliente_groq():
    groq_api_key = st.secrets["GROQ_API_KEY"] #api de groq almacenada
    return groq.Groq(api_key=groq_api_key)

    
#ESTADO DE LOS MENSAJES:
def inicializacion_del_estado_chat():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []



# HISTORIAL 
def mostrar_historial_chat():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"]):       
            st.markdown(mensaje["content"])
            
def obtener_mensaje_usuario():
    return st.chat_input("Envia un mensaje")

# AGREGAR MENSAJES AL ESTADO
def agregar_mensaje_al_historial(role, content):
    st.session_state.mensajes.append({"role":role, "content": content})


# VISUALIZAR MENSAJES
def monstrar_mensaje(role, content):
    with st.chat_message(role):
        st.markdown(content)


# COENCTARSE CON EL MODELO GROQ CORRESPONDIENTE
def obtener_respuesta_modelo(cliente, modelo, mensajes):
    respuesta = cliente.chat.completions.create(
        model=modelo,
        messages=mensajes,
        stream = False
    )
    return respuesta.choices[0].message.content



# FLUJO DE APP- (SIEMPRE AL FINAL)
def ejecutar_app():
    configurar_pagina()
    modelo = mostrar_sidebar()
    cliente = crear_cliente_groq()
    inicializacion_del_estado_chat()
    mostrar_historial_chat()
    mensaje_usuario = obtener_mensaje_usuario()
    
    print(mensaje_usuario)

    if mensaje_usuario :
        agregar_mensaje_al_historial("user", mensaje_usuario)
        monstrar_mensaje("user", mensaje_usuario)

        mensaje_modelo = obtener_respuesta_modelo(cliente, modelo, st.session_state.mensajes)
        agregar_mensaje_al_historial("assistant", mensaje_modelo)
        monstrar_mensaje("assistant", mensaje_modelo)

        



if __name__ == "__main__":
    ejecutar_app()

## streamlit run chatbot.py