import os
from mongoengine import Document, StringField, URLField, DateTimeField, ListField

class Project(Document):
    title = StringField(max_length=255, required=True)
    description = StringField()
    project_type = StringField(choices=["Github Project", "Medium Article", "Experience"], required = True)
    company = StringField()
    url = URLField()
    image_url = URLField()
    created_at = DateTimeField(required = True)
    updated_at = DateTimeField(required = True)
    start_date = DateTimeField()
    end_date = DateTimeField()
    tags = ListField(StringField(max_length=50))