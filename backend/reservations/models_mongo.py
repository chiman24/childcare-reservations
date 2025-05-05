# models_mongo.py
from mongoengine import Document, StringField, IntField, ListField, DateField 

class Reservation(Document):
    parent_name = StringField(required=True)
    rehearsal_date = DateField(required=True)
    email = StringField(required=True)
    num_children = IntField(required=True)
    phone_number = StringField()
    child_ages = ListField(IntField(), required=True)  # Store child ages as a JSON array
    special_notes = StringField(blank=True, null=True)
    timestamp = DateField(auto_now_add=True)  # Auto record submission time

    meta = {'collection': 'childcare_reservations'}
