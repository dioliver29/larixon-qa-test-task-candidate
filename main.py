from asphalt_road import AsphaltRoad
from vehicle import Car, Track

if __name__ == "__main__":
    asphalt_road = AsphaltRoad()

    car = Car(7)
    track = Track(15, 2)

    asphalt_road.add_vehicle(car)
    asphalt_road.add_vehicle(track)

    asphalt_road.fill_up(car, 80)
    asphalt_road.fill_up(track, 250)

    distance = 500.0
    asphalt_road.drive(car, distance)
    asphalt_road.drive(track, distance)

    asphalt_road.print_vehicle_remaining_fuels() 