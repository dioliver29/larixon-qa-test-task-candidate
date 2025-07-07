import unittest
from vehicle import Car, Track

class CarTests(unittest.TestCase):

    def setUp(self):
        self.car = Car(7)

    # fill_up()
    def test_fill_up_adds_fuel(self):
        self.car.fill_up(50)
        remaining = self.car.remaining_fuel()
        print(f"[Car] After fill_up(50) → Remaining: {remaining}")
        self.assertEqual(remaining, 50)

    def test_fill_up_caps_at_max(self):
        self.car.fill_up(150)
        remaining = self.car.remaining_fuel()
        print(f"[Car] After fill_up(150) → Capped at: {remaining}")
        self.assertEqual(remaining, 100)

    def test_fill_up_zero_raises(self):
        print("[Car] Trying fill_up(0) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.car.fill_up(0)

    def test_fill_up_negative_raises(self):
        print("[Car] Trying fill_up(-10) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.car.fill_up(-10)

    def test_fill_up_invalid_type_raises(self):
        for value in ["50", None, [50], True]:
            print(f"[Car] Trying fill_up({value}) → Expect TypeError")
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    self.car.fill_up(value)

    # drive()
    def test_drive_consumes_correct_fuel(self):
        self.car.fill_up(100)
        self.car.drive(200)
        remaining = self.car.remaining_fuel()
        print(f"[Car] After drive(200) → Remaining: {remaining}")
        self.assertAlmostEqual(remaining, 86.0)

    def test_drive_exact_fuel(self):
        self.car.fill_up(14)
        self.car.drive(200)
        print("[Car] Drove exact amount, expecting 0 fuel left")
        self.assertAlmostEqual(self.car.remaining_fuel(), 0.0)

    def test_drive_insufficient_fuel_raises(self):
        self.car.fill_up(5)
        print("[Car] Trying drive(200) with insufficient fuel → Expect ValueError")
        with self.assertRaises(ValueError):
            self.car.drive(200)

    def test_drive_negative_distance_raises(self):
        self.car.fill_up(50)
        print("[Car] Trying drive(-100) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.car.drive(-100)

    def test_drive_invalid_type_raises(self):
        self.car.fill_up(100)
        for value in ["100", None, [100], True]:
            print(f"[Car] Trying drive({value}) → Expect TypeError")
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    self.car.drive(value)

    # remaining_fuel()
    def test_remaining_fuel_type(self):
        self.car.fill_up(40)
        fuel = self.car.remaining_fuel()
        print(f"[Car] remaining_fuel() → {fuel} (type: {type(fuel)})")
        self.assertIsInstance(fuel, float)

    def test_remaining_fuel_after_fill_and_drive(self):
        self.car.fill_up(50)
        self.car.drive(100)
        fuel = self.car.remaining_fuel()
        print(f"[Car] After fill + drive → Remaining: {fuel}")
        self.assertAlmostEqual(fuel, 43.0)


class TrackTests(unittest.TestCase):

    def setUp(self):
        self.track = Track(15, 2)

    # fill_up()
    def test_fill_up_adds_fuel(self):
        self.track.fill_up(200)
        remaining = self.track.remaining_fuel()
        print(f"[Track] After fill_up(200) → Remaining: {remaining}")
        self.assertEqual(remaining, 200)

    def test_fill_up_caps_at_max(self):
        self.track.fill_up(800)
        remaining = self.track.remaining_fuel()
        print(f"[Track] After fill_up(800) → Capped at: {remaining}")
        self.assertEqual(remaining, 600)

    def test_fill_up_zero_raises(self):
        print("[Track] Trying fill_up(0) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.track.fill_up(0)

    def test_fill_up_negative_raises(self):
        print("[Track] Trying fill_up(-10) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.track.fill_up(-10)

    def test_fill_up_invalid_type_raises(self):
        for value in ["100", None, [100], True]:
            print(f"[Track] Trying fill_up({value}) → Expect TypeError")
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    self.track.fill_up(value)

    # drive()
    def test_drive_consumes_correct_fuel(self):
        self.track.fill_up(600)
        self.track.drive(100)
        remaining = self.track.remaining_fuel()
        print(f"[Track] After drive(100) → Remaining: {remaining}")
        self.assertAlmostEqual(remaining, 570.0)

    def test_drive_exact_fuel(self):
        self.track.fill_up(30)
        self.track.drive(100)
        print("[Track] Drove exact amount, expecting 0 fuel left")
        self.assertAlmostEqual(self.track.remaining_fuel(), 0.0)

    def test_drive_insufficient_fuel_raises(self):
        self.track.fill_up(10)
        print("[Track] Trying drive(100) with insufficient fuel → Expect ValueError")
        with self.assertRaises(ValueError):
            self.track.drive(100)

    def test_drive_negative_distance_raises(self):
        self.track.fill_up(100)
        print("[Track] Trying drive(-100) → Expect ValueError")
        with self.assertRaises(ValueError):
            self.track.drive(-100)

    def test_drive_invalid_type_raises(self):
        self.track.fill_up(100)
        for value in ["50", None, [50], True]:
            print(f"[Track] Trying drive({value}) → Expect TypeError")
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    self.track.drive(value)

    # remaining_fuel()
    def test_remaining_fuel_after_actions(self):
        self.track.fill_up(300)
        self.track.drive(200)
        fuel = self.track.remaining_fuel()
        print(f"[Track] After drive(200) → Remaining: {fuel}")
        self.assertAlmostEqual(fuel, 240.0)

    # trailer count
    def test_set_valid_trailer_count(self):
        for count in range(5):
            self.track.set_trailer_count(count)
            print(f"[Track] set_trailer_count({count}) succeeded")
            self.assertEqual(self.track._trailer_count, count)

    def test_set_invalid_trailer_count_raises(self):
        for count in [-1, 5, "2", None]:
            print(f"[Track] set_trailer_count({count}) → Expect ValueError or TypeError")
            with self.subTest(count=count):
                with self.assertRaises((ValueError, TypeError)):
                    self.track.set_trailer_count(count)


if __name__ == '__main__':
    unittest.main(verbosity=2)
