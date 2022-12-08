import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.write("""
         # The practical application
""")

st.write("""
         ## Wordcloud
""")

corpus = st.text_area ('Copy and paste a text and press enter or submit')
b1 = st.button("Submit")


exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 
                'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 
                'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 
                'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 
                'au', 'c', 'aussi', 'toutes', 'autre', 'comme']

#if len(corpus)>0:
st.set_option('deprecation.showPyplotGlobalUse', False)
if corpus or b1:
    wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 50).generate(corpus)
    plt.imshow(wordcloud)
    plt.axis('off')
    st.pyplot()


