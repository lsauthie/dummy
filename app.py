'''
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

todo:
    > DONE: link this script and the simi. script
'''
import flask
from flask import request, jsonify
import similarities as sim
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome Ludovic</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    
# A route to return all of the available entries in our catalog.
@app.route('/api/v1/books/all', methods=['GET'])
def api_all():
    return jsonify(books)
    
    
#http://127.0.0.1:5000/api/v1/dole?strings=ludovic is a big man, ludovic is a man, ludovic is a great man, sarah is his sister, patrizi is his mother, sarah is beautiful
@app.route('/api/v1/dole', methods=['GET'])
def dole():
    if 'strings' in request.args:
        arg_strings = request.args['strings']
        
        if bool(BeautifulSoup(arg_strings, "html.parser").find()):#check for html tags
            return 'Error: Please avoid html tags in strings'
        else:
            strings = [i.strip() for i in arg_strings.split(',')]
            #compare strings
            res = sim.sim(strings, 0.7) #list of strings and similarity ratio
        
    else:
        return 'Error: Please provide strings, i.e. /api/v1/dole?strings=string1, string2, string3'
        
    return jsonify(res)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)