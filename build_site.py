from jinja2 import Environment, FileSystemLoader
import os



env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
template = env.get_template('index.html')
print template.render()