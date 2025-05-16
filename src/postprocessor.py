# src/postprocessor.py

def validate_output(entry: dict) -> dict:
    """
    Post-processes a single disclosure item to clean values,
    handle missing keys, and normalize confidence.
    """
    cleaned = {
        "answer": entry.get("answer", "Not found").strip(),
        "confidence_score": float(entry.get("confidence_score", 0)),
        "page_reference": entry.get("page_reference", "N/A")
    }

    # Clamp confidence score between 0 and 1
    cleaned["confidence_score"] = max(0.0, min(1.0, cleaned["confidence_score"]))

    # If answer is empty or vague
    if cleaned["answer"].lower() in ["", "not found", "n/a"]:
        cleaned["answer"] = "Not available"
        cleaned["confidence_score"] = 0.0

    return cleaned

def postprocess_all(raw_result: dict) -> dict:
    """
    Applies `validate_output()` to all extracted Q&A pairs.
    """
    processed = {}
    for question, entry in raw_result.items():
        try:
            # If entry is already a parsed dict
            if isinstance(entry, dict):
                processed[question] = validate_output(entry)
            else:
                # Fallback if it's a string
                processed[question] = validate_output({"answer": entry})
        except Exception as e:
            processed[question] = {
                "answer": f"Postprocessing error: {str(e)}",
                "confidence_score": 0,
                "page_reference": "N/A"
            }
    return processed
