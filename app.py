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
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>New York University</a>","5","No Connection"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>The University Hospital of Giessen and Marburg</a>","2","No Connection"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>Cleveland Clinic Foundation</a>","9","Error"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>Johns Hopkins University</a>","3","Error"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>OhioHealth</a>","8","Shut Down"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>University of Rochester</a>","4","OK"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1'>Washington University</a>","3","OK"]
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
  },
  "disconnected_hospitals": random.randint(2, 5),
  "success_percentage": random.randint(0,100),
  "cpu_usage": random.randint(0,100),
  "memory": random.randint(0,100),
  "disk_space": random.randint(0,100),
  "message_types": {
    "msptwc": random.randint(1,7),
    "msptwoc": random.randint(16,80),
    "emrwc": random.randint(3,11),
    "emrwoc": random.randint(23,60),
    "dicomwc": random.randint(11,34),
    "dicomwoc": random.randint(15,90),
    "biobankingwc": random.randint(45,103),
    "biobankingwoc": random.randint(24,88),
  },
  "patient_consent": {
    "consented": random.randint(1,7),
    "total": random.randint(1,10)
  },
  "error_insights": {
    "mspt": random.randint(1,7),
    "emr": random.randint(1,10),
    "dicom": random.randint(2,9),
    "biobanking": random.randint(3,9),
  },
  "insights": {
    "alerts": random.randint(1,7),
    "errors": random.randint(1,10)
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
