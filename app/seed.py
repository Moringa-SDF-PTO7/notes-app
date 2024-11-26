from app import db,app
from models import Note

def seed_data():
    notes = [
        { 'title': "Task uno", 'description': "This is the 1st task." },
        { 'title': "Task dos", 'description': "This is the 2nd task." },
        { 'title': "Task tres", 'description': "This is the 3rd task." },
    ]
    for note in notes:
        db.session.add(
            Note(title = note['title'], description = note['description'])
        )
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        print("Starting Data Seed ...")
        seed_data()
        print("Seeding Complete")
