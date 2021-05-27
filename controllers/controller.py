from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_name = request.form['title']
    event_date = request.form['date']
    event_number_of_guests = request.form['number of guests']
    event_room = request.form['room']
    event_description = request.form['description']
    event_recurring = request.form.get("recurring")
    new_event = Event(event_name, event_date, event_number_of_guests, event_room, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)
