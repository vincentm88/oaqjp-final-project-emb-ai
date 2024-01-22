"""Module to run emotion detection"""
import json
import requests

def emotion_detector(text_to_analyze):
    """Function to  take text and send it to emotion detection api"""
    url_base = "https://sn-watson-emotion.labs.skills.network"
    url_case = "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    url = url_base + url_case
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    """convert response text into json"""
    formatted_response = json.loads(response.text)
    emotion_object = formatted_response["emotionPredictions"][0]["emotion"]
    emotions = {}
    if response.status_code == 200:
        emotions["anger"]= ["anger"] 
        emotions["disgust"]= emotion_object["disgust"] 
        emotions["fear"]= emotion_object["fear"] 
        emotions["joy"]= emotion_object["joy"] 
        emotions["sadness"]= emotion_object["sadness"]    
        emotions["dominant_emotion"] = max(emotion_object, key=lambda x: emotion_object[x])
    elif response.status_code == 400:
        emotions["anger"]=None
        emotions["disgust"]=None
        emotions["fear"]=None
        emotions["joy"]=None
        emotions["sadness"]=None
        emotions["dominant_emotion"]=None

    return emotions