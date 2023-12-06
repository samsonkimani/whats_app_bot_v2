from models.redis_om_s import RSession
import time
from models.sessionmodel import *
from utils.cab_menu import *
from .get_suggested_locations import *
from .ride_request import *


class Handler:

    def __init__(self) -> None:
        pass

    def handleLocations(self, incoming_message, user_number):
        latitude = incoming_message["payload"]["payload"]["latitude"]
        longitude = incoming_message["payload"]["payload"]["longitude"]
        state = "PICK-UP-LOCATION"
        session = RgetSession(user_number)
        stepTakenByUser = session.stepsTakenByUser + "," + state
        session.update(phoneNumber=user_number, state=state, stepTakenByUser=stepTakenByUser ,latitude=latitude, longitude=longitude)
        providePickUpLocation()
        return ""
    
    def handleDropOffLocations(self, incoming_message, user_number):
        longitude = incoming_message["payload"]["payload"]["longitude"]
        latitude = incoming_message["payload"]["payload"]["latitude"]
        state = "DROP-OFF-LOCATION"
        session = RgetSession(user_number)
        stepTakenByUser = session.stepsTakenByUser + "," + state
        session.update(phoneNumber=user_number, state=state, stepTakenByUser=stepTakenByUser ,latitude=latitude, longitude=longitude)
        provide_destination()
        return ""
    
    def handleCabOptions(self, json_menu):
        sub_menus(json_menu["menu"]["BOOK-CAB"])
        return ""
    
    def handleSpecificCab(self, json_menu):
        sub_menus(json_menu)
        return ""
    
    def handleDecline(self, json_menu, user_number):
        sendDeclineCabtext(json_menu)
        RdeleteSession(user_number)
        return ""
    
    def handleBooking(self, json_menu, user_number):
        sendBookCabtext(json_menu)
        # time.sleep(5)
        r = requestRide()
        trip_id(user_number,r["TripID"])
        driver_name(user_number,r["DriverName"],r["TimeDistance"],r["RoadDistance"])
        call(user_number,r["DriverMobileNumber"])
        cardetails(user_number,r["CarModel"],r["CarNumber"],r["CarColor"])
        driverPic(user_number,r["DriverPIC"])
        time.sleep(5)
        RdeleteSession(user_number)
        return ""
    
    def handleMojaExpressMenu(self, json_menu):
        sub_menus(json_menu)
        return ""
    
    def handleSubMenus(self, json_menu):
        sub_menus(json_menu)
        return ""

        


    
    
