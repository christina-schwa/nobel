#!/usr/bin/env python

from flask import Flask, json, render_template, request
import os

app = Flask(__name__)

@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')

    return '''<h1>The langage is: {}</h1>
            <h1>The framework is: {}</h1>
            <h1>The website is: {}</h1>'''.format(language, framework, website)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

#http://127.0.0.1:8080/query_example?language=Python
#http://127.0.0.1:8080/query_example?language=PHP&framework=Laravel&website=php.com

