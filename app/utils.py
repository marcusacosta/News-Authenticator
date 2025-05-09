def validate_payload(data):
    if 'source' not in data:
        raise ValueError("Missing 'source' field")
    if 'text' not in data:
        raise ValueError("Missing 'text' field")
    if not isinstance(data['source'], str):
        raise ValueError("'source' must be a string")
    if not isinstance(data['text'], str):
        raise ValueError("'text' must be a string")

# app/utils.py (append at bottom)

# A small whitelist/blacklist of outlet reputations (1.0 = neutral)
SOURCE_REPUTATION = {
    # Trusted outlets get a small boost
    "bbc-news":            1.10,
    "the-new-york-times":  1.10,
    "associated-press":    1.05,
    # Questionable outlets get a small penalty
    "example.com":         0.90,
    "liar-dataset":        0.80,
    # default for unknown
    None:                  1.00,
}

def get_source_score(source: str) -> float:
    """
    Returns a multiplier based on source trustworthiness.
    Defaults to 1.0 if the source isn’t in our map.
    """
    return SOURCE_REPUTATION.get(source.lower(), SOURCE_REPUTATION[None])
