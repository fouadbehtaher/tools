import splunklib.client as client
import splunklib.results as results

def connect_to_splunk():
    service = client.connect(
        host='localhost', port=8089, username='admin', password='changeme'
    )
    return service

def search_splunk(query):
    service = connect_to_splunk()
    job = service.jobs.create(query)
    while not job.is_done():
        pass
    result = results.ResultsReader(job.results())
    return list(result)
