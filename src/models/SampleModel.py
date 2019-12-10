from marshmallow import fields, Schema
from . import db
from sqlalchemy import distinct


class SampleModel(db.Model):
    """
    Modelo de muestra de sensores
    """
    __tablename__ = "samples"

    id = db.Column(db.Integer, primary_key=True)
    # db.ForeignKey('devices.num'),
    device = db.Column(db.Integer, nullable=False)
    sensores = db.Column(db.JSON)
    created_at = db.Column(db.DateTime)
    recepted_at = db.Column(db.DateTime)

    def __init__(self, data):
        """
        Class constructor
        """
        self.device = data.get('device')
        self.sensores = data.get('sensores')
        self.created_at = data.get('created_at')
        self.recepted_at = data.get('recepted_at')

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_samples():
        return SampleModel.query.all()

    @staticmethod
    def get_one_sample(id):
        return SampleModel.query.get(id)

    @staticmethod
    def get_samples_by_device(value):
        return SampleModel.query.filter_by(device=value).all()

    @staticmethod
    def get_devices():
        return SampleModel.query.distinct(SampleModel.device).all()

    def __repr(self):
        return '<id {}>'.format(self.id)


class SampleSchema(Schema):
    """
    Sample Schema
    """
    id = fields.Int(dump_only=True)
    device = fields.Int()
    sensores = fields.Raw()
    created_at = fields.DateTime()
    recepted_at = fields.DateTime()
