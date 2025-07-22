from google import genai
from google.genai import types

client = genai.Client()

def Shortener(originalPrompt, maxLength):
    words = originalPrompt.split()
    if len(words) <= maxLength:
        return originalPrompt
    return ' '.join(words[:maxLength]) + '...'

def Preserver():
    features = ["context", "intent", "keywords", "tone"]
    preserved = [f for f in features if len(f) > 4]
    print(f"Preserved features: {preserved}")

def DetailAdder():
    enhancements = ["clarity", "specificity", "structure", "examples"]
    added = [e.upper() for e in enhancements if "i" in e]
    print(f"Added details: {added}")

class OptimizedPropmpt:
    def __init__(self, originalPropmt, optimizedPrompt, lengthReduced, preservedFeatures, addedDetails):
        self.originalPropmt = originalPropmt
        self.optimizedPrompt = optimizedPrompt
        self.lengthReduced = lengthReduced
        self.preservedFeatures = preservedFeatures
        self.addedDetails = addedDetails
    
    def preview(self):
        return f"Original: {self.originalPropmt}\nOptimized: {self.optimizedPrompt}\nLength Reduced: {self.lengthReduced}\nPreserved Features: {self.preservedFeatures}\nAdded Details: {self.addedDetails}"

class PromptStrategy:
    def __init__(self, model, contents):
        self.model = model
        self.contents = contents

    def optimize(self):
        shortened = Shortener(self.contents, 50)
        Preserver()
        DetailAdder()
        return OptimizedPropmpt(
            self.contents, 
            shortened, 
            len(self.contents.split()) - len(shortened.split()),
            ["important", "key", "critical"],
            ["efficient", "effective"]
        )



user_prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
    config=types.GenerateContentConfig(
    ),
)
print("AI Response:")
print(response.text)

print("\n" + "="*50)
print("Testing PromptStrategy:")

strategy = PromptStrategy("gemini-2.5-flash", user_prompt)
optimized = strategy.optimize()
print("\n" + optimized.preview())

print("\n" + "="*50)

optimized_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=optimized.optimizedPrompt,
    config=types.GenerateContentConfig(
    ),
)
print("Optimized Response:")
print(optimized_response.text)
