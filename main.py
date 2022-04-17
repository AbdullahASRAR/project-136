from flask import Flask,request,jsonify
from data import data
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"succes"
    }),200  
@app.route("/star")
def star():
    name = request.args.get("name")
    star_data=next(item for item in data if item ["name"] == name)
    return jsonify({
        "data":star_data,
        "message":"succes"
    }),200
    
if __name__=="__main__":
    app.run()    