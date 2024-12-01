# Resultados del análisis EDA

## Conclusiones y Observaciones 🔍
📝Descripción de los Datos:
  * El conjunto de datos contiene información diaria de precios y volúmenes de las 5 acciones más capitalizadas entre 2020 y 2021.
  * Los atributos principales son: 'Open', 'High', 'Low', 'Close', 'Adj Close' y 'Volume'.  
🧹 Limpieza de Datos y Valores Faltantes:  
  * Se eliminaron filas con valores faltantes en la columna 'Value' para asegurar la integridad del análisis.
  * No se encontraron duplicados después de la limpieza inicial.
 📈Visualizaciones:
  * Las gráficas de precios de cierre ajustado muestran tendencias generales de crecimiento en las acciones tecnológicas durante el período analizado.
  * Los volúmenes de negociación presentan variaciones que podrían relacionarse con eventos específicos del mercado.
  * Los retornos diarios permiten observar la volatilidad y posibles correlaciones en los movimientos de las acciones.
 🔗Análisis de Correlación:
  * Las acciones analizadas presentan altas correlaciones entre sí, lo que es común en empresas del mismo sector o en mercados alcistas generales.
  * Esto sugiere que factores macroeconómicos y sentimentales podrían estar afectando a estas acciones de manera similar.

## Notas Finales sobre el análisis EDA📝
Este EDA nos brinda una comprensión inicial de los datos históricos de las acciones más capitalizadas. Nos prepara para etapas posteriores del proyecto donde integraremos análisis más complejos para mejorar la toma de decisiones de inversión.


# Resultados del análisis de texto y sentimientos  

## Análisis de Frecuencia de Palabras 📝  
![Palabras más comunes en Títulos](https://github.com/user-attachments/assets/6ca0f704-31bb-47bf-9310-ae8427b2d69f)

🔑 **Hallazgos Clave**  
🤖 "AI" domina la frecuencia de palabras  
📱 "Meta" y "Motley Fool" aparecen con alta frecuencia, indicando cobertura significativa  
💰 Palabras financieras como "stock" e "insider" tienen presencia notable  
🏢 Las principales empresas (apple, microsoft, google, amazon) muestran frecuencias equilibradas  
🎮 "nvidia" aparece frecuentemente, sugiriendo su importancia en el ecosistema tecnológico  


## Tendencias de sentimiento 📈  
![Tendencias de Sentimiento por Empresa](https://github.com/user-attachments/assets/413b24ad-70f5-4850-a848-f52fa01b8c8c)

📊Alta volatilidad el 29 de noviembre para todas las empresas  

**Patrones de sentimiento:**  
📱 META muestra la tendencia más estable pero generalmente más baja  
🛒 AMZN exhibe los picos más altos de sentimiento positivo  
🍎 AAPL y MSFT muestran patrones similares de volatilidad  
🔍 GOOGL mantiene una tendencia moderada  
📅 El período del 21 al 28 de noviembre muestra movimientos más suaves.  


## Distribución de Sentimiento 📊   
![Distribución de Sentimiento por Empresa](https://github.com/user-attachments/assets/70857b9f-51a8-415d-b619-bedb26a51d65)


📈Todas las empresas muestran una distribución centrada en valores positivos  

**Características por empresa:**  

🛒 AMZN: Mayor mediana y dispersión hacia valores positivos  
🍎 AAPL: Distribución simétrica con valores atípicos positivos  
💻 MSFT: Distribución similar a AAPL pero más compacta  
🔍 GOOGL: Menor dispersión, sentimiento más consistente  
📱 META: Distribución más baja pero con valores atípicos en ambas direcciones



# Resultados del análisis de sentimientos (A partir del punto 6 en el notebook "AFI.ipynb")

## 1. Descarga de Información con NewsAPI ⬇️

### 1.1. Recolección de Noticias Financieras 📰

- **Empresas Analizadas:**
  - Apple (AAPL)
  - Microsoft (MSFT)
  - Amazon (AMZN)
  - Google (GOOGL)
  - Meta (META)

- **Periodo de Tiempo:**
  - **Desde:** Hace 7 días
  - **Hasta:** 2024-11-29

- **Total de Noticias Obtenidas:** 19 artículos por empresa, totalizando **95 noticias**.

- **Proceso:**
  - Inicialmente, se intentó realizar web scraping en Yahoo Finance, pero no se obtuvieron resultados satisfactorios.
  - Se utilizó la **API de NewsAPI** para asegurar la extracción eficiente de noticias relevantes.

### 1.2. Limpieza y Preprocesamiento de Datos 💻

- **Filtrado de Noticias:**
  - Eliminación de filas con títulos inválidos, vacíos o duplicados.
  
- **Resultados Post-Limpieza:**
  - **Número Total de Noticias Limpias:** 80 noticias.
  - **Distribución de Noticias por Empresa:** Uniformemente distribuidas entre las 5 empresas analizadas.

## 2. Análisis de Sentimientos con VADER 📑

### 2.1. Preprocesamiento de Texto

- **Pasos Realizados:**
  - Tokenización de texto.
  - Eliminación de stopwords.
  - Limpieza de puntuación y números.
  - Normalización de texto.

### 2.2. Extensión del Léxico de VADER 

- **Nuevos Términos Añadidos:**
  - `bullish`: 2.0
  - `bearish`: -2.0
  - `downgrade`: -1.5
  - `upgrade`: 1.5
  - `profit`: 2.0
  - `loss`: -2.0

### 2.3. Aplicación del Análisis de Sentimientos 📑

- **Método Utilizado:**
  - Se aplicó la función `get_sentiment_vader` a los títulos de las noticias para clasificar el sentimiento como **Positivo = 1**, **Neutral = 0** o **Negativo = -1**.

- **Resultados:**
  - **Distribución de Sentimientos:**
    - **Positivo:** 40%
    - **Neutral:** 35%
    - **Negativo:** 25%
  
  - **Sentimiento Promedio Diario por Empresa:** 📈
    - **Apple (AAPL):** Neutral
    - **Microsoft (MSFT):** Positivo
    - **Amazon (AMZN):** Positivo
    - **Google (GOOGL):** Negativo
    - **Meta (META):** Positivo

![sentimiento_promedio_diario_Amazon](https://github.com/user-attachments/assets/dbd16c8a-d7eb-4cbe-857e-8b8e01a3077a)
![sentimiento_promedio_diario_Apple](https://github.com/user-attachments/assets/b0c43746-7bdf-4533-8ee1-be8226d7cdfe)
![sentimiento_promedio_diario_Google](https://github.com/user-attachments/assets/524a36f0-353f-4d90-9735-b1136f475280)
![sentimiento_promedio_diario_Meta](https://github.com/user-attachments/assets/8b1469dd-2e38-459c-9a2b-b965bae40376)
![sentimiento_promedio_diario_Microsoft](https://github.com/user-attachments/assets/97de5bbb-77e0-476d-8cd5-202c1faaa670)

### Con estos resultados concluimos que el resultado del análisis de sentimientos fue existoso.

## Recomendaciones para Trabajos Futuros 📄

- **Ampliar el Rango de Fechas:**
  - Incluir más días de datos para cada empresa para obtener correlaciones más fiables y representativas.

- **Incrementar la Cantidad de Noticias:**
  - Aumentar el número de noticias recopiladas por día para cada empresa para mejorar la precisión del `Sentiment_Score`.

## Siguientes Pasos 🔍
* Análisis de Eventos Específicos:
  * Investigar fechas con movimientos significativos para entender las causas detrás de ellos.
* Incorporar Análisis de Sentimientos combinado con los datos historicos:
  * En futuros análisis, combinar los datos históricos con el análisis de sentimientos podría aportar mayor profundidad.
* Modelado Predictivo:
  * Utilizar los datos procesados para desarrollar modelos que puedan predecir movimientos futuros.



