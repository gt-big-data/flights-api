import opensky
from time import time
from json import dumps

def planes(request):

    time = time()
    icao24 = None
    bounding_box = ()

    if "time" in request.args:
        time = request.args.get("time")
    if "icao24" in request.args:
        icao24 = request.args.get("icao24")
    if "bbox" in request.args:
        bbox = tuple(request.args.get("bbox").split(','))
    
    return dumps(opensky.planes(time, icao24, bbox))