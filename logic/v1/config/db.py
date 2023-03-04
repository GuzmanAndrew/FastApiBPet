from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:Software9525*@database-bpet.csro2nol6a13.us-east-1.rds.amazonaws.com:3306/bpet_db")

meta = MetaData()

conn = engine.connect()