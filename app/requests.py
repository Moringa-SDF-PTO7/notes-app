from flask import Flask, render_template, jsonify, request
from models import Note, db

def register_routes(app: Flask):

    # Home route
    @app.route('/')
    def index():
        return render_template("index.html")
    
    # show notes
    @app.route("/notes", methods=['GET'])
    def get_notes():
        notes = Note.query.all()
        return jsonify(
            [ n.to_json() for n in notes ]
        )
    
    # create new note
    @app.route("/note", methods=['POST'])
    def create_note():
        data = request.json
        title = data.get('title')
        description = data.get("description")

        if len(str(title)) < 1:
            return jsonify({
                'message': "Title can not be blank"
            }), 422

        new_note = Note(title = title, description = description)
        db.session.add(new_note)
        db.session.commit()
        return jsonify({
            'message': "Added note successfully"
            }), 201
    
    # update note
    @app.route('/note/<int:id>', methods=['PUT', 'PATCH'])
    def update_note(id):
        data = request.json
        note = Note.query.get_or_404(id)
        title = data.get("title")
        description = data.get("description")
        status = data.get("status")

        if title:
            note.title = title

        if description:
            note.description = description

        if status:
            note.status = status

        db.session.commit()
        return jsonify({
            'message': f'Note with id: {id} has been updated.'
        })
    
    # delete note
    @app.route('/note/<int:id>', methods=['DELETE'])
    def delete_note(id):
        note = Note.query.get_or_404(id)
        db.session.delete(note)
        db.session.commit()
        return jsonify({
            'message': f'Note with id: {id} has been deleted.'
        })

