from typing import Optional

BILLING_KEY = ["payment", "card", "refund", "charged", "invoice", "billing"]
TECH_KEY = ["error", "crash", "bug", "not working", "issue", "fail"]
ACCOUNT_KEY = ["login", "password", "account", "username", "sign in", "sign out"]

def infer_topic(text: Optional[str]) -> Optional[str]:
    if text is None:
        return None
    lower = text.lower()
    if any(k in lower for k in BILLING_KEY):
        return "billing"
    if any(k in lower for k in TECH_KEY):
        return "tech"
    if any(k in lower for k in ACCOUNT_KEY):
        return "account"
    return "other"

NEGATIVE_WORDS = ["angry", "upset", "ridiculous", "terrible", "horrible",
                  "worst", "unacceptable"]
POSITIVE_WORDS = ["positive", "acceptable", "good", "great", "thank you",
                  "love", "awesome"]

def infer_sentiment(text: Optional[str]) -> Optional[str]:
    if text is None:
        return None
    lower = text.lower()
    if any(w in lower for w in POSITIVE_WORDS):
        return "positive"
    if any(w in lower for w in NEGATIVE_WORDS):
        return "negative"
    return "neutral"

def urgency(text: Optional[str], sentiment: Optional[str]) -> Optional[float]:
    if text is None:
        return None
    score = 0.0
    lower = text.lower()
    if any(w in lower for w in ["urgent", "asap", "immediately", "now"]):
        score += 0.5
    if sentiment == "negative":
        score += 0.3
    return min(score, 1.0)

def priority(urgency: Optional[float]) -> str:
    if urgency is None:
        return "medium"
    if urgency >= 0.7:
        return "high"
    if urgency >= 0.3:
        return "medium"
    return "low"