from .redis_om_s import RSession
import json

def RsetSession(phone, state):
    """
    Create a new session and set session TTL.
    """
    sess = RSession(
        phoneNumber=phone,
        state=state,
        stepsTakenByUser=state
    )
    sess.save()

def RgetSession(phoneNumber):
    """
    Check if session exists by searching using a phone number.
    """
    try:
        session = RSession.find(phoneNumber)
        if session:
            return session
        else:
            return False
    except Exception as e:
        session = f"There was an error in session retrieval: {str(e)}"
    return False

def RupdateSession(state, phoneNumber):
    """
    Update state and steps taken by the user in a session.
    """
    session = RSession.find(phoneNumber)
    if session:
        stepsTakenByUser = session.stepsTakenByUser + "," + state
        session.update(phoneNumber=phoneNumber, state=state, stepsTakenByUser=stepsTakenByUser)
        return session
    else:
        return "session not found"


def RdeleteSession(phoneNumber):
    """
    Delete a session.
    """
    session = RSession.find(RSession.phoneNumber == phoneNumber).first()
    if session:
        try:
            session.delete()
        except Exception as e:
            print(f"Error: {str(e)}")
            return {"successful": True, "message": f"Session for {phoneNumber} deleted successfully."}
    else:
        return {"successful": False, "reason": f"No session found for {phoneNumber}."}

def RgetUserstep(phoneNumber):
    """
    Check if the user is in the INITIAL-PAGE state.
    """
    try:
        session = RSession.find((RSession.phoneNumber == phoneNumber) & (RSession.state == "INITIAL-PAGE")).first()
        return True if session else False
    except Exception as e:
        print(str(e))
        return False

def RsaveUserCurrentLocation(phoneNumber, latitude, longitude):
    """
    Save the user's pickup location in terms of latitude and longitude.
    """
    session = RSession.find(phoneNumber)
    if session:
        session.update(phoneNumber=phoneNumber, latitude=latitude, longitude=longitude)
    else:
        return {"successful": False, "reason": "No session was found"}

def RsaveDropOfLocation(phoneNumber, location):
    """
    Save the user's typed drop-off location.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if session:
        session.dropoff_location = location
        session.save()
    else:
        return {"successful": False, "reason": "No session was found"}

def RchosenDropOffLocation(phoneNumber, location):
    """
    Save the user's chosen drop-off location from the suggested locations.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if session:
        session.chosenDropOffLocation = location
        session.save()
    else:
        return {"successful": False, "reason": "No session was found"}

def RsavePaymentMode(phoneNumber, mode):
    """
    Save the user's payment mode.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if session:
        session.paymentModes = mode
        session.save()
    else:
        return {"successful": False, "reason": "No session was found"}

def RgetCurrentUserState(phoneNumber):
    """
    Get the current state of the user.
    """
    session = RSession.find(phoneNumber)
    if session:
        return session.state
    else:
        return {"successful": False, "reason": "No session was found"}

def RsaveCard_mobile_obu_number(phoneNumber, num):
    """
    Save the user's card, mobile, or OBU number.
    """
    session = RSession.find(phoneNumber)
    if session:
        session.update(phoneNumber=phoneNumber, card_mobile_obu_number=num)
    else:
        return {"successful": False, "reason": "No session was found"}

def RgetUserDepartment(phoneNumber):
    """
    Check if the user has a corporate department.
    """
    try:
        session = RSession.find(phoneNumber)
        if session:
            return session.corporateDepartment
        return False
    except Exception as e:
        print("Error:", str(e))
        return False

def RgetUserDepartmentName(phoneNumber):
    """
    Get the name of the user's corporate department.
    """
    try:
        session = RSession.find(phoneNumber)
        if session:
            return session.corporateDepartment
        return False
    except Exception as e:
        print("Error:", str(e))
        return False

def RsaveCorporateDepartment(phoneNumber, dept):
    """
    Save the user's corporate department.
    """
    session = RSession.find(phoneNumber)
    if session:
        session.update(phoneNumber=phoneNumber, corporateDepartment=dept)
    else:
        return {"successful": False, "reason": "No session was found"}
