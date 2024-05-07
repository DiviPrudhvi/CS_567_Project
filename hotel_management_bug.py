class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    
    def check_in(self, guest, room_number):
        if room_number not in self.rooms:
            self.rooms[room_number] = guest
            return f"{guest} checked into room {room_number} successfully."
        else:
            return f"Error: Room {room_number} is already occupied."
    
    def check_out(self, room_number):
        if room_number in self.rooms:
            guest = self.rooms.pop(room_number)
            return f"{guest} checked out from room {room_number}."
        else:
            return f"Error: Room {room_number} is not occupied."
    
    def display_rooms(self):
        return self.rooms

hotel = Hotel("Grand Hotel", {101: "Alice", 102: "Bob", 103: "Charlie"})

# Introduce a bug: incorrect method call for displaying rooms
print("Current Rooms:", hotel.display_rooms())  # Bug: Incorrect method call
