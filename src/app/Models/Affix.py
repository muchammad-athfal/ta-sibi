from ...config.database import db, BaseModel
from flask import url_for

class Affix(BaseModel):
    __tablename__ = 'affixes'

    #table columns
    name = db.Column(db.String(255), nullable=False)
    slug_name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    video_link = db.Column(db.Text(), nullable=False)
    
    #constructor
    # def __init__(self, parent_id=None, email=None, password=None):
    #     self.name = name
    #     self.email = email
    #     self.authenticated = True
    
    def jsonResponse(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'video_link': self.video_link
        }