import webapp2
from models import *
from views import template


class RegistrationsHandler(webapp2.RequestHandler):

    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        course = self.request.get('course')
        r = Registration(name=name, email=email, course=course)
        r.put()
        self.response.write(template('confirmation.html'))

    def get(self):
        registrations = Registration.all()
        template_values = {"registrations": registrations}
        self.response.write(template('registrations.html', template_values))
