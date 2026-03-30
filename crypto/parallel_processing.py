from concurrent.futures import ThreadPoolExecutor

def parallel_calculation(function, data_dict):
    results = {}

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(function, value): key for key, value in data_dict.items()}

        for future in futures:
            key = futures[future]
            results[key] = future.result()

    return results