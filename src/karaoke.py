class Karaoke:
    def __init__(self, input_name, input_rooms, input_guests):
        self.name = input_name
        self.rooms = input_rooms
        self.guests = input_guests
    
    def add_room(self, room_data):
        self.rooms.append(room_data)