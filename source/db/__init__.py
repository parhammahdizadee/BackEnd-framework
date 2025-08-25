from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,          # number of persistent connections
    max_overflow=20,       # extra connections beyond pool_size
    pool_timeout=30,       # seconds to wait for a free connection
    pool_recycle=1800,     # recycle connections every 30 mins
    pool_pre_ping=True     # test connection before using
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
