''' Executing this function initiates emotion detection 
    to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This function implements the emotion_detector function'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_begining = "For the given statement, the system response is "
    response_anger = f"'anger': {response['anger']}, "
    response_disgust = f"'disgust': {response['disgust']}, "
    response_fear = f"'fear': {response['fear']}, "
    response_joy = f"'joy': {response['joy']} and "
    response_sadness = f"'sadness': {response['sadness']}."
    response_end = f" The dominant emotion is {response['dominant_emotion']}."
    formatted_response = response_begining
    formatted_response += response_anger + response_disgust + response_fear
    formatted_response += response_joy + response_sadness + response_end
    return str(formatted_response)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
