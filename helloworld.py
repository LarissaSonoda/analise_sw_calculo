import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


#SETANDO STOPWORDS

stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os", "que", "não",
                  "sobre", "está", "para", "mas", "a", "o", "está",
                  "ele", "eles", "ela", "elas", "eu", "quer", "é", "um", "vamos", "quem",
                  "isso", "por", "muito", "aqui", "tem", "ok", "há", "estou", "aí", "fazer",
                  "nos", "nosso", "nossa", "nós", "se", "e", "vai", "como", "quando", "o que", "quem", "quando",
                  "esse", "este", "esses", "essa", "esta", "essas", "estas", "estes",
                  "agora", "lá", "vou", "vai", "dá", "boa", "maior", "grupo",
                  "teve", "tendo"])


df = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeIV_ptBR");

summary = df.dropna(subset=['personagem'], axis=0)['personagem']

all_summary = "\n".join(s for s in summary)

wordcloud = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud);
wordcloud.to_file("personagens_IV.png")


df1 = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeV_ptBR");

summary1 = df1.dropna(subset=['personagem'], axis=0)['personagem']

all_summary1 = "\n".join(s for s in summary1)
wordcloud1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud1);
wordcloud1.to_file("personagens_V.png")


df2 = pd.read_excel("C:\\Users\\laris\\Desktop\\estudos_ferias20232\\python\\SW - Episode IV.xlsx", sheet_name = "SW_EpisodeVI_ptBR");

summary2 = df.dropna(subset=['personagem'], axis=0)['personagem']

all_summary2 = "\n".join(s for s in summary2)

wordcloud2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summary2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud2);
wordcloud2.to_file("personagens_VI.png")


# Filme IV - Luke - Falas

resultLuke1 = df.loc[df['personagem'] == 'LUKE', 'diálogo']

all_summaryFalasLuke1 = "\n".join(s for s in resultLuke1)
wordcloudFalasLuke1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLuke1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLuke1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLuke1);
wordcloudFalasLuke1.to_file("falasLukeEpisodeIV.png")


#Filme V - Falas Luke
resultLuke2 = df1.loc[df1['personagem'] == 'LUKE', 'diálogo']

all_summaryFalasLuke2 = "\n".join(s for s in resultLuke2)
wordcloudFalasLuke2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLuke2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLuke2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLuke2);
wordcloudFalasLuke2.to_file("falasLukeEpisodeV.png")


#Filme VI - Falas Luke
resultLuke3 = df2.loc[df2['personagem'] == 'LUKE', 'diálogo']

all_summaryFalasLuke3 = "\n".join(s for s in resultLuke3)
wordcloudFalasLuke3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLuke3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLuke3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLuke3);
wordcloudFalasLuke3.to_file("falasLukeEpisodeVI.png")
