class Karaoke:
    def __init__(self, input_name, input_rooms, input_guests, input_entry_fee):
        self.name = input_name
        self.rooms = input_rooms
        self.guests = input_guests
        self.entry_fee = input_entry_fee
    
    def add_room(self, room_data):
        self.rooms.append(room_data)

    def let_guest_in(self, guest_data):
        self.guests.append(guest_data)