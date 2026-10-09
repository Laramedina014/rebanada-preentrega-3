# Optimización de Campañas de Marketing mediante Segmentación de Clientes


## 1. Problema de Negocio
Las campañas de marketing masivas e indiferenciadas generan un elevado costo por contacto y una baja tasa de conversión al dirigirse a audiencias con baja probabilidad de respuesta.
Este proyecto analiza el comportamiento de compra y variables demográficas de 2.240 clientes con el objetivo de identificar qué perfiles responden con mayor frecuencia, permitiendo reasignar el presupuesto publicitario hacia los segmentos de mayor retorno.


## 2. Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Procesamiento y Análisis de Datos:** Pandas, NumPy
* **Visualización de Datos:** Matplotlib, Seaborn
* **Control de Versiones y Documentación:** Git, GitHub, Markdown


## 3. Metodología
El proyecto sigue el marco de trabajo **CRISP-DM** estructurado en iteraciones cortas:
* **Comprensión del Negocio (Business Understanding):** Definición de la Question Story y métricas clave de conversión (tasa de aceptación y gasto promedio por categoría).
* **Comprensión y Preparación de los Datos (Data Understanding & Preparation):** Exploración del dataset *Customer Personality Analysis* (2.240 registros, 29 variables), tratamiento de los 24 valores nulos en `Income` y selección de variables clave bajo el criterio **JBGE** (*Just Barely Good Enough*).
* **Modelado y Análisis (Modeling/Analysis):** Agrupación comparativa según la variable objetivo `Response` y segmentación por categorías de consumo clave (`MntWines`, `MntMeatProducts`).
* **Evaluación (Evaluation):** Análisis del diferencial de gasto e ingresos para formular recomendaciones concretas de reasignación presupuestaria.


## 4. Hallazgos Clave
* **Efecto Ingreso:** Los clientes que aceptaron la campaña registran un ingreso promedio un 38% superior frente a quienes la rechazaron ($69.194 vs. $50.088).
* **Categorías Predictivas:** El gasto promedio en vinos es más del doble ($502 vs. 198)yencarnescasieltriple(276 vs. $98) en el grupo que respondió positivamente.
* **Eficiencia de Pauta:** Focalizar la inversión en audiencias con perfil de consumo en vinos y carnes permite excluir contactos de baja probabilidad de compra sin comprometer el volumen total de conversiones.


## 5. Estructura del Repositorio
├── marketing_campaign.csv      # Dataset fuente de Kaggle (Customer Personality Analysis)
├── rebanada_marketing.py       # Script principal en Python
├── requirements.txt            # Dependencias del proyecto
├── resultado_rebanada.png      # Gráfico comparativo generado por el script
└── README.md                   # Documentación técnica del repositorio


## 6. Cómo Ejecutar el Proyecto
1. Clonar el repositorio:
   git clone https://github.com/Laramedina014/rebanada-preentrega-3.git
   cd marketing-campaign-analysis


2. Instalar las dependencias requeridas:
   pip install -r requirements.txt


3. Ejecutar el script principal:
   python rebanada_marketing.py
