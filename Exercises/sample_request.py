import requests
import json

if __name__ == '__main__':

    url = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2"

    response = requests.get(url)
    print(response)
    #response_json = json.loads(response.text)
    response_json = response.json()
    print(response_json)
    #mapped = (map(lambda fact: fact['text'], response_json))

    def map_response(fact):
        return fact['text']

    mapped = map(map_response, response_json)

    print(*mapped)
    #print(json.dumps(mapped))
