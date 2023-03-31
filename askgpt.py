import openai

def ask_gpt(query):
# query = " What's the biggest difference between a champion, formula one driver and all the others?"

    # example with a system message
    MODEL = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You must answer concisely as a helpful assistant."},
            {"role": "user", "content": query},
        ],
        temperature=0,
    )
    gpt_response = response['choices'][0]['message']['content']
    print(gpt_response)

    return gpt_response
