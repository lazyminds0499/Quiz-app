import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "easy"
}
# respond = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
respond = requests.get(url="https://opentdb.com/api.php", params=parameters)
ques = respond.json()
ques_data = ques["results"]