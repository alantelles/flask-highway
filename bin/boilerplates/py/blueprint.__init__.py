import os
from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from app.views.base_views import BaseViews
from dont_touch.core_views import render
from dont_touch.helpers.routes import register_routes

#DON'T REMOVE: blueprint views register section

#END: blueprint views register section



{bp_name} = Blueprint('{bp_name}', __name__, template_folder='templates')
{bp_name}_path = os.path.join(os.getcwd(),'app', 'blueprints', '{bp_name}')


class {bp_name_camel}Views(BaseViews):
    
    def index(self):
        self.render('/blog/index')

{bp_name}_views = {bp_name_camel}Views()

#DON'T TOUCH: register routes section
register_routes('{bp_name}', {bp_name}_views={bp_name}_views)
#END: register routes section