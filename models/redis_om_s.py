from redis_om import Field, JsonModel
from .redis_manager import RedisManager
from typing import Optional

class RSession(JsonModel):
    phoneNumber: str = Field(index=True)
    state: str = Field(index=True)
    stepsTakenByUser: Optional[str] = Field(index=True)
    longitude: Optional[str] = Field(index=False)
    latitude: Optional[str] = Field(index=False)
    dropoff_location: Optional[str] = Field(index=False)
    paymentModes: Optional[str] = Field(index=False)
    card_mobile_obu_number: Optional[str] = Field(index=False)
    chosenDropOffLocation: Optional[str] = Field(index=False)
    corporateDepartment: Optional[str] = Field(index=True)


    def key(self):
        return f"RSession:{self.phoneNumber}"
    
    def to_dict(self):
        return {
            "phoneNumber": self.phoneNumber,
            "state": self.state,
            "stepsTakenByUser": self.stepsTakenByUser,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "dropoff_location": self.dropoff_location,
            "paymentModes": self.paymentModes,
            "card_mobile_obu_number": self.card_mobile_obu_number,
            "chosenDropOffLocation": self.chosenDropOffLocation,
            "corporateDepartment": self.corporateDepartment,
        }

    def save(self, expire_time=None):
        redis_manager = RedisManager()
        redis_manager.set_data(self.key(), self.to_dict(), expire_time)

    def load(self):
        redis_manager = RedisManager()
        data = redis_manager.get_data(self.key())
        if data:
            self.update(data)

    @classmethod
    def delete(cls, phone_number):
        redis_manager = RedisManager()
        redis_manager.delete_key(cls(phoneNumber=phone_number).key())
