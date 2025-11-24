1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    ```bash
    flask run
    ```

3.  **Access the App**:
    Open your browser and navigate to `http://127.0.0.1:5000`.

## Database
The application uses a PostgreSQL database. Ensure your database is running and the connection string in `db_logic.py` is correct:
`postgresql://postgres:Admin@localhost:5432/ass_db`

## Features
- CRUD operations for User, Caregiver, Member, Address, Job, Job Application, and Appointment.
- Simple interface using Bootstrap.
