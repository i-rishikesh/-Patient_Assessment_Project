import psycopg2
import json
from parse_ocr_data import parse_text

def store_data_in_db(text):
    """Insert extracted JSON data into PostgreSQL database."""
    json_data = parse_text(text)

    conn = psycopg2.connect(
        dbname="patient_data",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Extract patient details
    data = json.loads(json_data)
    cur.execute("INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id;",
                (data["patient_name"], data["dob"]))
    patient_id = cur.fetchone()[0]

    # Insert form data
    cur.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
                (patient_id, json_data))
    
    conn.commit()
    cur.close()
    conn.close()

    print("Data stored successfully!")

# Test database storage
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

    store_data_in_db(sample_text)
