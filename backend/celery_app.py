from celery import Celery

celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0'
)

from app import app
from application.models import Users
from mail import send_mail
import csv

def generate_csv(data, filename='report.csv'):
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def daily_reminders():
    with app.app_context():
        users = Users.query.all()
        for user in users:
            send_mail(user.email, "Visit the application!", "Hey user,\n\n Have you visited our application? if not click here http://127.0.0.1:5000")
    print('mails sent')

def montly_report():
    with app.app_context():
        users = Users.query.all()
        for user in users:
            # fetch user's past month's information like what he did, no of registrations reviews etc
            data = [
                {'no': 1, 'name': 'reliance'},
                {'no': 2, 'name': 'market'},
                {'no': 3, 'name': 'surya theater'}
            ]
            template = """
here is your past month activity
{% for activity in data %}
    {{ activity.no }} - {{ activity.name }}
{% endfor %}
"""
            from jinja2 import Template
            send_mail(user.email, "Here's your montly activity", Template(template).render(data=data))
    print('mails sent')
