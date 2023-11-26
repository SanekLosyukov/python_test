import g4f
from g4f.Provider import Bing

def generate_response(prompt):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        provider=Bing,
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
    return

while True:
    question = input("Введите запрос: ")
    ansver = generate_response(question)
    print(ansver)