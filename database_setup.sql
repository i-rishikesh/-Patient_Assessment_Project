CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    gender VARCHAR(10),
    phone VARCHAR(20),
    medical_history TEXT[]
);
