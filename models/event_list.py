from models.event import *

event1 = Event("Gala", "2021-09-25", 7, "room 1", "It is a Gala", True)
event2 = Event("Gala", "2020-08-12", 4, "room 2", "It is a Gala", False)

events = [event1, event2]

def add_new_event(event):
    events.append(event)