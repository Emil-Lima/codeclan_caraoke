class Room:
    def __init__(self, input_name, input_songs, input_customers):
        self.name = input_name
        self.songs = input_songs
        self.customers = input_customers

    def add_guest(self, guest_data):
        self.customers.append(guest_data)

    def add_song(self, song_data):
        self.songs.append(song_data)