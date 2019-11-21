import random
import json
from flask import Flask, jsonify, Response, request
  
app = Flask(__name__) 

hospitals = [
  {
    "columns":[
      {"text":"Hospital Name","type":"string"},
      {"text":"Erros","type":"string"},
      {"text":"Status","type":"string"}
    ],
    "rows":[
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=nyu'>New York University</a>","5","No Connection"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=uhgm'>The University Hospital of Giessen and Marburg</a>","2","No Connection"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=ccf'>Cleveland Clinic Foundation</a>","9","Error"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=jhu'>Johns Hopkins University</a>","3","Error"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=oh'>OhioHealth</a>","8","Shut Down"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=ur'>University of Rochester</a>","4","OK"],
      ["<a href='http://localhost:3000/d/SVYoZG0Zk/biogen-dashboard-2?orgId=1&var-hname=wu'>Washington University</a>","3","OK"]
    ],  
    "type":"table"
  }
]

hospitalDict = {
  'nyu': 'New York University',
  'uhgm': 'The University Hospital of Giessen and Marburg',
  'ccf': 'Cleveland Clinic Foundation',
  'jhu': 'Johns Hopkins University',
  'oh': 'OhioHealth',
  'ur': 'University of Rochester',
  'wu': 'Washington University'
}

@app.route('/') 
def hello_world(): 
    return jsonify({
  "requests_handled": random.randint(7209, 14324),
  "requests_duration_milliseconds": random.randint(1122473,1235257),
  "request_failures": int(random.randint(2, 7)),
  "documents_loaded": {
    "fast": random.randint(1,7),
    "slow": random.randint(16,60)
  },
  "disconnected_hospitals": int(random.randint(2, 5)),
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
  },
  "hospital_connected" : [
    {"key":'nyu', "value": random.choice([0, 1])},
    {"key":'uhgm', "value": random.choice([0, 1])},
    {"key":'ccf', "value": random.choice([0, 1])},
    {"key":'jhu', "value": random.choice([0, 1])},
    {"key":'oh', "value": random.choice([0, 1])},
    {"key":'ur', "value": random.choice([0, 1])},
    {"key":'wu', "value": random.choice([0, 1])}
  ],
  "hospital_message_types" : [
    {'nyu': {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'uhgm': {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'ccf': {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'jhu': {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'oh' : {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'ur' : {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }},
    {'wu' : {
      "mspt": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "emr": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "dicom": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "biobanking": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)},
      "hl7": {"errors": random.randint(1,7), "messages": random.randint(1,7), "nonconsented": random.randint(1,7)}
      }}
  ]
})

@app.route('/search', methods=["POST"]) 
def search_data(): 
    return Response(json.dumps(hospitalDict.keys()),  mimetype='application/json')

@app.route('/query', methods=["POST"]) 
def query_data(): 
    return Response(json.dumps(hospitals),  mimetype='application/json')

@app.route('/hospitalName', methods=["GET"]) 
def get_hospital_name(): 
    hname = request.args.get('hospitalName')
    hospital_name_html = "<center><h2>{}</h2></center>".format(hospitalDict[hname])
    return Response(hospital_name_html, status=200,  mimetype='text/plain', headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'PUT, GET, POST, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    })

@app.route('/hospitalkeys', methods=["GET"]) 
def get_hospital_keys(): 
    return Response(json.dumps(hospitalDict.keys()),  mimetype='application/json')
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005, debug=True)  
