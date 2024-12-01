# Carpeta con archivos de código

#### Archivo adjunto "AFI.ipynb"  
Es el notebook que contiene los pasos de la descarga y guadado de datos, así tambien como el análisis EDA considerando los siguientes puntos:
* Descripción de los datos
* Limpieza de datos
* Valores faltantes
* Visualización de datos
* Referencias

Adicional, se realizó la parte final de este proyecto (Continuación del Proyecto).  

En el punto 5 del notebook "AFI.ipynb" se agregó el código para realizar web scraping de fuentes de noticias sobre las empresas que estamos analizando. 

#### Archivo adjunto "sentiment_analysis.py"
Este script realiza un análisis avanzado de sentimiento sobre noticias financieras de empresas tecnológicas. Utiliza técnicas de procesamiento de lenguaje natural (NLP) y visualización de datos para extraer insights significativos de los títulos de las noticias.

### Funcionalidades Principales
**Preprocesamiento de Texto**

- Tokenización de texto
- Eliminación de stopwords
- Limpieza de puntuación y números
- Normalización de texto

**Análisis de Sentimiento** 

- Cálculo de polaridad del sentimiento usando TextBlob
- Análisis por empresa
- Tendencias temporales de sentimiento
- Distribución de sentimientos

**Análisis de Entidades**

- Extracción de entidades nombradas usando spaCy
- Frecuencia de menciones por empresa
- Identificación de entidades relevantes

**Visualizaciones Interactivas**  

- Tendencias de sentimiento por empresa
- Distribución de sentimiento por empresa
- Gráfico de frecuencia de palabras comunes

**Dependencias**

- pandas
- numpy
- spacy
- altair
- textblob
- nltk

📄 **Resultados**  
El script genera:    

📊 Visualizaciones interactivas en formato HTML  
📝 Resumen estadístico por empresa  
📈 Análisis de tendencias  
🔍 Identificación de patrones en las noticias  

📂 Archivos Generados  

sentiment_trend_interactive.html  
sentiment_dist_interactive.html  
word_frequency_interactive.html  

Este análisis proporciona insights valiosos sobre la percepción de las empresas tecnológicas en las noticias y ayuda a identificar patrones y tendencias en la cobertura mediática.

#### Dentro del notebok "AFI.ipynb" también, a partir del punto 6 se realizó otro web scraping y análisis de sentimientos. Esto, para complementar este proyecto y, en conjunto con el análisis previamente mencionado en "sentiment_analysis.py", cumple cabalmente con los requisitos del proyecto final de la asignatura de Desarrollo de Proyecto I, así como permite avanzar y establecer las bases para continuar desarrollando este proyecto de tesis.

Donde se consideraron los siguientes puntos:
* 6.1 Recolección de Datos Textuales
* 6.2. Pasos para la Limpieza y Preprocesamiento de Datos
* 6.3. Análisis de Sentimientos con OpenAI (A desarrollar)
* 6.4. Análisis de Sentimientos con VADER
* 7. Integración de Datos de Sentimiento con Datos Financieros (A desarrollar)
* 7.1. Calcular el Sentimiento Promedio Diario por Empresa
* 7.2. Obtención de Datos Históricos de Precios de Acciones
* 7.3. Creación de la Columna 'Price Change'
* Próximos Pasos:
* Análisis de Correlación y Visualización de Datos
* Desarrollo de un Modelo Predictivo para Predecir Retornos de Acciones Basado en Sentimientos
* Implementación de Métodos Estadísticos Avanzados para Validar Resultados

