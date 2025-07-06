import unittest
from vehicle import Car, Track


class TestVehicleTableOutput(unittest.TestCase):
    def test_car_table(self):
        print("\n===== Car Fuel Usage Table =====")
        print(f"{'Distance':<10} | {'Before':<10} | {'After':<10} | {'Consumed':<10} | {'Expected':<10} | {'Result'}")
        print("-" * 70)

        car = Car(7) 
        car.fill_up(100)

        test_cases = [
            100,
            200,
            5.777,
            0,
            -1
        ]

        for distance in test_cases:
            with self.subTest(distance=distance):
                fuel_before = car.remaining_fuel()
                try:
                    car.drive(distance)
                    fuel_after = car.remaining_fuel()
                    consumed = round(fuel_before - fuel_after, 4)
                    expected = round(7 * distance / 100, 4)
                    result = "✅" if abs(consumed - expected) < 0.01 else "❌"
                except Exception as e:
                    fuel_after = fuel_before
                    consumed = 0.0
                    expected = round(7 * distance / 100, 4) if distance >= 0 else "N/A"
                    result = f"❌ Error: {type(e).__name__}"

                print(f"{str(distance):<10} | {fuel_before:<10.2f} | {fuel_after:<10.2f} | {consumed:<10} | {expected:<10} | {result}")
                if distance >= 0:
                    self.assertAlmostEqual(consumed, expected, delta=0.01)
                else:
                    with self.assertRaises(ValueError):
                        car.drive(distance)

    def test_track_table_and_trailer_variation(self):
        print("\n===== Track Fuel Usage Table =====")
        print(f"{'Distance':<10} | {'Trailers':<10} | {'Before':<10} | {'After':<10} | {'Consumed':<10} | {'Expected':<10} | {'Result'}")
        print("-" * 90)

        track = Track(15, 2)
        track.fill_up(600)

        test_cases = [
            (2, 100),
            (3, 100),
            (4, 100),
            (0, 100),
            (1, 5.777),
            (1, 0),
            (1, -1)
        ]

        for trailer_count, distance in test_cases:
            with self.subTest(trailers=trailer_count, distance=distance):
                try:
                    track.set_trailer_count(trailer_count)
                    consumption_per_100km = 15 * trailer_count
                    fuel_before = track.remaining_fuel()

                    try:
                        track.drive(distance)
                        fuel_after = track.remaining_fuel()
                        consumed = round(fuel_before - fuel_after, 4)
                        expected = round(consumption_per_100km * distance / 100, 4)
                        result = "✅" if abs(consumed - expected) < 0.01 else "❌"
                    except Exception as e:
                        fuel_after = fuel_before
                        consumed = 0.0
                        expected = round(consumption_per_100km * distance / 100, 4) if distance >= 0 else "N/A"
                        result = f"❌ Error: {type(e).__name__}"

                    print(f"{str(distance):<10} | {trailer_count:<10} | {fuel_before:<10.2f} | {fuel_after:<10.2f} | {consumed:<10} | {expected:<10} | {result}")

                    if distance >= 0:
                        self.assertAlmostEqual(consumed, expected, delta=0.01)
                    else:
                        with self.assertRaises(ValueError):
                            track.drive(distance)

                except ValueError:
                    print(f"❌ Error: Invalid trailer count {trailer_count}")
                    self.assertTrue(trailer_count < 0 or trailer_count > 4)

    def test_trailer_count_limits(self):
        print("\n--- Проверка допустимых значений количества трейлеров ---")
        valid_counts = [0, 1, 2, 3, 4] # тест с 0 трейлеров не очень информативный и как будто бесполезный, т.к. трак все равно будет потреблять бензин в реальности, возможно, стоит добавить что 1 трейлер всегда есть у трака
        for count in valid_counts:
            try:
                Track(15, count)
                print(f"✅ Track with {count} trailer(s) created successfully.")
            except Exception as e:
                self.fail(f"❌ Track with {count} trailer(s) raised an error: {e}")

        print("\n--- Проверка недопустимых значений количества трейлеров ---")
        invalid_counts = [-1, 5]
        for count in invalid_counts:
            with self.subTest(trailer_count=count):
                try:
                    Track(15, count)
                    self.fail(f"❌ Track with {count} trailer(s) should have raised ValueError.")
                except ValueError:
                    print(f"✅ Track with {count} trailer(s) correctly raised ValueError.")
                except Exception as e:
                    self.fail(f"❌ Unexpected exception for trailer count {count}: {e}")

    def test_max_fuel_capacity_car(self):
        car = Car(7)
        car.fill_up(150)
        self.assertLessEqual(car.remaining_fuel(), 100)
        print(f"\n✅ Car max fuel limited to {car.remaining_fuel()}L (not over 100L)")

    def test_max_fuel_capacity_track(self):
        track = Track(15, 2) # здесь еще можно добавить тесты на макс капасити для 1 , 3 и 4 трейлеров 
        track.fill_up(700)
        self.assertLessEqual(track.remaining_fuel(), 600)
        print(f"✅ Track max fuel limited to {track.remaining_fuel()}L (not over 600L)")

class TestTypeValidation(unittest.TestCase):
    def test_type_errors_table(self):
        print("\n===== TypeError Validation Table =====")
        print(f"{'Method':<30} | {'Input':<15} | {'Expected':<15} | {'Result'}")
        print("-" * 80)

        def check(func, input_desc):
            try:
                func()
                result = "❌"
            except TypeError:
                result = "✅"
            except Exception as e:
                result = f"❌ ({type(e).__name__})"
            print(f"{func.__name__:<30} | {input_desc:<15} | TypeError       | {result}")

        car = Car(7)
        track = Track(15, 2)

        check(lambda: car.fill_up("abc"), '"abc" (str)')
        check(lambda: car.drive([100]), '[100] (list)')
        check(lambda: car.fill_up(None), 'None')
        check(lambda: track.set_trailer_count("3"), '"3" (str)')
        check(lambda: track.fill_up([]), '[] (list)')
        check(lambda: track.drive(True), 'True (bool)')

if __name__ == "__main__":
    unittest.main()
