# utils/wordcloud_gen.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, output_path="assets/wordcloud.png"):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
