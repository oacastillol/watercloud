from flask import request, json, Response, Blueprint, g, escape
from marshmallow import ValidationError
from ..models.SampleModel import SampleModel, SampleSchema
from re import match
from datetime import datetime, timedelta
import pytz
sample_api = Blueprint('samples', __name__)
sample_schema = SampleSchema()


@sample_api.route('/', methods=['POST'])
@sample_api.route('', methods=['POST'])
def create():
    req_data = request.get_json()
    model = {}
    rowid = req_data['rowid']
    model['device'] = req_data['device']
    model['sensores'] = json.loads(req_data['info'])
    model['created_at'] = model['sensores']['create_date']
#    tzone = pytz.timezone('America/Bogota')
#    model['created_at'] = tzone.localize(model['created_at'])
    del(model['sensores']['create_date'])
    del(model['sensores']['node'])
    model['sensores'] = json.dumps(model['sensores'])
    model['recepted_at'] = datetime.now().isoformat()
    try:
        data = sample_schema.load(model)
    except ValidationError as err:
        print(err.messages)
        print(err.valid_data)
        return custom_response(err.messages, 200)
    else:
        sample = SampleModel(data)
        sample.save()
        return custom_response(rowid, 201)


@sample_api.route('/', methods=['GET'])
@sample_api.route('', methods=['GET'])
def list():
    samples = SampleModel.get_all_samples()
    for sample in samples:
        sample.created_at = sample.created_at - timedelta(hours=5)
        sample.recepted_at = sample.recepted_at - timedelta(hours=5)
    data = sample_schema.dump(samples, many=True)
    for e in data:
        e['sensores'] = json.loads(e['sensores'])
    return custom_response(data, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
