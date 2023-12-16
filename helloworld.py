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
                  "teve", "tendo", "estava", "estávamos", "outra", "ah", "algo", "ser",
                  "tão", "posso", "são", "onde", "ou", "sido", "sabe", "minuto",
                  "tenho", "temos", "pode", "pequeno", "uma", "uns", "um", "pai", "mãe", "tio", "irmã",
                  "sou", "tudo", "diga", "lembra", "morava", "te", "sua", "seu", "tua", "teu", "suas", "seus", "lo", "estão",
                  "minha", "meu", "minhas", "meus", "ter", "coisa", "então", "na", "ano", "sim", "nada", "ver", "ei", "sei",
                  "também"])


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



#FILME IV - Han Solo
resultHan1 = df.loc[df['personagem'] == 'HAN', 'diálogo']

all_summaryFalasHan1 = "\n".join(s for s in resultHan1)
wordcloudFalasHan1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasHan1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasHan1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasHan1);
wordcloudFalasHan1.to_file("falasHanEpisodeIV.png")


#Filme V - Falas Han Solo
resultHan2 = df1.loc[df1['personagem'] == 'HAN', 'diálogo']

all_summaryFalasHan2 = "\n".join(s for s in resultHan2)
wordcloudFalasHan2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasHan2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasHan2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasHan2);
wordcloudFalasHan2.to_file("falasHanEpisodeV.png")


#Filme VI - Falas Han Solo
resultHan3 = df2.loc[df2['personagem'] == 'HAN', 'diálogo']

all_summaryFalasHan3 = "\n".join(s for s in resultHan3)
wordcloudFalasHan3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasHan3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasHan3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasHan3);
wordcloudFalasHan3.to_file("falasHanEpisodeVI.png")


#FILME IV - Leia
resultLeia1 = df.loc[df['personagem'] == 'LEIA', 'diálogo']

all_summaryFalasLeia1 = "\n".join(s for s in resultLeia1)
wordcloudFalasLeia1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLeia1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLeia1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLeia1);
wordcloudFalasLeia1.to_file("falasLeiaEpisodeIV.png")


#Filme V - Falas Leia
resultLeia2 = df1.loc[df1['personagem'] == 'LEIA', 'diálogo']

all_summaryFalasLeia2 = "\n".join(s for s in resultLeia2)
wordcloudFalasLeia2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLeia2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLeia2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLeia2);
wordcloudFalasLeia2.to_file("falasLeiaEpisodeV.png")


#Filme VI - Falas Leia
resultLeia3 = df2.loc[df2['personagem'] == 'LEIA', 'diálogo']

all_summaryFalasLeia3 = "\n".join(s for s in resultLeia3)
wordcloudFalasLeia3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasLeia3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasLeia3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasLeia3);
wordcloudFalasLeia3.to_file("falasLeiaEpisodeVI.png")


#FILME IV - Threepio
resultThreepio1 = df.loc[df['personagem'] == 'THREEPIO', 'diálogo']

all_summaryFalasThreepio1 = "\n".join(s for s in resultThreepio1)
wordcloudFalasThreepio1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasThreepio1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasThreepio1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasThreepio1);
wordcloudFalasThreepio1.to_file("falasThreepioEpisodeIV.png")


#Filme V - Falas Threepio
resultThreepio2 = df1.loc[df1['personagem'] == 'THREEPIO', 'diálogo']

all_summaryFalasThreepio2 = "\n".join(s for s in resultThreepio2)
wordcloudFalasThreepio2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasThreepio2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasThreepio2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasThreepio2);
wordcloudFalasThreepio2.to_file("falasThreepioEpisodeV.png")


#Filme VI - Falas Threepio
resultThreepio3 = df2.loc[df2['personagem'] == 'THREEPIO', 'diálogo']

all_summaryFalasThreepio3 = "\n".join(s for s in resultThreepio3)
wordcloudFalasThreepio3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasThreepio3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasThreepio3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasThreepio3);
wordcloudFalasThreepio3.to_file("falasThreepioEpisodeVI.png")




#FILME IV - Ben
resultBen1 = df.loc[df['personagem'] == 'BEN', 'diálogo']

all_summaryFalasBen1 = "\n".join(s for s in resultBen1)
wordcloudFalasBen1 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasBen1)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasBen1, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasBen1);
wordcloudFalasBen1.to_file("falasBenEpisodeIV.png")


#Filme V - Falas Ben
resultBen2 = df1.loc[df1['personagem'] == 'BEN', 'diálogo']

all_summaryFalasBen2 = "\n".join(s for s in resultBen2)
wordcloudFalasBen2 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasBen2)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasBen2, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasBen2);
wordcloudFalasBen2.to_file("falasBenEpisodeV.png")


#Filme VI - Falas Ben
resultBen3 = df2.loc[df2['personagem'] == 'BEN', 'diálogo']

all_summaryFalasBen3 = "\n".join(s for s in resultBen3)
wordcloudFalasBen3 = WordCloud(stopwords=stopwords, background_color = "black", width=1600, height=800).generate(all_summaryFalasBen3)
# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloudFalasBen3, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloudFalasBen3);
wordcloudFalasBen3.to_file("falasBenEpisodeVI.png")