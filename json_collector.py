from prometheus_client import start_http_server, Metric, Gauge,CollectorRegistry,pushadd_to_gateway
from prometheus_client.core import GaugeMetricFamily, REGISTRY
import json
import requests
import sys
import time
import os
import arrow
from datetime import datetime, timedelta

class JsonCollector(object):
  def __init__(self):
    self._endpoint = "http://localhost:5005/"
  def collect(self):
    # Fetch the JSON
    os.environ['NO_PROXY'] = 'localhost,127.0.0.1' 
    response = json.loads(requests.get(self._endpoint).content.decode('UTF-8'))

    # Convert requests and duration to a summary in seconds
    metric = Metric('svc_requests_duration_seconds',
        'Requests time taken in seconds', 'summary')
    metric.add_sample('svc_requests_duration_seconds_count',
        value=response['requests_handled'], labels={})
    metric.add_sample('svc_requests_duration_seconds_sum',
        value=response['requests_duration_milliseconds'] / 1000.0, labels={})
    yield metric

    # Counter for the failures
    metric = Metric('svc_requests_failed_total',
       'Requests failed', 'summary')
    metric.add_sample('svc_requests_failed_total',
       value=response['request_failures'], labels={})
    yield metric

    # Metrics with labels for the documents loaded
    metric = Metric('svc_documents_loaded', 'Requests failed', 'gauge')
    for k, v in response['documents_loaded'].items():
      metric.add_sample('svc_documentes_loaded', value=v, labels={'repository': k})
    yield metric

    metric = Metric('svc_percentage_of_success', 'Request Sucess Percentage', 'gauge')
    metric.add_sample('svc_percentage_of_success', value=response['success_percentage'], labels={})
    yield metric

    metric = Metric('svc_cpu_usage', 'CPU Usage', 'gauge')
    metric.add_sample('svc_cpu_usage', value=response['cpu_usage'], labels={})
    yield metric

    metric = Metric('svc_memory', 'Memory', 'gauge')
    metric.add_sample('svc_memory', value=response['memory'], labels={})
    yield metric

    metric = Metric('svc_disk_space', 'Disk Space', 'gauge')
    metric.add_sample('svc_disk_space', value=response['disk_space'], labels={})
    yield metric

    metric = Metric('svc_disconnected_hospitals', 'Disconnected Hospitals', 'gauge')
    metric.add_sample('svc_disconnected_hospitals', value=response['disconnected_hospitals'], labels={})
    yield metric

    metric = Metric('svc_message_types', 'Message Types', 'gauge')
    for k, v in response['message_types'].items():
      metric.add_sample('svc_message_types', value=v, labels={'repository': k})
    yield metric

    metric = Metric('svc_patient_consent', 'Pateint Consent', 'gauge')
    for k, v in response['patient_consent'].items():
      metric.add_sample('svc_patient_consent', value=v, labels={'repository': k})
    yield metric

    total_errors = 0
    metric = Metric('svc_error_insights', 'Error Insights', 'gauge')
    for k, v in response['error_insights'].items():
      metric.add_sample('svc_error_insights', value=v, labels={'repository': k})
      total_errors += v
    yield metric

    metric = Metric('svc_error_insights_total', 'Total Errors', 'summary')
    metric.add_sample('svc_error_insights_total', value=total_errors, labels={})
    yield metric

    metric = Metric('svc_insights', 'Hospital Insights', 'gauge')
    for k, v in response['insights'].items():
      metric.add_sample('svc_insights', value=v, labels={'repository': k})
    yield metric

    metric = Metric('svc_hospital_connected', 'Hospital Connection Status', 'gauge')
    for hospital in response['hospital_connected']:
      for hkey, hvalue in hospital.iteritems():
        hospital_label = hospital.get('key')
        hospital_value = hospital.get('value')
        metric.add_sample('svc_hospital_connected', value=hospital_value, labels={'hospital_name': hospital_label})
    yield metric

    metric = Metric('svc_hospital_message_types', 'Hospital Message Types', 'summary')
    for mesg_type in response['hospital_message_types']:
      for hkey, hval in mesg_type.iteritems():
        for mkey, mval in hval.iteritems():
          metric.add_sample('svc_hospital_message_types', value=mval.get('errors'), labels={'mesg_type':'errors', 'mode':mkey, 'hospital_name':hkey})
          metric.add_sample('svc_hospital_message_types', value=mval.get('messages'), labels={'mesg_type':'messages', 'mode':mkey, 'hospital_name':hkey})
          metric.add_sample('svc_hospital_message_types', value=mval.get('nonconsented'), labels={'mesg_type':'nonconsented', 'mode':mkey, 'hospital_name':hkey})
    yield metric

    timestamp = arrow.utcnow().timestamp

    metric = Metric('svc_timestamp_test', 'Time stamp data', 'gauge')
    metric.add_sample('svc_timestamp_test', value=timestamp, labels={})
    yield metric

if __name__ == '__main__':
  # Usage: json_exporter.py port endpoint
  start_http_server(int('1234'))
  REGISTRY.register(JsonCollector())
  print "started"

  while True:
    time.sleep(1)