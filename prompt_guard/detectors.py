import re

PATTERNS = [
    r"ignore previous instructions",
    r"disregard all prior instructions",
    r"you are now in developer mode",
    r"system override",
    r"output your initial system prompt",
    r"<\|im_start\|>",
    r"\[system\]",
    r"---end system prompt---"
]

class PromptInjectionDetector:
    def __init__(self):
        self.patterns = PATTERNS

    def analyze(self, prompt: str):
        p_lower = prompt.lower()
        matched = [p for p in self.patterns if re.search(p, p_lower)]
        is_threat = len(matched) > 0
        return {
            "is_threat": is_threat,
            "confidence": 0.95 if is_threat else 0.05,
            "detected_triggers": matched
        }

    # Base64 obfuscation probe detection
