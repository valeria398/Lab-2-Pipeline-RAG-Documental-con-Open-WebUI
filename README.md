# Reinicar contenmedor corrupto

Si open erb ui da probema intena cambiar la version a v0.5.20 en el compose y sigue los siguientes pasos

1. Detener y eliminar solo el contenedor dañado:

'''
docker rm -f open-webui-lab
'''

2. Eliminar la imagen corrupta de Open WebUI:

'''
docker rmi ghcr.io/open-webui/open-webui:main
'''

3. Volver a descargar la imagen limpia y levantar el servicio:

'''
docker compose pull open-webui
docker compose up -d
'''
4. Revisar logs del contenedor 

'''
docker logs -f open-webui-lab
'''

5. Verificación
Espera unos segundos y comprueba con docker ps que open-webui-lab ya no diga Restarting, sino Up ... (health: starting) o Up ..., y luego revisa nuevamente con docker logs -f open-webui-lab hasta ver que arranque Uvicorn.

# Solucion omitiendo imagen docker de open web ui
Si esto no lo soluciona puedes usar un entorno directo en python de la siguiente forma:

# 1. Elimina el contenedor problemático de Open WebUI
docker rm -f open-webui-lab

# 2. Crea un entorno virtual limpio en tu carpeta de laboratorio
python3 -m venv .venv-webui
source .venv-webui/bin/activate

# 3. Instala la versión estable de Open WebUI
pip install open-webui

# 4. Inícialo apuntando a tu Ollama en localhost:11434
OLLAMA_BASE_URL=http://localhost:11434 open-webui serve --port 3000