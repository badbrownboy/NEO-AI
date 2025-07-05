import openai
from voice import listen, speak
from actions import perform_action
from memory import remember, recall

openai.api_key = "your-api-key"

def interpret_command(command):
    prompt = f"You are an AI that controls a computer like a human. The user said: {command}. What should you do?"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

while True:
    command = listen()
    speak(f"You said: {command}")
    plan = interpret_command(command)
    speak(f"Understood. I'll: {plan}")
    remember(command, plan)
    perform_action(plan)
