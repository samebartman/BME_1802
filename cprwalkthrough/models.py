from cprwalkthrough import db

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Video {}>'.format(self.filename)

class Audio(db.Model):
    __tablename__ = 'audio'
    id = db.Column(db.Integer, primary_key=True)
    audioname = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Audio {}>'.format(self.audioname)