from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
from pymysql import cursors
import string
import json
from random import *

def loadChallenges():
    with open("./challenges.json") as fd:
        return json.load(fd)
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'workshop_secu'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(cursorclass=cursors.DictCursor)
mysql.init_app(app)


@app.route("/api/foods")
def getFoods():
    id = request.args.get("id")
    if not id or ";" in id:
        return jsonify({"error": "Cheating.. mmh?"})
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from foods where id=" + id)
    data = cursor.fetchall()
    return jsonify(data)


@app.route("/api/foods2")
def getFoods2():
    id = request.args.get("id")
    if not id or ";" in id:
        return jsonify({"error": "Cheating.. mmh?"})
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from foods2 where id=" + id)
    data = cursor.fetchall()
    return jsonify(data)


@app.route("/api/fakeLogin")
def getFakeLogin():
    pseudo = request.args.get("pseudo")
    pwd = request.args.get("password")
    if not pseudo or not pwd or ";" in pwd:
        return jsonify({"error": "Cheating.. mmh?"})
    pseudo = pseudo.lower().replace("or", "").replace("||", "")
    pwd = pwd.lower().replace("or", "").replace("||", "")
    cursor = mysql.connect().cursor()
    query = "SELECT * FROM fakeCreds WHERE "
    query += "pseudo='" + pseudo + "' and password='" + pwd + "'"
    try:
        cursor.execute(query)
    except:
        return jsonify({"error": "Invalid query: " + query})
    data = cursor.fetchall()
    if not data:
        return jsonify({"error": "Invalid credentials"})
    return jsonify(data)


@app.route("/api/random")
def getRandom():
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    return jsonify({"content": "".join(choice(allchar) for x in range(randint(min_char, max_char)))})

@app.route("/api/checkFlag")
def checkFlag():
    categoryName = request.args.get("categoryName")
    challName = request.args.get("challName")
    flag = request.args.get("flag")
    isok = loadChallenges()[categoryName][challName]["flag"] == flag
    return jsonify({"isok": isok})

@app.route("/api/getChallenges")
def getChallenges():
    challenges = loadChallenges()
    for category in challenges.values():
        for chall in category.values():
            chall["flag"] = ""
    return jsonify({"challenges": challenges})

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
