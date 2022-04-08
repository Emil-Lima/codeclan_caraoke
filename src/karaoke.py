class Karaoke:
    def __init__(self, input_name, input_rooms):
        self.name = input_name
        self.rooms = input_rooms
    
    def add_room(self, room_data):
        self.rooms.append(room_data)