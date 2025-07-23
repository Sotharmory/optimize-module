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
