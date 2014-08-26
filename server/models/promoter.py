from .. import db


class Promoter(db.Model):
    """
    Model for promoters.
    """
    __tablename__ = 'promoters'

    promoter_id = db.Column(db.Integer, primary_key=True)
    promoter_name = db.Column(db.String, unique=True)