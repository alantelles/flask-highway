from flask import render_template, redirect, request, url_for, session, flash
from app.views.base_views import BaseViews
import app.blueprints.user_management.views.access_control as access_control
from dont_touch.core_views import render

class {view_name_camel}Views(BaseViews):    
{views_list}
{view_name}_views = {view_name_camel}Views()