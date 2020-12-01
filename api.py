import flask
from flask import request, jsonify
from flask_api import FlaskAPI, status, exceptions
import  main

app = FlaskAPI(__name__)
#app.config["DEBUG"] = True


@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = str(request.data.get('message',''))
    response = main.chat(message)

    return  {'message':response}


if __name__ == "__main__":
    app.run(debug=True)