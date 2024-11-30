# Resultados del análisis EDA

## Conclusiones y Observaciones
* Descripción de los Datos:
  * El conjunto de datos contiene información diaria de precios y volúmenes de las 5 acciones más capitalizadas entre 2020 y 2021.
  * Los atributos principales son: 'Open', 'High', 'Low', 'Close', 'Adj Close' y 'Volume'.
* Limpieza de Datos y Valores Faltantes:
  * Se eliminaron filas con valores faltantes en la columna 'Value' para asegurar la integridad del análisis.
  * No se encontraron duplicados después de la limpieza inicial.
* Visualizaciones:
  * Las gráficas de precios de cierre ajustado muestran tendencias generales de crecimiento en las acciones tecnológicas durante el período analizado.
  * Los volúmenes de negociación presentan variaciones que podrían relacionarse con eventos específicos del mercado.
  * Los retornos diarios permiten observar la volatilidad y posibles correlaciones en los movimientos de las acciones.
* Análisis de Correlación:
  * Las acciones analizadas presentan altas correlaciones entre sí, lo que es común en empresas del mismo sector o en mercados alcistas generales.
  * Esto sugiere que factores macroeconómicos y sentimentales podrían estar afectando a estas acciones de manera similar.

## Siguientes Pasos
* Análisis de Eventos Específicos:
  * Investigar fechas con movimientos significativos para entender las causas detrás de ellos.
* Incorporar Análisis de Sentimientos:
  * En futuros análisis, combinar los datos históricos con el análisis de sentimientos podría aportar mayor profundidad.
* Modelado Predictivo:
  * Utilizar los datos procesados para desarrollar modelos que puedan predecir movimientos futuros.

## Notas Finales  
Este EDA nos brinda una comprensión inicial de los datos históricos de las acciones más capitalizadas. Nos prepara para etapas posteriores del proyecto donde integraremos análisis más complejos para mejorar la toma de decisiones de inversión.


# Resultados del análisis de texto y sentimientos  

## Análisis de Frecuencia de Palabras
![Palabras más comunes en Títulos](https://github.com/user-attachments/assets/6ca0f704-31bb-47bf-9310-ae8427b2d69f)

La palabra "ai" es la más frecuente, reflejando el dominio de la Inteligencia Artificial en las noticias  
"Meta" y "Motley Fool" aparecen con alta frecuencia, indicando cobertura significativa  
Palabras financieras como "stock" e "insider" tienen presencia notable  
Las principales empresas (apple, microsoft, google, amazon) muestran frecuencias equilibradas  
"nvidia" aparece frecuentemente, sugiriendo su importancia en el ecosistema tecnológico  


## Tendencias de sentimiento
![Tendencias de Sentimiento por Empresa](https://github.com/user-attachments/assets/413b24ad-70f5-4850-a848-f52fa01b8c8c)

Alta volatilidad el 29 de noviembre para todas las empresas  

**Patrones de sentimiento:**  
META muestra la tendencia más estable pero generalmente más baja  
AMZN exhibe los picos más altos de sentimiento positivo  
AAPL y MSFT muestran patrones similares de volatilidad  
GOOGL mantiene una tendencia moderada  
El período del 21 al 28 de noviembre muestra movimientos más suaves.  


## Distribución de Sentimiento
![Distribución de Sentimiento por Empresa](https://github.com/user-attachments/assets/70857b9f-51a8-415d-b619-bedb26a51d65)


Todas las empresas muestran una distribución centrada en valores positivos  

**Características por empresa:**  

AMZN: Mayor mediana y dispersión hacia valores positivos  
AAPL: Distribución simétrica con valores atípicos positivos  
MSFT: Distribución similar a AAPL pero más compacta  
GOOGL: Menor dispersión, sentimiento más consistente  
META: Distribución más baja pero con valores atípicos en ambas direcciones  







