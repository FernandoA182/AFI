# Carpeta con archivos de código

Archivo adjunto "AFI.ipynb"  
Es el notebook que contiene los pasos de la descarga y guadado de datos, así tambien como El análisis EDA considerando los siguientes puntos:
* Descripción de los datos
* Limpieza de datos
* Missing values
* Visualización de datos
* Referencias

Adicional, en la parte final del notebook se agregó el código para realizar web scraping de fuentes de noticias sobre las mepresas que estamos analizando. 


Archivo "sentiment_analysis.py"
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
