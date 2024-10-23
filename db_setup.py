from sqlalchemy import create_engine, Column, String, Integer, text
from sqlalchemy.orm import declarative_base

server_name = "DESKTOP-O79B368\\SQLEXPRESS"
database_name = "master"

# MSSQL bağlantısı
mssql_db_url = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(mssql_db_url)
engine = engine.execution_options(isolation_level="AUTOCOMMIT")

# Veritabanının var olup olmadığını kontrol et
sql = text("SELECT name FROM sys.databases WHERE name = 'telefon_rehberi'")
with engine.connect() as connection:
    result = connection.execute(sql)
    if result.fetchone() is None:
        # Veritabanı yok, oluştur
        sql = text("CREATE DATABASE telefon_rehberi")
        connection.execute(sql)


# Veritabanı bağlantısını değiştir
database_name = "telefon_rehberi"
mssql_db_url = f"mssql+pyodbc://{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(mssql_db_url)

Base = declarative_base()

class Kisi(Base):
    __tablename__ = "rehber"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Surname = Column(String)
    Number = Column(String)
    Adress = Column(String)

Base.metadata.create_all(engine)
