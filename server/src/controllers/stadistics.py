from main import app
from bson.json_util import dumps, loads
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repository.stadistics_repository import find


@app.get('/stadistics', status_code=200)
async def root():
    stadistics = find({}, {'_id': 0})
    return [stadistic for stadistic in list(stadistics)]
