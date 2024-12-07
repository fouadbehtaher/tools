from elasticsearch import Elasticsearch

def log_to_elasticsearch(data, index_name):
    es = Elasticsearch()
    es.index(index=index_name, document=data)
