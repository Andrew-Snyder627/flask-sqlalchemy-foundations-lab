from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here


class Earthquake(db.Model):
    __tablename__ = "earthquakes"  # Names the table

    # Sets the columns
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

# Readable Output
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
