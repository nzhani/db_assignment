from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, Text, ForeignKey, Date, Time, Float
from sqlalchemy.exc import SQLAlchemyError

DB_URL = "postgresql://postgres:Admin@localhost:5432/ass_db"
engine = create_engine(DB_URL)
metadata = MetaData()

#Defininf tables
user_table = Table(
    'USER', metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('email', String(255), unique=True, nullable=False),
    Column('given_name', String(100), nullable=False),
    Column('surname', String(100), nullable=False),
    Column('city', String(100)),
    Column('phone_number', String(20)),
    Column('profile_description', Text),
    Column('password', String(255), nullable=False)
)

caregiver_table = Table(
    'caregiver', metadata,
    Column('caregiver_user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
    Column('photo', String(255)),
    Column('gender', String(50)),
    Column('caregiving_type', String(100)),
    Column('hourly_rate', Float)
)

member_table = Table(
    'member', metadata,
    Column('member_user_id', Integer, ForeignKey('user.user_id'), primary_key=True),
    Column('house_rules', Text),
    Column('dependent_description', Text)
)

address_table = Table(
    'address', metadata,
    Column('member_user_id', Integer, ForeignKey('member.member_user_id'), primary_key=True),
    Column('house_number', String(50)),
    Column('street', String(255)),
    Column('town', String(100))
)

job_table = Table(
    'job', metadata,
    Column('job_id', Integer, primary_key=True, autoincrement=True),
    Column('member_user_id', Integer, ForeignKey('member.member_user_id'), nullable=False),
    Column('required_caregiving_type', String(100)),
    Column('other_requirements', Text),
    Column('date_posted', Date)
)

job_application_table = Table(
    'job_application', metadata,
    Column('caregiver_user_id', Integer, ForeignKey('caregiver.caregiver_user_id'), primary_key=True),
    Column('job_id', Integer, ForeignKey('job.job_id'), primary_key=True),
    Column('date_applied', Date)
)

appointment_table = Table(
    'appointment', metadata,
    Column('appointment_id', Integer, primary_key=True, autoincrement=True),
    Column('caregiver_user_id', Integer, ForeignKey('caregiver.caregiver_user_id'), nullable=False),
    Column('member_user_id', Integer, ForeignKey('member.member_user_id'), nullable=False),
    Column('appointment_date', Date),
    Column('appointment_time', Time),
    Column('work_hours', Integer),
    Column('status', String(50))
)
# functions to   use in app.py
def q(sql, p=None):
    try:
        with engine.connect() as c:
            r = c.execute(text(sql), p or {})
            c.commit()
            if r.returns_rows:
                return r.fetchall()
            return None
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        return None

def get_all(table_obj):
    with engine.connect() as conn:
        result = conn.execute(table_obj.select())
        return result.fetchall()

def get_by_id(table_obj, id_col, id_val):
    with engine.connect() as conn:
        result = conn.execute(table_obj.select().where(id_col == id_val))
        return result.fetchone()

def create_record(table_obj, data):
    with engine.connect() as conn:
        result = conn.execute(table_obj.insert().values(**data))
        conn.commit()
        return result

def update_record(table_obj, id_col, id_val, data):
    with engine.connect() as conn:
        result = conn.execute(table_obj.update().where(id_col == id_val).values(**data))
        conn.commit()
        return result

def delete_record(table_obj, id_col, id_val):
    with engine.connect() as conn:
        result = conn.execute(table_obj.delete().where(id_col == id_val))
        conn.commit()
        return result
