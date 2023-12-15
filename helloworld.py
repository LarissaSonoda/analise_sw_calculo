import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

df = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeIV_ptBR");

summary = df.dropna(subset=['personagem'], axis=0)['personagem']

all_summary = "\n".join(s for s in summary)
stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os"])
wordcloud = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud);
wordcloud.to_file("personagens_IV.png")

df2 = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeV_ptBR");

summary2 = df2.dropna(subset=['personagem'], axis=0)['personagem']

all_summary2 = "\n".join(s for s in summary)
wordcloud2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud2);
wordcloud2.to_file("personagens_V.png")

df3 = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeVI_ptBR");

summary3 = df3.dropna(subset=['personagem'], axis=0)['personagem']

all_summary3 = "\n".join(s for s in summary)
wordcloud3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud3);
wordcloud3.to_file("personagens_VI.png")