import gzip
import json

path = 'jawiki-country.json.gz' 

def load():
    with gzip.open(path, 'rt') as f:
        for l in f:
            data = json.loads(l)
            if data['title'] == 'イギリス':
                return data['text']

if __name__ == "__main__":
    print(load())