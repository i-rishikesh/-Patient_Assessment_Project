import re
import json

def parse_text(text):
    """Parse extracted text to JSON format."""
    data = {}

    # Extract patient details
    name_match = re.search(r"Name:\s*(.*)", text)
    dob_match = re.search(r"DOB:\s*(\d{2}/\d{2}/\d{4})", text)
    date_match = re.search(r"Date:\s*(\d{2}/\d{2}/\d{4})", text)

    if name_match: data["patient_name"] = name_match.group(1).strip()
    if dob_match: data["dob"] = dob_match.group(1).strip()
    if date_match: data["date"] = date_match.group(1).strip()

    # Extract yes/no fields
    data["injection"] = "Yes" if "Injection: Yes" in text else "No"
    data["exercise_therapy"] = "Yes" if "Exercise Therapy: Yes" in text else "No"

    # Extract difficulty ratings
    difficulty_ratings = {}
    for activity in ["bending", "putting on shoes", "sleeping"]:
        match = re.search(rf"{activity.capitalize()}:\s*(\d)", text)
        if match:
            difficulty_ratings[activity] = int(match.group(1))

    data["difficulty_ratings"] = difficulty_ratings

    # Extract pain symptoms
    pain_symptoms = {}
    for symptom in ["pain", "numbness", "tingling", "burning", "tightness"]:
        match = re.search(rf"{symptom.capitalize()}:\s*(\d+)", text)
        if match:
            pain_symptoms[symptom] = int(match.group(1))

    data["pain_symptoms"] = pain_symptoms

    return json.dumps(data, indent=4)

# Test parsing
if __name__ == "__main__":
    sample_text = """Name: John Doe
    DOB: 01/05/1988
    Date: 02/06/2025
    Injection: Yes
    Exercise Therapy: No
    Bending: 3
    Putting on Shoes: 1
    Sleeping: 2
    Pain: 2
    Numbness: 5
    Tingling: 6
    """
    
    parsed_json = parse_text(sample_text)
    print(parsed_json)
