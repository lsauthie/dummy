'''
Useful references
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/
'''

import flask
from flask import request, jsonify
import similarities as sim
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from dbswissre import Swissre
from base import Session, engine, Base



app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    
    url_root = request.url_root
    
    link1 = url_root + "dole/flush"
    link2 = url_root + "dole/all"
    link3 = url_root + "dole?strings=ludovic is a big man, ludovic is a man, ludovic is a great man, sarah is his sister, patrizi is his mother, sarah is beautiful"
    
    welcome = """ <h1>Welcome Ludovic Bis</h1>
    
    <a href="{}">/dole/flush</a></br>
    <a href="{}">/dole/all   </a></br>
    <a href="{}">/dole?strings=ludovic is a big man, ludovic is a man, ludovic is a great man, sarah is his sister, patrizi is his mother, sarah is beautiful</a>
    
   
    """.format(link1, link2, link3)
    
    return welcome


@app.route('/dole/flush', methods=['GET'])
def dole_flush():
    session = Session()
    session.query(Swissre).delete()
    session.commit()
    session.close()
    return "Swissre table has been flushed"

@app.route('/dole/all', methods=['GET'])
def dole_all():
    session = Session()
    swissre = session.query(Swissre).all()
    
    d = {}
    for i in swissre:
        reference = i.reference
        sentence = i.sentence
        ratio = i.ratio
        t = (sentence, ratio)
        
        if reference in d:
            if t not in d[reference]:
                d[reference].append(t)
        else:
            d[reference] = [t]
    
    session.close()
    return jsonify(d)

    
#http://127.0.0.1:5000/dole?strings=ludovic is a big man, ludovic is a man, ludovic is a great man, sarah is his sister, patrizi is his mother, sarah is beautiful
@app.route('/dole', methods=['GET'])
def dole():
    if 'strings' in request.args:
        arg_strings = request.args['strings']
        
        if bool(BeautifulSoup(arg_strings, "html.parser").find()):#check for html tags
            return 'Error: Please avoid html tags in strings'
        else:
            strings = [i.strip() for i in arg_strings.split(',')]
            #compare strings
            res = sim.sim(strings, 0.7) #list of strings and similarity ratio
            
            #add information into DB
            session = Session()
            for reference, l in res.items():
                for item in l:
                    db_row = Swissre(reference, item[0], item[1])
                    session.add(db_row)
            
            
            session.commit()
            session.close()
                
        
    else:
        return 'Error: Please provide strings, i.e. /api/v1/dole?strings=string1, string2, string3'
        
    return jsonify(res)
	
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(host='0.0.0.0',port=5000)
    
