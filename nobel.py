#!/usr/bin/env python

from flask import Flask, json, render_template, request, redirect
import os

app = Flask(__name__)

# This is the easy part:
@app.route("/all")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #render_template is always looking in templates folder
    return render_template('index.html',data=data_json)

# This creates the "/<year>" GET endpoint. 
# I also tried using an if/else statement for GET method vs. POST method, but it didn't work. 
@app.route("/<year>", methods=['GET'])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json["prizes"]
    year = request.view_args['year']
    output_data = [x for x in data if x['year']==year]
    #render_template is always looking in templates folder
    return render_template('index.html',data=output_data)

# This creates the "/<year>" POST endpoint.
# My previous version successfully created a form but did not write to the JSON file.
# When I tried to incorporate the code for appending a JSON file, it did not work, and the form part didn't work anymore, either.
@app.route("/<year>", methods=['POST', 'GET'])
def new_prize():
    if request.method == 'POST':
        #json_url = os.path.join(app.static_folder,"","nobel.json")
        #data_json = json.load(open(json_url))
        
        # I don't know why some of these variables are sort of grayed out...
        new_year = request.form['year']
        new_category = request.form['category']
        new_id = request.form['id']
        new_firstname = request.form['firstname']
        new_surname = request.form['surname']
        new_motivation = request.form['motivation']
        new_share = request.form['share']

        nobel_dict = {'year':new_year}
        with open('./static/nobel.json','r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["prizes"].append(nobel_dict)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
        return render_template('index.html',data=nobel_dict)

#I couldn't get any of the "else" conditions to work properly...
    #else:
        #return render_template('index.html')
        #return redirect render_template('index.html')
        #return redirect(json_url)

if __name__ == '__main__':
    app.run(debug=True, port=8000)