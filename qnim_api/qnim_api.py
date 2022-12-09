import json
from flask import Flask, request, jsonify
from qnim import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    piles = request.headers
    row1,row2,row3,row4 = piles["Row1"],piles["Row2"],piles["Row3"],piles["Row4"]
    piles = [int(row1),int(row2),int(row3),int(row4)]
    print(piles)
    row_choice,amount = get_quantum_move(piles)
    result = '{"Pick from row": "'+str(row_choice)+'","Amount":"'+str(amount)+'"}'
    result = json.loads(result)
    return (result)

app.run(debug=True)