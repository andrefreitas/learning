import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def template(template_file, values=None):
    if not values:
        values = {}
    jinja_template = JINJA_ENVIRONMENT.get_template(template_file)
    return jinja_template.render(values)

