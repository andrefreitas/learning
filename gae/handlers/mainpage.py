import webapp2
from views import template


class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(template('form.html'))
