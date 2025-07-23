from client import get_client, generate_response
from strategy import PromptStrategy

client = get_client()

user_prompt = input("Enter your prompt: ")

response = generate_response(client, user_prompt)
print("AI Response:")
print(response)

print("\n" + "="*50)
print("Testing PromptStrategy:")

strategy = PromptStrategy("gemini-2.5-flash", user_prompt)
optimized = strategy.optimize()
print("\n" + optimized.preview())

print("\n" + "="*50)

optimized_response = generate_response(client, optimized.optimizedPrompt)
print("Optimized Response:")
print(optimized_response)
