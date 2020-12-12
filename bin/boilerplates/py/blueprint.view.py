from flask import render_template, redirect, request, url_for, session, flash
import app.blueprints.user_management.views.access_control as access_control

class {view_name_camel}Views:    
    def index(self):
        return render_template('{bp_name}/{view_name}/index.html')

{view_name}_views = {view_name_camel}Views()