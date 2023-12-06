from flask import Flask, request
import json
from models.sessionmodel import *
from utils.cab_menu import *
from utils.get_suggested_locations import *
from utils.handlers import Handler


app = Flask(__name__)


# Fetching the menu json data
json_file_path = 'static/menu.json'
with open(json_file_path, 'r') as json_file:
    menu_json = json.load(json_file)

Handler = Handler()

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    incoming_message = request.get_json()
    print(incoming_message)

    if not incoming_message or incoming_message["type"] != "message":
        return "not a message"

    user_number = incoming_message["payload"]['sender']['phone']

    if incoming_message["payload"]["type"] == "location" and RgetSession(user_number).state == "BOOK-CAB":
        Handler.handleDropOffLocations(incoming_message, user_number)
        return "" 
       
    if incoming_message["payload"]["type"] == "location" and RgetSession(user_number).state == "DROP-OFF-LOCATION":
        Handler.handleCabOptions(menu_json)
        return ""
    
    session = RgetSession(user_number)
    if session:
        # return "session exists"
        try:
            raw_option = incoming_message["payload"]["payload"]["title"]
            json_key = raw_option.strip().replace(" ", "-").upper()


            if json_key == "GO-BACK-TO-MAIN-MENU":
                RdeleteSession(user_number)
                menu_instr = menu_json["menu"]["INITIAL-PAGE"]
                state = "INITIAL-PAGE"
                RsetSession(user_number, state)
                service_buttons(menu_instr)
                return ""
            
            if json_key == "BOOK":
                state = "BOOK"
                RupdateSession(state, user_number)
                Handler.handleBooking(menu_json["menu"]["BOOK"], user_number)
                return ""
            
            if json_key == "DECLINE":
                state = "DECLINE"
                RupdateSession(state, user_number)
                Handler.handleDecline(menu_json["menu"]["DECLINE"], user_number)

            if json_key == "BOOK-CAB":
                state = "BOOK-CAB"
                RupdateSession(state, user_number)
                providePickUpLocation()
                return ""    

            if json_key in ["BASIC", "COMFORT", "LADYBUG", "PARCEL"]:
                state = json_key
                RupdateSession(state, user_number)
                Handler.handleSpecificCab(menu_json["menu"][json_key])
                return ""
            
                

            if json_key == "MOJA-EXPRESS":
                state = "MOJA-EXPRESS"
                RupdateSession(state, user_number)
                Handler.handleMojaExpressMenu(menu_json["menu"]["MOJA-EXPRESS"])
                return ""
            if json_key == "MTC":
                state = "MTC"
                RupdateSession(state, user_number)
                Handler.handleMojaExpressMenu(menu_json["menu"]["MTC"])
                return ""
            if json_key == "ETC":
                state = "ETC"
                RupdateSession(state, user_number)
                Handler.handleMojaExpressMenu(menu_json["menu"]["ETC"])
                return ""
            
            if json_key == "TICKETS":
                state = "TICKETS"
                RupdateSession(state, user_number)
                Handler.handleSubMenus(menu_json["menu"]["TICKETS"])
                return ""
            
            if json_key == "LITTLE_EVENTS":
                state = "LITTLE_EVENTS"
                RupdateSession(state, user_number)
                Handler.handleSubMenus(menu_json["menu"]["LITTLE_EVENTS"])
                return ""
            

            

    

            # elif json_key == "CONFIRM-EXPRESS-WAY":
            #     handle_confirmation(user_number, json_key)

        except Exception as e:
            rsession = RgetSession(user_number)
            json_key = rsession.state


    else:
        menu_instr = menu_json["menu"]["INITIAL-PAGE"]
        state = "INITIAL-PAGE"
        RsetSession(user_number, state)
        service_buttons(menu_instr)

    return ""

if __name__ == '__main__':
    app.run(debug=True)
