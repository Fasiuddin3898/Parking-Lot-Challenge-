import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_width=8, spot_length=12):
        self.spot_size = spot_width * spot_length
        self.total_spots = square_footage // self.spot_size
        self.parking_lot = [None] * self.total_spots
        self.parking_map = {} 

    def park_car(self, car, spot):
        if spot < 0 or spot >= self.total_spots:
            return "Invalid spot number. Please choose another spot."

        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            self.parking_map[str(car)] = spot
            return f"Car with license plate {car} parked successfully in spot {spot}."
        else:
            return "Spot is already occupied. Try another spot."

    def generate_parking_map(self):
        return json.dumps(self.parking_map)

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return str(self.license_plate)

    def park(self, parking_lot):
        spot = random.randint(0, len(parking_lot.parking_lot) - 1)
        status = parking_lot.park_car(self, spot)
        while status == "Spot is already occupied. Try another spot.":
            spot = random.randint(0, len(parking_lot.parking_lot) - 1)
            status = parking_lot.park_car(self, spot)
        print(status)


def main():
    cars = [Car('ABC1234'), Car('XYZ5678'), Car('DEF9012'), Car('GHI3456')]  
    parking_lot = ParkingLot(2000) 

    for car in cars:
        car.park(parking_lot)
        if None not in parking_lot.parking_lot:
            print("Parking lot is full.")
            break

if __name__ == "__main__":
    main()
