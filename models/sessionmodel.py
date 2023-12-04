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
    RSession.db().expire(sess.key(), 500)

def RgetSession(phoneNumber):
    """
    Check if session exists by searching using a phone number.
    """
    try:
        session = RSession.find(RSession.phoneNumber == phoneNumber).first()
    except Exception as e:
        session = None
    return "session available" if session else "no session"

def RupdateSession(state, phoneNumber):
    """
    Update state and steps taken by the user in a session.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.state = state
    session.stepsTakenByUser = f"{session.stepsTakenByUser}.{state}"
    session.save()
    return json.loads(session.json())

def RdeleteSession(phoneNumber):
    """
    Delete a session.
    """
    session = RSession.find(RSession.phoneNumber == phoneNumber).first()
    if session:
        try:
            sess_key = session.key()
            pk = sess_key[30:]
            session.delete(pk)
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
        return True
    except Exception as e:
        print(str(e))
        return False

def RsaveUserCurrentLocation(phoneNumber, latitude, longitude):
    """
    Save the user's pickup location in terms of latitude and longitude.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.longitude = longitude
    session.latitude = latitude
    session.save()

def RsaveDropOfLocation(phoneNumber, location):
    """
    Save the user's typed drop-off location.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.dropoff_location = location
    session.save()

def RchosenDropOffLocation(phoneNumber, location):
    """
    Save the user's chosen drop-off location from the suggested locations.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.chosenDropOffLocation = location
    session.save()

def RsavePaymentMode(phoneNumber, mode):
    """
    Save the user's payment mode.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.paymentModes = mode
    session.save()

def RgetCurrentUserState(phoneNumber):
    """
    Get the current state of the user.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    return session.state

def RsaveCard_mobile_obu_number(phoneNumber, num):
    """
    Save the user's card, mobile, or OBU number.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.card_mobile_obu_number = num
    session.save()

def RgetUserDepartment(phoneNumber):
    """
    Check if the user has a corporate department.
    """
    try:
        session = RSession.find((RSession.phoneNumber == phoneNumber) & (RSession.state == "STAFF-ATTENDANCE")).first()

        if session.corporateDepartment is not None:
            return False
        else:
            return True

    except Exception as e:
        print("Error:", str(e))
        return False

def RgetUserDepartmentName(phoneNumber):
    """
    Get the name of the user's corporate department.
    """
    try:
        session = RSession.find((RSession.phoneNumber == phoneNumber) & (RSession.state == "STAFF-ATTENDANCE")).first()
        return session.corporateDepartment
    except Exception as e:
        print("Error:", str(e))
        return False

def RsaveCorporateDepartment(phoneNumber, dept):
    """
    Save the user's corporate department.
    """
    session = RSession.find((RSession.phoneNumber == phoneNumber)).first()
    if not session:
        return {"successful": False, "reason": "no session was found"}
    session.corporateDepartment = dept
    session.save()
