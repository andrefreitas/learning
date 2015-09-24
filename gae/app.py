import webapp2


from handlers import *


application = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/registrations', RegistrationsHandler)
], debug=True)