"""
The Liskov substitution principle states that a child class must be substitutable for its parent class. Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send: {message} to {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send: {message} to {self.phone}")


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notifications):
        self.notifications = notifications

    def send(self, message):
        self.notifications.notify(message)


if __name__ == "__main__":
    contact = Contact("John Doe", "john@test.com", "(408)-888-9999")

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Hello John")

    notification_manager.notification = email_notification
    notification_manager.send("Hi John")
