# this is a boolean search program written by Feras Alnehabi and Mohammed Alqifari
import json
import time

def tokenization(text):
    text = text.lower()
    punctuation = '.,!?;:"()[]{}'
    for char in punctuation:
        text = text.replace(char, ' ')
    return text.split()
    
def create_index(corpus):
    inverted_index = {}
    for doc_id, document in enumerate(corpus):
        words = tokenization(document)
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
    return inverted_index

def Boolean_Search(query, index):
    query = query.lower().strip()
    keywords = query.split()  # Space means OR
    matches = set()
    
    for keyword in keywords:
        if '&' in keyword:
            sub_keywords = keyword.split('&')
            if sub_keywords[0] in index:
                and_matches = set(index[sub_keywords[0]])
            else:
                and_matches = set()
                
            for sub in sub_keywords[1:]:
                and_matches = and_matches.intersection(set(index.get(sub, [])))
                
            matches = matches.union(and_matches)
        else:
            matches = matches.union(set(index.get(keyword, [])))
    
    return list(matches)

def load_dataset(file_path):
    corpus = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if "short_description" in data:
                        corpus.append(data["short_description"])
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print("File not found:", file_path)
    return corpus

def experiment(queries, index):
    timings = []
    for query in queries:
        start_time = time.perf_counter()
        search_results = Boolean_Search(query, index)
        end_time = time.perf_counter()
        timings.append({
            "query": query,
            "num_results": len(search_results),
            "time_microseconds": (end_time - start_time) *10**6
        })
    return timings

if __name__ == "__main__":
    data_collection = load_dataset("news.json")
    term_index = create_index(data_collection)
    
    sample_queries = [
        "king&salman",
        "football basketball",
        "iphone ipad",
        "artificial&intelligence",
        "covid vaccine"
    ]
    
    experiment_results = experiment(sample_queries, term_index)

    for result in experiment_results:
        print("Query: {}, Results: {}, Time: {:.2f} µs".format(
            result["query"], result["num_results"], result["time_microseconds"]))
