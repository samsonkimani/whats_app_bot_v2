from models.redis_om_s import RSession
import json
from models.sessionmodel import *
from utils.cab_menu import *
from .get_suggested_locations import *


class Handler:

    def __init__(self) -> None:
        pass

    def handleLocations(self, incoming_message, user_number):
        latitude = incoming_message["payload"]["payload"]["latitude"]
        longitude = incoming_message["payload"]["payload"]["longitude"]
        state = "DROP-OFF-LOCATION"
        session = RgetSession(user_number)
        stepTakenByUser = session.stepsTakenByUser + "," + state
        session.update(phoneNumber=user_number, state=state, stepTakenByUser=stepTakenByUser ,latitude=latitude, longitude=longitude)        
        locaton = getPlaceSuggestion("kilimani")
        suggested_location_menus(locaton, user_number)
        session = RgetSession(user_number)
        return ""
    
    
