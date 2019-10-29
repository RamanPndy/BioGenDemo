import random
import json
from flask import Flask, jsonify, Response
  
app = Flask(__name__) 

hospitals = [
  {
    "columns":[
      {"text":"Hospital Name","type":"string"},
      {"text":"Erros","type":"string"},
      {"text":"Status","type":"string"}
    ],
    "rows":[
      ["New York University","5","No Connection"],
      ["The University Hospital of Giessen and Marburg","2","No Connection"],
      ["Cleveland Clinic Foundation","9","Error"],
      ["Johns Hopkins University","3","Error"],
      ["OhioHealth","8","Shut Down"],
      ["University of Rochester","4","OK"],
      ["Washington University","3","OK"]
    ],
    "type":"table"
  }
]
  
@app.route('/') 
def hello_world(): 
    return jsonify({
  "requests_handled": random.randint(7209, 14324),
  "requests_duration_milliseconds": random.randint(1122473,1235257),
  "request_failures": random.randint(2, 7),
  "documents_loaded": {
    "fast": random.randint(1,7),
    "slow": random.randint(16,60)
  }
})

@app.route('/search', methods=["POST"]) 
def search_data(): 
    return Response(json.dumps(hospitals[0]["columns"]),  mimetype='application/json')

@app.route('/query', methods=["POST"]) 
def query_data(): 
    return Response(json.dumps(hospitals),  mimetype='application/json')
  
if __name__ == '__main__':
    app.run()  
