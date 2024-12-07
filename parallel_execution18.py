import dask
from dask import delayed, compute
import ray

@delayed
def process_data(data_chunk):
    return sum(data_chunk)

def process_large_dataset(data):
    data_chunks = [data[i:i + 1000] for i in range(0, len(data), 1000)]
    results = compute(*[process_data(chunk) for chunk in data_chunks])
    return sum(results)

ray.init(ignore_reinit_error=True)

@ray.remote
def process_data_ray(data_chunk):
    return sum(data_chunk)

def process_large_dataset_ray(data):
    data_chunks = [data[i:i + 1000] for i in range(0, len(data), 1000)]
    results = ray.get([process_data_ray.remote(chunk) for chunk in data_chunks])
    return sum(results)
