import os
from time import time

from dotenv import load_dotenv

from opensky_api import OpenSkyApi

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

USER = os.getenv("OPENSKY_USERNAME")
PASS = os.getenv("OPENSKY_PASSWORD")

api = OpenSkyApi(USER, PASS)

def _translate_position_source(position_source):

    if position_source == 0:
        return "ADS-B"
    elif position_source == 1:
        return "ASTERIX"
    elif position_source == 2:
        return "MLAT"
    elif position_source == 3:
        return "FLARM"
    else:
        raise ValueError("Couldn't identify position source")

def planes(time=time(), icao24=None, bounding_box=()):

    response = api.get_states(time_secs=time, icao24=icao24, bbox=bounding_box)

    states = []

    # https://opensky-network.org/apidoc/python.html#opensky_api.StateVector
    for state in response.states:

        states.append({
            "icao24": state.icao24,
            "callsign": state.callsign,
            "originCountry": state.origin_country,
            "lastSeen": state.time_position,
            "timeSinceLastSeen": state.last_contact,
            "longitude": state.longitude,
            "latitide": state.latitude,
            "geometricAltitude": state.geo_altitude,
            "barometricAltitude": state.baro_altitude,
            "grounded": state.on_ground,
            "speed": state.velocity,
            "heading": state.heading,
            "squawkCode": state.squawk,
            "positionSource": _translate_position_source(state.position_source)
        })
    
    return states