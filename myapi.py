import os
import nlpcloud

api_key = os.getenv("NLPCLOUD_API_KEY")
if not api_key:
    raise RuntimeError("NLPCLOUD_API_KEY is not set in the environment.")

client1 = nlpcloud.Client("gpt-oss-120b", api_key, gpu=True)
client2 = nlpcloud.Client("python-langdetect", api_key, gpu=False)

def ner(text1, text2):
    response = client1.entities(text1,text2)
    return response

def sentiment_analysis(text):
    response = client1.sentiment(text)
    return response


def language_detection(text):
    response = client2.language(text)
    return response
