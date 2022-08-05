from flask import Flask, jsonify

app = Flask(__name__)

import database.connection_db as dbconnetion

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/word/<string:file>/<string:word>')
def getfrequencyWordfile(word,file):
    totalWord=dbconnetion.frequencyFile(word, file)
    if (len(totalWord) > 0):
        return jsonify({'Frequency': totalWord})
    return jsonify({'message': 'frequency is 0'})


@app.route('/<string:word>')
def getfrequencyWord(word):
    totalWord=dbconnetion.frequencyWord(word)
    print(totalWord)
    if (len(totalWord) > 0):
        return jsonify({'Frequency': totalWord})
    return jsonify({'message': 'frequency is 0'})

if __name__ == '__main__':
    app.run(debug=False, port=5000)