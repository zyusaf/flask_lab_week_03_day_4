class Event():
    def __init__(self, name_of_event, date, number_of_guests, room, description, recurring):
        self.name_of_event = name_of_event
        self.date = date
        self.number_of_guests = number_of_guests
        self.room = room
        self.description = description
        self.recurring = recurring