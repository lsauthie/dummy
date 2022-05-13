from sqlalchemy import Column, String, Float, Integer
from base import Base

class Swissre(Base):
    __tablename__ = 'swissre'

    id = Column(Integer, primary_key=True)
    reference = Column(String(120), nullable=False)
    sentence = Column(String(120))
    ratio = Column(Float)

    def __init__(self, reference, sentence, ratio):
        self.reference = reference
        self.sentence = sentence
        self.ratio = ratio