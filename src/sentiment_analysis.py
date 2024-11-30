import pandas as pd
import numpy as np
import spacy
import altair as alt
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')
# Cargar modelo de spaCy
nlp = spacy.load('en_core_web_sm')

class AdvancedTextAnalyzer:
    def __init__(self):
        self.data = None
        self.processed_texts = []
        self.common_words = None
        
    def load_data(self, csv_file):
        """Carga los datos del CSV"""
        self.data = pd.read_csv(csv_file)
        
    def preprocess_text(self, text):
        """Preprocesa el texto usando spaCy"""
        doc = nlp(str(text).lower())
        # Eliminar stopwords, puntuación y números
        tokens = [token.text for token in doc 
                 if not token.is_stop and not token.is_punct 
                 and not token.like_num]
        return tokens
        
    def analyze_sentiment(self, text):
        """Análisis de sentimiento usando TextBlob"""
        return TextBlob(str(text)).sentiment.polarity
        
    def extract_entities(self, text):
        """Extrae entidades nombradas usando spaCy"""
        doc = nlp(str(text))
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
        
    def process_all_texts(self):
        """Procesa todos los textos y genera análisis"""
        # Procesar títulos
        all_tokens = []
        self.entities_by_company = {}
        
        for idx, row in self.data.iterrows():
            # Preprocesar texto
            tokens = self.preprocess_text(row['title'])
            all_tokens.extend(tokens)
            
            # Extraer entidades
            entities = self.extract_entities(row['title'])
            if row['ticker'] not in self.entities_by_company:
                self.entities_by_company[row['ticker']] = []
            self.entities_by_company[row['ticker']].extend(entities)
        
        # Calcular palabras más comunes
        self.common_words = Counter(all_tokens).most_common(20)
        
        # Análisis de sentimiento
        self.data['sentiment_score'] = self.data['title'].apply(self.analyze_sentiment)
        self.data['processed_tokens'] = self.data['title'].apply(self.preprocess_text)
        
    def create_interactive_visualizations(self):
        """Crea visualizaciones interactivas usando Altair"""
        # 1. Gráfico de tendencias de sentimiento
        sentiment_trend = alt.Chart(self.data).mark_line(point=True).encode(
            x='date:T',
            y='sentiment_score:Q',
            color='ticker:N',
            tooltip=['ticker', 'sentiment_score', 'title']
        ).properties(
            width=700,
            height=400,
            title='Tendencias de Sentimiento por Empresa'
        ).interactive()
        
        # 2. Gráfico de distribución de sentimiento
        sentiment_dist = alt.Chart(self.data).mark_boxplot().encode(
            x='ticker:N',
            y='sentiment_score:Q',
            color='ticker:N',
            tooltip=['ticker', 'sentiment_score']
        ).properties(
            width=700,
            height=400,
            title='Distribución de Sentimiento por Empresa'
        ).interactive()
        
        # 3. Crear DataFrame para palabras comunes
        words_df = pd.DataFrame(self.common_words, columns=['word', 'count'])
        word_freq = alt.Chart(words_df).mark_bar().encode(
            x='count:Q',
            y=alt.Y('word:N', sort='-x'),
            tooltip=['word', 'count']
        ).properties(
            width=700,
            height=400,
            title='Palabras Más Comunes en Títulos'
        ).interactive()
        
        return sentiment_trend, sentiment_dist, word_freq
    
    def generate_summary(self):
        """Genera un resumen del análisis"""
        summary = []
        
        # Resumen por empresa
        for ticker in self.data['ticker'].unique():
            company_data = self.data[self.data['ticker'] == ticker]
            avg_sentiment = company_data['sentiment_score'].mean()
            
            # Entidades más comunes para esta empresa
            company_entities = Counter([ent[0] for ent in self.entities_by_company[ticker]])
            top_entities = company_entities.most_common(5)
            
            summary.append(f"""
            {ticker}:
            - Sentimiento promedio: {avg_sentiment:.3f}
            - Número de noticias: {len(company_data)}
            - Entidades más mencionadas: {', '.join([f"{ent[0]} ({ent[1]})" for ent in top_entities])}
            """)
        
        return "\n".join(summary)

# Ejemplo de uso
analyzer = AdvancedTextAnalyzer()
analyzer.load_data('tech_news.csv')
analyzer.process_all_texts()

# Generar visualizaciones
sentiment_trend, sentiment_dist, word_freq = analyzer.create_interactive_visualizations()

# Guardar visualizaciones como HTML
sentiment_trend.save('sentiment_trend_interactive.html')
sentiment_dist.save('sentiment_dist_interactive.html')
word_freq.save('word_frequency_interactive.html')

# Imprimir resumen
print(analyzer.generate_summary())