''' Deploying app to web by Flask'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    '''Recieve the text user send to be analysed and 
       pass it to emotion_detector function and return result 
       displaying emotions with related scores'''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract emotions and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominent_emotion = response['dominent_emotion']

    if dominent_emotion is None:
        return " Invalid text! Please try again!. "

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}, and "
        f"'dominent_emotion': {dominent_emotion}"
    )

@app.route("/")
def render_index_page():
    ''' function to render the html template for our app'''
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
