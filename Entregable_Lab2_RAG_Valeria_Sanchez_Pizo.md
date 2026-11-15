# Informe de Laboratorio 2: Pipeline RAG con Open WebUI y Ollama

- **Estudiante / Equipo:** Valeria Sanchez Pizo
- **Stack Utilizado:** qwen2.5:1.5b-instruct + nomic-embed-text + Open WebUI + Docker Compose
- **Fecha:** 15/11/2026

---

## 1. Comparativa: Antes del RAG (Línea Base)
Sin acceso a la base de conocimiento, qwen2.5:1.5b-instruct no pudo responder con los datos privados de Innovatech y alucinó en todas las pruebas. Ante la consulta del auxilio de conectividad, estimó un valor de “$350 a $450” (en otro intento, “500.000 pesos”), cuando el real es $245.000 COP, e inventó el código “INV102” en lugar de #INV-CON-2027. Sobre RRHH, mencionó a un “gerente de RRH informático” y no a la directora Laura Martínez, y no dio el límite de 7 días hábiles. En la consulta sobre la fuga en AWS entregó una respuesta genérica, sin el plazo de 2 horas, el canal #sec-incidentes-urgente ni la extensión 809, que degeneró en un bucle repetitivo de referencias a NIST. En un intento incluso afirmó que “Innovatech Colombia” no existe como entidad. En conjunto, el modelo rellenó el vacío con respuestas plausibles pero falsas, en lugar de reconocer que no tenía la información.

## 2. Comparativa: Después del RAG (Con Knowledge Base)
Tras indexar politica_innovatech_2027.txt en la colección Politicas-Innovatech-2027 (embeddings con nomic-embed-text vía Ollama) y conectarla al modelo qwen-innovatech, la precisión pasó de respuestas inventadas a respuestas fieles al documento. El modelo respondió correctamente $245.000 COP y el código #INV-CON-2027; indicó el máximo de 7 días hábiles de vacaciones anticipadas para quien lleva entre 6 meses y 1 año, con aprobación del líder de proyecto y de RRHH, gestionado por la directora Laura Martínez; y, ante la fuga en AWS, reportó el plazo menor a 2 horas, el canal de Slack #sec-incidentes-urgente (o la extensión 809) y el cifrado AES-256 con rotación trimestral de llaves. En las tres respuestas Open WebUI mostró “1 Fuente”, el fragmento de la política recuperado de la colección, lo que permite verificar de dónde sale cada dato (trazabilidad). Las respuestas se apoyaron en el contexto recuperado y no en el conocimiento general del modelo.

## 3. Evaluación de Control de Alucinaciones (Fuera de Dominio)
Ante la pregunta sobre el horario de la cafetería los sábados, un dato que no existe en el documento, el modelo no inventó ningún horario, que era el riesgo principal. Respondió que no podía proporcionar esa información y recomendó consultar la página web oficial de Innovatech o contactar a la empresa. El comportamiento fue correcto en lo esencial, pero no ideal: en lugar de indicar que “el documento no contiene información sobre la cafetería”, atribuyó la falta de datos a que no tiene acceso a la información específica de la empresa. Open WebUI también mostró “1 Fuente”, porque la búsqueda vectorial siempre devuelve el fragmento más cercano aunque no sea relevante. Esto muestra que el RAG reduce la alucinación pero no la elimina por sí solo; el prompt de sistema, la temperatura baja y el tamaño del modelo influyen en que sepa decir “no está en el documento”.

---

## 4. Evidencias Adjuntas (Capturas de Pantalla)
- [ ] Captura 1: Respuesta del modelo sin RAG (alucinación / desconocimiento).
- [ ] Captura 2: Documento `politica_innovatech_2027.txt` indexado en *Workspace -> Knowledge*.
- [ ] Captura 3: Respuesta fundamentada usando `#Politicas-Innovatech-2027` con citas desplegadas.
