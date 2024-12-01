# Desarrollo de un Asistente Financiero Inteligente

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

- TextBlob para análisis de sentimiento
- SpaCy para procesamiento de lenguaje natural
- Altair para visualizaciones interactivas

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


<div style="text-align: justify">El análisis integrado de las noticias tecnológicas revela patrones significativos en la narrativa del sector. La inteligencia artificial emerge como un tema dominante, reflejándose no solo en la frecuencia de menciones sino también en el tono generalmente positivo de las noticias relacionadas. Esta tendencia subraya la creciente importancia de la IA en la dirección estratégica de las principales empresas tecnológicas. La variabilidad en el sentimiento de las noticias se alinea estrechamente con la diversidad de temas cubiertos, desde avances tecnológicos hasta desafíos regulatorios, creando un panorama informativo dinámico y multifacético.
Cada empresa mantiene una huella distintiva en términos de cobertura mediática y sentimiento asociado, lo que refleja sus diferentes posicionamientos en el mercado y estrategias corporativas. La presencia constante de terminología financiera en las noticias destaca la estrecha relación entre el desarrollo tecnológico y el desempeño en el mercado de valores. Este enfoque dual en innovación y rendimiento financiero caracteriza la narrativa actual del sector tecnológico.
Las implicaciones para el sector son sustanciales: la IA se ha convertido en el eje central de la narrativa tecnológica, mientras que el análisis financiero mantiene una influencia significativa en la percepción pública de estas empresas. Aunque se observa una volatilidad considerable en la percepción de las compañías, la tendencia general se mantiene positiva, sugiriendo una confianza subyacente en el sector tecnológico a pesar de las fluctuaciones a corto plazo. Este panorama refleja la madurez del sector y su capacidad para mantener el optimismo del mercado incluso en un entorno informativo altamente dinámico.</div>

Los resultados detallados de este análisis se pueden encontrar en la carpeta resultados.  

## Aspectos Cubiertos del Proyecto

- Análisis de texto avanzado con spaCy/NLTK
- Visualizaciones interactivas con Altair
- Análisis de sentimiento
- Procesamiento de datos estructurados
- Extracción de entidades y relaciones
- Análisis estadístico y tendencias

**Flujo de Trabajo**

- Análisis EDA
- Extracción de noticias mediante web scraping
- Preprocesamiento de textos
- Análisis de sentimiento
- Generación de visualizaciones
- Documentación de resultados

Para más detalles sobre la implementación y resultados específicos, consulte los notebooks correspondientes en la carpeta



# Estructura de repositorio

El objetivo de este repositorio es implementar las buenas prácticas de acuerdo al paper ["Good Enough Practices in Scientific Computing"](https://arxiv.org/abs/1609.00037) por Greg Wilson, Jennifer Bryan, Karen Cranston, Justin Kitzes, Lex Nederbragt, Tracy K. Teal.

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
