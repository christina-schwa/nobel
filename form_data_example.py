#!/usr/bin/env python

from flask import Flask, json, render_template, request
import os

app = Flask(__name__)

@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}.</h1>'.format(language, framework)

    return '''<form method="POST">
            Language <input type="text" name="language">
            Framework <input type="text" name="framework">
            <input type="submit">
            </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=8080)

#http://127.0.0.1:8080/form_example