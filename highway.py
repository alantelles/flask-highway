import sys, os, traceback
from bin.constants import *
from bin.generators import generate
from bin.generators.new_project import new_project

parts = sys.argv
  

  
opt = {
  'generate': generate,
  'g': generate,
  'new': new_project
}
if len(parts) > 1:
  handler = opt.get(parts[1])
  if handler:
    params = parts[2:]
    handler(params)

  else:
    print('Invalid option')

else:
  no_args = """Flask-Highway CLI tool/startup app for accelerating developing with Flask

Flask-Highway creates a basic startup flask app with built-in authentication role-based system.
It features an access control view that turns easy to control access of your applications endpoint
Intuitive and less-write routing declaration system

Usage: highway [options]
    - new [project name]
      Creates a new project

    - generate|g 
      Generates parts of your application (blueprints, views, models...)

Contribute on GitHub!

  https://github.com/alantelles/flask-highway-cli

Flask Highway base app

  https://github.com/alantelles/flask-highway
  """
  print(no_args)

