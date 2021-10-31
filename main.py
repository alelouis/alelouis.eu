import jinja2
import json

TEMPLATE_FILE = "templates/shortstories.html"

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
template = env.get_template(TEMPLATE_FILE)

with open('shortstories.json', 'r') as f:
	data = json.load(f)
	
output = template.render(data)
# to save the results
with open("shortstories.html", "w") as fh:
	fh.write(output)