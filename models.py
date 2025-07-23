class OptimizedPropmpt:
    def __init__(self, originalPropmt, optimizedPrompt, lengthReduced, preservedFeatures, addedDetails):
        self.originalPropmt = originalPropmt
        self.optimizedPrompt = optimizedPrompt
        self.lengthReduced = lengthReduced
        self.preservedFeatures = preservedFeatures
        self.addedDetails = addedDetails
    
    def preview(self):
        return f"Original: {self.originalPropmt}\nOptimized: {self.optimizedPrompt}\nLength Reduced: {self.lengthReduced}\nPreserved Features: {self.preservedFeatures}\nAdded Details: {self.addedDetails}"
