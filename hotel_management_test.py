import unittest
from hotel_management_bug import Hotel

class TestHotelManagement(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Test Hotel", {101: "Alice", 102: "Bob"})

    def test_check_in(self):
        self.assertEqual(self.hotel.check_in("Charlie", 103), "Charlie checked into room 103 successfully.")
        self.assertEqual(self.hotel.check_in("Dave", 101), "Error: Room 101 is already occupied.")

    def test_check_out(self):
        self.assertEqual(self.hotel.check_out(101), "Alice checked out from room 101.")
        self.assertEqual(self.hotel.check_out(103), "Error: Room 103 is not occupied.")

if __name__ == "__main__":
    unittest.main()
