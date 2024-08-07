# import the Flask class from the flask library
from flask import Flask, render_template, jsonify
import sqlite3

# object inheriting from Flask
app = Flask(__name__)

# this function gets a random word, the correct definiton of it, and the incorrect defintion
def get_word():
    # connecting to SQlite database
    conn = sqlite3.connect('word_definition.db')
    c = conn.cursor()
    # selecting a random word with definition 
    c.execute('SELECT word, definition FROM words ORDER BY RANDOM() LIMIT 1')
    # gets one as opposed to fetchmany
    word = c.fetchone()
    # gets a random incorrect definition
    c.execute('SELECT definition FROM words WHERE definition != ? ORDER BY RANDOM() LIMIT 1', (word[1],))
    incorrect_definition = c.fetchone()
    # closes database connection
    conn.close()
    # word 0 is the correct word to be asked
    # word 1 is the correct definition
    # incorrect_definition[0] is 0 as it is the only element we got, no word selected here
    return word[0], word[1], incorrect_definition[0]

# gets to home page
@app.route('/')
def index():
    # finds .html file in templates and sends rendered html to be opened on browser
    return render_template('web-front.html')

# gets random word and its defintion
@app.route('/get_word', methods=['GET'])
def get_word_route():
    word, definition, incorrect_definition = get_word()
    # returning as json response
    return jsonify({'word': word, 'definition': definition, 'incorrect_definition': incorrect_definition})

# runs script in debug mode
if __name__ == '__main__':
    app.run(debug=True)
