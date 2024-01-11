from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.route('/get-text', methods = ['POST'])
# def get_text():
#     content = request.get_json()
#     transformed_text = {'key': 'processed' + content['text']}
#     return jsonify(transformed_text)
 
#get data from vue js when user click subnmit
@app.route('/retrieve-data', methods = ['POST']) #get data from vue js (text) since vue posted it, methods= ['POST']
def retrieve_data(): 
    user_input = request.get_json()['_rawValue']
    # print(user_input)
    return user_input

#get data from vue js (text)
#post transformed data to vue js
if __name__ == '__main__':
    app.run(debug=True)
    
#res
# status, 
# data : {analysis: {abstractive: {rephrased_text}, sentiment: {sentiment_score}, extractive: {keywords}, reliability: {reliability_score}}