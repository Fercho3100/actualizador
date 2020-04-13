# coding: utf-8
from sqlalchemy import Column, DateTime, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TbSystemsPo(Base):
    __tablename__ = 'tb_systems_pos'

    id = Column(INTEGER(11), primary_key=True)
    ip = Column(String(15))
    codigo = Column(String(100), unique=True)
    licencia = Column(Text)
    fecha = Column(DateTime)
    lastconnection = Column(DateTime)
    cliente = Column(String(180))
    telefono = Column(String(8))
    email = Column(String(100))
    status = Column(TINYINT(4), server_default=text("'0'"))
    actualizar = Column(TINYINT(1), server_default=text("'0'"))
