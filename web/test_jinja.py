import random

from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader('web'),
    autoescape=select_autoescape(['html', 'xml']),
)
template = env.get_template("ind.html")
print(template.render(c=80))
