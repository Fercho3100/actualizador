from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("conf.env", "r") as dicc:
    for line in dicc:
        if 'NUMLICENCIA' in line:
            explode_licencia = line.strip().split("<=>")
            licencia = explode_licencia[1]
        if 'LICENCIADOR' in line:
            explode_path = line.strip().split("<=>")
            codvendedor = explode_path[1]

db_uri_metr =  'postgresql+psycopg2://' + user + ':' + pass_decryp + '@' + host + ':' + port + '/' + db
engine_metr = create_engine(db_uri_metr)
Session_Metr = sessionmaker(bind=engine_metr)
base_Metr = declarative_base()