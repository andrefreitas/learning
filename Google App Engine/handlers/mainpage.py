import webapp2
from models import *
from views import *

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('form.html')
        self.response.write(template.render())
