from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:NRJrWXyzzcMQoLbFjTmNsKOVzVyaQqOw@kodama.proxy.rlwy.net:19550/railway"
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


