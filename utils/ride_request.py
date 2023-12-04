import requests

# def requestRide():
#     headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "apikey": "lztgzgifb7ok1wwlb9luve90zersbjiz",
# }
#     # url = "https://api.gupshup.io/sm/api/v1/msg"
#     url = "https://api.gupshup.io/wa/api/v1/msg"  

#     payload={
#   "RequestID": "BOOKARIDE",
#   "SessionID": "HBhGpLw0efgwbDqILlYSCC9WT5hoooCh",
#   "Country": "KENYA",
#   "UserID": "VODATZ",
#   "Key": "2342",
#   "MobileNumber": "255798863355",
#   "TrxReference": "0000",
#   "IMEI": "503215342734445",
#   "BookARide": {
#     "Name": "Morgan Gicheha",
#     "VehicleType": "TESTING",
#     "PickupLatitude": "-1.2644332746188693",
#     "PickupLongitude": "36.763407496952304",
#     "PickupAddress": "Kimanga",
#     "DropOffLatitude": "-1.2937341",
#     "DropOffLongitude": "36.8728424",
#     "DropOffAddress": "",
#     "FavouriteDriver": "",
#     "SkipDrivers": "",
#     "PaymentMode": "CASH",
#     "PaymentSource": "255758027779",
#     "CallBackURL": "http://tzvodaipgtest02.vodacomtz.corp:9455/vodaride/callback"
#   }
# }
#     try:
#         response = requests.post(url, headers=headers, data=payload)
#         return response.json()
#     except:
#         pass
#     return {
#   "Status": "000",
#   "TripID": "2875B28E-E779-4F09-B806-6CA24D4E45F5-2023-04",
#   "DriverName": "silas",
#   "DriverMobileNumber": "254743775223",
#   "DriverEmail": "odongosilas648@gmail.com",
#   "DriverPIC": "https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample02.jpg",
#   "PromoCode": "",
#   "DriverLatitude": "-3.991070500000000",
#   "DriverLongitude": "39.709338500000001",
#   "CarModel": "BAJAJ",
#   "CarNumber": "KMEB280R",
#   "CarColor": "Blue",
#   "DriverRating": "4.75",
#   "RoadDistance": "0",
#   "TimeDistance": "0",
#   "FriendCode": "2875B28E-",
#   "SocialMediaID": "",
#   "TripDistance": "0.00",
#   "TripTime": "0.00"
# }

def requestRide():
    return {
  "Status": "000",
  "TripID": "2875B28E-E779-4F09-B806-6CA24D4E45F5-2023-04",
  "DriverName": "silas",
  "DriverMobileNumber": "254743775223",
  "DriverEmail": "odongosilas648@gmail.com",
  "DriverPIC": "https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample02.jpg",
  "PromoCode": "",
  "DriverLatitude": "-3.991070500000000",
  "DriverLongitude": "39.709338500000001",
  "CarModel": "BAJAJ",
  "CarNumber": "KMEB280R",
  "CarColor": "Blue",
  "DriverRating": "4.75",
  "RoadDistance": "0",
  "TimeDistance": "0",
  "FriendCode": "2875B28E-",
  "SocialMediaID": "",
  "TripDistance": "0.00",
  "TripTime": "0.00"
}


if __name__ == "__main__":
    print(requestRide())