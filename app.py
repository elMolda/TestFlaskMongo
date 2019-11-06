from flask import Flask, jsonify, request, abort, redirect, url_for, make_response
from dataBase import getAll, addOne

app = Flask(__name__) #Server


@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({"message": 'Pong'})

@app.route('/users', methods = ['GET', 'POST'] )
def manageUsers():
    res = None
    if request.method == 'GET':
        res = make_response(jsonify(getAll.getAllUsers()), 200)
    elif request.method == 'POST':
        returned = addOne.addOneUser(request)
        if returned == True:
            res = make_response(jsonify(getAll.getAllUsers()), 201)
        else:
            return abort(400, "Error al insertar")
    return res

if __name__ == '__main__': #Server set up
    app.run(debug=True, port=5000)