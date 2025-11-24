from sqlalchemy import create_engine, inspect, text

DB_URL = "postgresql://postgres:Admin@localhost:5432/ass_db"
engine = create_engine(DB_URL)

def inspect_db():
    try:
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        print(f"Tables found: {table_names}")
        
        for table in table_names:
            print(f"\nTable: {table}")
            columns = inspector.get_columns(table)
            for col in columns:
                print(f"  - {col['name']} ({col['type']})")
                
    except Exception as e:
        print(f"Error inspecting DB: {e}")

if __name__ == "__main__":
    inspect_db() #fuck nameing commit
