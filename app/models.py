from app import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.text('NOW()'))

    def __repr__(self):
        return f'<Conversation {self.id}>'