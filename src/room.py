class Room:
    def __init__(self, input_name, input_songs, input_customers, input_maximum_capacity):
        self.name = input_name
        self.songs = input_songs
        self.customers = input_customers
        self.maximum_capacity = input_maximum_capacity

    def add_guest(self, guest_data):
        if len(self.customers) < self.maximum_capacity:
            self.customers.append(guest_data)

    def check_out_guest(self, guest_data):
        self.customers.remove(guest_data)

    def add_song(self, song_data):
        self.songs.append(song_data)