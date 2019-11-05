from flask import Flask, jsonify
from dataBase import getAll

app = Flask(__name__) #Server


@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/users', methods = ['GET'] )
def getUsers():
    return jsonify(getAll.getAllUsers())

if __name__ == '__main__': #Server set up
    app.run(debug=True, port=5000)