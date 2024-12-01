# Desarrollo de un Asistente Financiero Inteligente

![DALL·E 2024-12-01 02 02 40 - A modern, professional LinkedIn post illustration for a financial AI project  The central focus is a futuristic financial assistant hologram analyzing](https://github.com/user-attachments/assets/9e2e2983-7ac6-4e68-aef5-faefe051603d)

En este repositorio se pretende desarrollar un Asistente Financiero Inteligente para la Optimización de Decisiones de Inversión en el Mercado de Acciones.

# Abstract

En el contexto actual de los mercados financieros, la cantidad de información disponible para los inversores es abrumadora. La toma de decisiones de inversión eficiente requiere no solo del análisis de datos históricos, sino también de la interpretación del sentimiento del mercado reflejado en noticias, redes sociales y otros medios de comunicación. La inteligencia artificial (IA) y, específicamente, el 
procesamiento del lenguaje natural (PLN), ofrecen herramientas poderosas para abordar este desafío.

El presente proyecto propone el desarrollo de un asistente financiero inteligente que optimice las decisiones de inversión en el mercado de acciones.

# Análisis exploratorio de datos (EDA)

Se analizaron las acciones de AAPL, MSFT, AMZN, GOOGL y META durante 2020-2021. Se observó una tendencia alcista en los precios de cierre ajustado, con una caída notable en marzo de 2020 por la pandemia de COVID-19. Las acciones presentaron alta correlación positiva, lo que es común en empresas del mismo sector o en mercados alcistas generales, esto sugiere que factores macroeconómicos y sentimentales podrían estar afectando a estas acciones de manera similar. Los volúmenes de negociación mostraron variaciones que reflejan eventos específicos del mercado. Este análisis proporciona una base sólida para integrar el análisis de sentimientos y desarrollar modelos predictivos más precisos.

# Web Scraping y Análisis de Sentimientos
**Extracción de Datos**  
Se realizó web scraping de noticias financieras a través de Finviz, enfocándonos en las cinco principales empresas tecnológicas (AAPL, MSFT, AMZN, GOOGL y META). La extracción incluye:

- Fecha de publicación
- Ticker de la empresa
- Título de la noticia
- Fuente original de la noticia
- URL de la noticia

**Análisis de Sentimientos**  

Se desarrolló un analizador avanzado de texto que procesa las noticias extraídas utilizando:  

- `TextBlob` para análisis de sentimiento
- `SpaCy` para procesamiento de lenguaje natural
- `Altair` para visualizaciones interactivas

**Características principales del análisis:**  

- Cálculo de polaridad del sentimiento para cada noticia
- Extracción de entidades nombradas
- Generación de métricas por empresa
- Visualizaciones de tendencias temporales

**Visualizaciones Generadas**  

El análisis produce tres visualizaciones principales:  

- Tendencias de sentimiento por empresa a lo largo del tiempo
- Distribución del sentimiento para cada compañía
- Frecuencia de palabras clave en los títulos


<div style="text-align: justify; text-justify: inter-word; margin-right: 0; padding-right: 0; max-width: 100%;">
El análisis integrado de las noticias tecnológicas revela patrones significativos en la narrativa del sector. La inteligencia artificial emerge como un tema dominante, reflejándose no solo en la frecuencia de menciones sino también en el tono generalmente positivo de las noticias relacionadas. Esta tendencia subraya la creciente importancia de la IA en la dirección estratégica de las principales empresas tecnológicas. La variabilidad en el sentimiento de las noticias se alinea estrechamente con la diversidad de temas cubiertos, desde avances tecnológicos hasta desafíos regulatorios, creando un panorama informativo dinámico y multifacético.
Cada empresa mantiene una huella distintiva en términos de cobertura mediática y sentimiento asociado, lo que refleja sus diferentes posicionamientos en el mercado y estrategias corporativas. La presencia constante de terminología financiera en las noticias destaca la estrecha relación entre el desarrollo tecnológico y el desempeño en el mercado de valores. Este enfoque dual en innovación y rendimiento financiero caracteriza la narrativa actual del sector tecnológico.
Las implicaciones para el sector son sustanciales: la IA se ha convertido en el eje central de la narrativa tecnológica, mientras que el análisis financiero mantiene una influencia significativa en la percepción pública de estas empresas. Aunque se observa una volatilidad considerable en la percepción de las compañías, la tendencia general se mantiene positiva, sugiriendo una confianza subyacente en el sector tecnológico a pesar de las fluctuaciones a corto plazo. Este panorama refleja la madurez del sector y su capacidad para mantener el optimismo del mercado incluso en un entorno informativo altamente dinámico.
</div>


## Aspectos Cubiertos del Proyecto

- Análisis de texto avanzado con `spaCy/NLTK`
- Visualizaciones interactivas con `Altair`
- Análisis de sentimiento
- Procesamiento de datos estructurados
- Extracción de entidades y relaciones
- Análisis estadístico y tendencias


# 2do Web Scraping y Análisis de Sentimientos

En el notebook "AFI.ipynb", a partir del punto 6, se realiza otro web scraping y análisis de sentimientos con las siguientes características:

1. **Descarga de Noticias Financieras:**
   - **Fuente:** Utilización de la API de NewsAPI para recopilar hasta 19 artículos diarios por empresa en un periodo de 7 días.
   - **Proceso:** Implementación de web scraping inicial fallida en Yahoo Finance, seguida del uso exitoso de NewsAPI para asegurar la extracción de noticias relevantes.
   - **Limpieza de Datos:** Eliminación de títulos inválidos, vacíos y duplicados, y conversión de fechas al formato adecuado.

2. **Análisis de Sentimientos:**
   - **Preprocesamiento de Texto:** Tokenización, eliminación de stopwords, limpieza de puntuación y normalización de texto.
   - **Extensión del Léxico de VADER:** Incorporación de términos específicos del dominio financiero como `bullish`, `bearish`, `profit` y `loss` para mejorar la precisión del análisis.
   - **Clasificación de Sentimientos:** Uso de VADER para categorizar los títulos de las noticias en **Positivo**, **Neutral** o **Negativo**.
   - **Resultados:** Distribución de sentimientos con un 40% positivo, 35% neutral y 25% negativo, destacando tendencias positivas en Microsoft y Amazon, y negativas en Google.

3. **Más adelante se continuará desarrollando los siguientes puntos:**
   - **Correlación de Sentimientos con Rendimiento de Acciones**
   - **Construcción de un Modelo Predictivo**
   - **Desarrollo de una Plataforma para Usuarios**

## Flujo de Trabajo
- Análisis EDA
- Análisis de sentimientos
  - Extracción de noticias mediante web scraping

## Dónde encontrar información detallada de este proyecto
* Los resultados detallados de este análisis se pueden encontrar en la carpeta resultados.  
* Para más detalles sobre la implementación y resultados específicos, consulte los notebooks correspondientes en la carpeta src.

## Colaboración en el proyecto  
Este proyecto forma parte de la Maestría en Ciencias de los Datos de la Universidad de Guadalajara y constituye el proyecto final de la asignatura Desarrollo de Proyecto I impartida por el Mtro. Cuspinera Contreras.  
Se desarrolló el proyecto titulado "Asistente Financiero Inteligente", el cual está siendo elaborado por Fernando Arévalo como tema de tesis. Asimismo, contó con la valiosa colaboración de Carmen Herrera, quien realizó importantes aportes en el análisis.

# Estructura de repositorio

La estructura que tiene nuestro repositorio es la siguiente:
    
    ├── data                            <- Carpeta de bases de datos.  
    |    |── README.md                  <- Descripción general del contenido de la carpeta.
    |    └── datos_acciones.csv         <- Base de datos.  
    |    └── tech_news.csv              <- Base de datos para análisis de texto y sentimientos.  
    |      
    ├── doc                             <- Carpeta de archivos de texto.
    |    └──  README.md                 <- Descripción de Problematica, Objetivo y Justificación del proyecto.
    |
    ├── results                         <- Carpeta de resultados.  
    |    └──  README.md                 <- Descripción de los resultados del análisis EDA, análisis de texto y de sentimientos.
    |  
    ├── src                             <- Carpeta de archivos de código.    
    |    |── AFI.ipynb                  <- Archivo notebook de código (Análisis EDA, Web scraping).
    |    |── sentiment_analysis.py      <- Archivo de código para análisis de sentimiento y visualización de noticias de empresas/acciones tecnológicas.
    |    └── README.md                  <- Descripción general del contenido del notebook.
    |  
    ├── CITATION.md                     <- Información sobre como citar este trabajo.  
    |  
    ├── CONTRIBUTING.md                 <- Información para contribuir en este trabajo.  
    |   
    ├── LICENSE                         <- Información sobre la Licencia: MIT License.  
    |  
    ├── README.md                       <- Información general del proyecto.
