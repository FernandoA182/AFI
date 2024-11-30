📁 **Carpeta con bases de datos originales**

Datos del archivo "datos_acciones.csv" adjunto en esta carpeta data.  
Para este trabajo y análisis EDA se extrajeron los datos de 5 empresas que tienden a estar entre las más capitalizadas, las cuales son:  

🍎 Apple Inc. (AAPL)  
💻 Microsoft Corporation (MSFT)  
📦 Amazon.com, Inc. (AMZN)  
🔍 Alphabet Inc. (GOOGL)  
👥 Meta Platforms, Inc. (META) - anteriormente Facebook  



📊 **Análisis y Procesamiento**   
El notebook "AFI.ipynb" adjunto en la carpeta src, además de contener el análisis EDA, tambien explica la descarga de estos datos provenientes de Yahoo Finance, mediante la librería "yfinance", su restructuración, y como fueron guardados. Además de su descripción, información general del data frame, estadisticas descriptivas, entre otros aspectos reelevantes de estos datos.



📰 **Web Scraping de Noticias**  
El siguiente archivo adjunto en esta carpeta, llamado "tech_news.csv", es el segundo resultado de ejecutar el notebook "AFI.ipynb", en el cual se realiza  web scraping que obtiene noticias de sitios como Finviz:
Este script recopiló noticias sobre las empresas tecnológicas anteriormente mencionadas.



📱 **Fuentes de Datos:**

📊 Finviz  
📈 MarketWatch  
📰 Otros sitios de noticias financieras  



📄 **Estructura del Dataset:**  
El script guardó los datos en tech_news.csv con:

🏷️ Ticker (símbolo de la empresa)  
📅 Fecha  
📝 Título de la noticia  
🔍 Fuente  
🔗 URL  
   
Este archivo CSV se convirtió en la base para nuestro análisis posterior de sentimiento y visualizaciones, a partir del notebook "sentiment_analysis.py" adjunto en la carpeta src.
