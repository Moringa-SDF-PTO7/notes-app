# id long, title text, description text, status enum (multi choice option)

from flask_sqlalchemy  import SQLAlchemy
import enum

db = SQLAlchemy()

class Status(enum.Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    COMPLETE = 3

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(db.Enum(Status), nullable=False, default='TO_DO')

    def __repr__(self):
        return f"<Note: {self.title}>"
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.name
        }

