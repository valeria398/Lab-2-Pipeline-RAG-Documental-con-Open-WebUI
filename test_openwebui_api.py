import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")

# ==============================================================================
# 1. CONFIGURACIÓN DE CONEXIÓN A OPEN WEBUI
# ==============================================================================
# Docker publica el contenedor como host:3000 -> contenedor:8080.
# La ruta compatible con OpenAI en Open WebUI termina en "/api".
OPENWEBUI_BASE_URL = "http://localhost:3000/api"

# API Key de Open WebUI (Settings -> Account -> API Keys).
# Se lee de la variable de entorno o del archivo .env junto a este script.
OPENWEBUI_API_KEY = os.getenv("OPENWEBUI_API_KEY", "")

# Inicializamos el cliente oficial de OpenAI apuntando a nuestro entorno local
client = OpenAI(
    base_url="http://localhost:3000/api",
    api_key="sk-74d81f4d894b47afb696d82c56f1c46d",
)

# ==============================================================================
# 2. SELECCIÓN DEL MODELO (BASE VS. PERSONALIZADO CON RAG)
# ==============================================================================
# Para probar el modelo base del Lab 2:
MODELO_A_USAR = "modelo-fitness-colombiano"
# MODELO_A_USAR = "usar ID del modelo creado en open webui"
# ------------------------------------------------------------------------------
# NOTA PARA USAR UN MODELO PERSONALIZADO (CON RAG / KNOWLEDGE BASE INTEGRADO):
# Si creaste un modelo personalizado en "Workspace -> Models", solo debes
# cambiar la variable MODELO_A_USAR por el ID exacto de ese modelo.
#
# Ejemplo:
# MODELO_A_USAR = "mi-modelo-personalizado"
#
# Consideraciones obligatorias antes de llamarlo por API:
#   1. El modelo personalizado debe tener visibilidad "Public" (o compartida con
#      el usuario dueño de la API Key).
#   2. La Base de Conocimiento (Knowledge) vinculada a ese modelo TAMBIÉN debe
#      tener visibilidad "Public"; de lo contrario, el RAG no recuperará contexto.
#   3. Si la API Key pertenece a un usuario normal (no admin), el administrador
#      debe haber habilitado el permiso "Allow API Key Creation" en su rol.
#   4. No necesitas enviar "#" ni archivos adjuntos en el mensaje: Open WebUI
#      ejecutará automáticamente la búsqueda vectorial en segundo plano.
# ------------------------------------------------------------------------------


def consultar_modelo(prompt_usuario: str) -> None:
    if not OPENWEBUI_API_KEY:
        print(
            "Falta OPENWEBUI_API_KEY. Ponla en el archivo .env "
            "(junto a este script) o expórtala en la terminal."
        )
        return

    print(f"Conectando a {OPENWEBUI_BASE_URL} | Modelo: {MODELO_A_USAR}...\n")
    try:
        response = client.chat.completions.create(
            model=MODELO_A_USAR,
            messages=[
                {
                    "role": "user",
                    "content": prompt_usuario,
                }
            ],
            temperature=0.3,  # Temperatura baja para respuestas más precisas y deterministas
        )

        respuesta_texto = response.choices[0].message.content
        print("--- Respuesta del Modelo ---")
        print(respuesta_texto)

    except Exception as e:
        print(f"Error al conectar con Open WebUI: {e}")


if __name__ == "__main__":
    # Prompt de prueba inicial
    pregunta = "Hola, preséntate brevemente y dime qué tipo de asistencia puedes brindarme."
    consultar_modelo(pregunta)