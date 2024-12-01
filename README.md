# Desarrollo de un Asistente Financiero Inteligente

En este repositorio se pretende desarrollar un Asistente Financiero Inteligente para la Optimización de Decisiones de Inversión en el Mercado de Acciones.

# Abstract

En el contexto actual de los mercados financieros, la cantidad de información disponible para los inversores es abrumadora. La toma de decisiones de inversión eficiente requiere no solo del análisis de datos históricos, sino también de la interpretación del sentimiento del mercado reflejado en noticias, redes sociales y otros medios de comunicación. La inteligencia artificial (IA) y, específicamente, el 
procesamiento del lenguaje natural (PLN), ofrecen herramientas poderosas para abordar este desafío.

El presente proyecto propone el desarrollo de un asistente financiero inteligente que optimice las decisiones de inversión en el mercado de acciones.

# Análisis exploratorio de datos (EDA)

Se analizaron las acciones de AAPL, MSFT, AMZN, GOOGL y META durante 2020-2021. Se observó una tendencia alcista en los precios de cierre ajustado, con una caída notable en marzo de 2020 por la pandemia de COVID-19. Las acciones presentaron alta correlación positiva, lo que es común en empresas del mismo sector o en mercados alcistas generales, esto sugiere que factores macroeconómicos y sentimentales podrían estar afectando a estas acciones de manera similar. Los volúmenes de negociación mostraron variaciones que reflejan eventos específicos del mercado. Este análisis proporciona una base sólida para integrar el análisis de sentimientos y desarrollar modelos predictivos más precisos.

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
