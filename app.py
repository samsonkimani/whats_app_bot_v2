from flask import Flask, request
import json
import redis
from models.sessionmodel import *
from redis_om import Migrator
from utils.cab_menu import *
from utils.get_suggested_locations import getPlaceSuggestion
# from utils.send_message import send_message
from utils.ride_request import requestRide

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

Migrator().run()

# Fetching the menu json data
json_file_path = 'static/menu.json'
with open(json_file_path, 'r') as json_file:
    menu_json = json.load(json_file)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    incoming_message = request.get_json()
    print(incoming_message)

    if not incoming_message or incoming_message["type"] != "message":
        return "not a message"

    user_number = incoming_message["payload"]['sender']['phone']

    

    if RgetSession(user_number):
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

            if json_key == "BOOK-CAB" and RgetUserstep(user_number):
                state = "PICK-UP-LOCATION"
                RupdateSession(state, user_number)
                send_location()
                return ""

            # if json_key in ["BASIC", "COMFORT", "LADYBUG", "PARCEL"]:
            #     ha(user_number, json_key)

            # elif json_key == "PAYMENTS":
            #     handle_payment(user_number, json_key)

            # elif json_key == "CONFIRM-EXPRESS-WAY":
            #     handle_confirmation(user_number, json_key)

        except Exception as e:
            rsession = RgetSession(user_number)
            rsession.dict()
            json_key = rsession.dict()["state"]

        try:
            menu_instr = menu_json["menu"][json_key]
            state = menu_json["menu"][json_key]["id"]
            sub_menus(menu_instr)
            RupdateSession(state, user_number)

            if json_key == "BOOK":
                r = requestRide()
                print(r)
                if r["Status"] == "000":
                    try:
                        requestRide(user_number)
                        # trip_id(user_number, r["TripID"])
                        # driver_name(user_number, r["DriverName"], r["TimeDistance"], r["RoadDistance"])
                        # call(user_number, r["DriverMobileNumber"])
                        # cardetails(user_number, r["CarModel"], r["CarNumber"], r["CarColor"])
                        # driverPic(user_number, r["DriverPIC"])
                    except Exception as e:
                        print(f"Failed to process ride request response: {str(e)}")

        except Exception as e:
            rsession = RgetSession(user_number)
            rsession.dict()
            json_key = rsession.dict()["state"]
            menu_instr = menu_json["menu"][json_key]
            service_buttons(menu_instr)

    else:
        menu_instr = menu_json["menu"]["INITIAL-PAGE"]
        state = "INITIAL-PAGE"
        RsetSession(user_number, state)
        service_buttons(menu_instr)

    return ""

@app.route('/sendmessage', methods=['POST'])
def message():
    incoming_message = request.get_json()
    number = incoming_message["to"]
    message = incoming_message["text"]
    # send_message(number, message)
    return ""

if __name__ == '__main__':
    Migrator().run()
    app.run(debug=True)
