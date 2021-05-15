from flask import render_template,url_for,Flask,request
from connection_dbModel import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/<int:id>')
def rount2(id):
    return

@app.route('/tt2/csv-submit',methods=['POST','GET'])
def tt2_csv_submit():
    if request.method=="GET":
        return render_template('tt2-csv-submit.html')
    elif request.method=="POST":
        csvInput=request.form.get('csvInput')
        issuerInput=request.form.get('issuerInput')
        return {"hi":csvInput,"lo":issuerInput}



if __name__ == '__main__':
    app.run(debug=True)
