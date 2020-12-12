import sys, os, traceback
from bin.constants import *
from bin.generators import generate

parts = sys.argv
  
def new_project(params):
  try:
    os.mkdir(APPP)
    os.mkdir(BPP)
    os.mkdir(TPS)
    os.mkdir(DTB)
    os.mkdir(LYT)
    os.mkdir(STCS)
   
    
    print('New Flask Highway project initialized')
    
  except IndexError:
    raise IndexError('A name for your project was not provided')
    
  
  
opt = {
  'generate': generate,
  'g': generate,
  'new': new_project
}
if len(parts) > 1:
  handler = opt[parts[1]]
  params = parts[2:]
  handler(params)

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

