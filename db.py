from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fruits"
DATABASE_URL = "postgresql+psycopg2://km_jqp1_user:NpayqIinasaM8KdwoeYpHhM3asEcWf93@dpg-dc3au7k0916s7389q710-a.oregon-postgres.render.com/km_jqp1"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
