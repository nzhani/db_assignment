from db_logic import (
    user_table, caregiver_table, member_table, address_table, job_table, job_application_table, appointment_table,
    get_all
)

def test_tables():
    tables = {
        'User': user_table,
        'Caregiver': caregiver_table,
        'Member': member_table,
        'Address': address_table,
        'Job': job_table,
        'Job Application': job_application_table,
        'Appointment': appointment_table
    }

    for name, table in tables.items():
        try:
            print(f"Testing {name}...")
            results = get_all(table)
            print(f"  Success! Found {len(results)} records.")
        except Exception as e:
            print(f"  FAILED: {e}")

if __name__ == "__main__":
    test_tables()
