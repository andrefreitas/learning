import webapp2
from models import *
from views import *

class RegistrationsHandler(webapp2.RequestHandler):

    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        course = self.request.get('course')
        r = Registration(name = name, email = email, course = course)
        r.put()
        template = JINJA_ENVIRONMENT.get_template('confirmation.html')
        self.response.write(template.render())

    def get(self):
        registrations = Registration.all()
        template_values = {"registrations" : registrations}
        template = JINJA_ENVIRONMENT.get_template('registrations.html')
        self.response.write(template.render(template_values))
