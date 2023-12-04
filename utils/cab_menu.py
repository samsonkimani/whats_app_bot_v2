import json
import requests
from models.sessionmodel import RupdateSession

url = "https://api.gupshup.io/wa/api/v1/msg"

headers = {
    "apikey": "5dwlwmv39a17qr09blov5ciq4mzat5lu",
    "Content-Type": "application/x-www-form-urlencoded",
}

def send_whatsapp_message(data):
    """
    Helper function to send WhatsApp messages.
    """
    response = requests.post(url, headers=headers, data=data)
    return response.status_code, response.json()

def service_buttons(initial_page_json):
    """
    Display the main menu with service buttons.
    """
    options = [{"type": "text", "title": value[4:], "description": ""} for value in initial_page_json["options"].values()]
    menu_title = "Menu" if initial_page_json["text"] != "Welcome to Little. Ride a Little Better.\n" else "Main Menu"
    back_to_main_menu = {"type": "text", "title": "Go back to main menu", "description": ""}
    options.append(back_to_main_menu)
    menu = {
        "type": "list",
        "title": "Little",
        "body": initial_page_json["text"],
        "globalButtons": [{"type": "text", "title": menu_title}],
        "items": [{"title": "Services", "subtitle": "Services", "options": options}]
    }
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": json.dumps(menu),
        "src.name": "jkclassics",
    }
    return send_whatsapp_message(data)

def sub_menus(menu_json):
    """
    Display submenus from the menu JSON.
    """
    options = [{"type": "text", "title": value[4:], "description": ""} for value in menu_json["options"].values()]
    back_to_main_menu = {"type": "text", "title": "Go back to main menu", "description": ""}
    options.append(back_to_main_menu)
    submenu = {
        "type": "list",
        "title": "Little",
        "body": menu_json["text"],
        "globalButtons": [{"type": "text", "title": "Menu"}],
        "items": [{"title": "Services", "subtitle": "Services", "options": options}]
    }
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": json.dumps(submenu),
        "src.name": "jkclassics",
    }
    return send_whatsapp_message(data)

def suggested_location_menus(locations, user_number):
    """
    Display the suggested location menu.
    """
    options = [{"type": "text", "title": str(index + 1), "description": f"{location['description']} , {location['state']}"} for index, location in enumerate(locations)]
    back_to_main_menu = {"type": "text", "title": "Go back to main menu", "description": ""}
    options.append(back_to_main_menu)
    menu = {
        "type": "list",
        "title": "Little",
        "body": "Choose Drop-off Location from suggested Locations",
        "globalButtons": [{"type": "text", "title": "Menu"}],
        "items": [{"title": "Services", "subtitle": "Services", "options": options}]
    }
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": json.dumps(menu),
        "src.name": "jkclassics",
    }
    response_status_code = send_whatsapp_message(data)
    if response_status_code == 200:
        RupdateSession("SUGGESTED-LOCATION", user_number)
    return response_status_code

def send_location():
    """
    Display the menu used to get the current user location.
    """
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": '{"type":"location_request_message","body":{"type":"text","text":"Where would you like to be picked?"},"action":{"name":"send_location"}}',
        "src.name": "jkclassics",
    }
    return send_whatsapp_message(data)

def provide_payment_mode():
    """
    Display the menu used to get the user's payment mode.
    """
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": '{"type":"text","text":"How would you like to pay for your ride?","quick_reply":{"type":"options","options":[{"type":"text","title":"Cash","description":""},{"type":"text","title":"M-Pesa","description":""},{"type":"text","title":"Card","description":""}]}}',
        "src.name": "jkclassics",
    }
    return send_whatsapp_message(data)

def provide_card_number():
    """
    Display the menu used to get the user's card number.
    """
    data = {
        "channel": "whatsapp",
        "source": "254775895174",
        "destination": "254727499710",
        "message": '{"type":"text","text":"Please enter your card number"}',
        "src.name": "jkclassics",
    }
    return send_whatsapp_message(data)

