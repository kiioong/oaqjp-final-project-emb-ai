import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json,headers=headers)

    response_json = json.loads(response.text)
    emotion_predections = response_json['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_predections, key=emotion_predections.get)

    emotion_predections["dominant_emotion"] = dominant_emotion

    return emotion_predections
