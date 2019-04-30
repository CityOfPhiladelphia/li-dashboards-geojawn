from flask import Blueprint, render_template, redirect

from li_metabase.utils import Dashboard, build_iframe_url_from_dashboard_url, DashboardNotFound
from li_metabase.auth import auth


MISC_DASHBOARDS = [
    Dashboard('Service Requests', 'service-requests', 158)
]

bp = Blueprint('misc', __name__)

@bp.route('/misc/<dashboard_url>')
@auth.login_required
def misc(dashboard_url):
    global MISC_DASHBOARDS

    iframe_url = build_iframe_url_from_dashboard_url(dashboard_url, MISC_DASHBOARDS)

    return render_template('dashboard.html', iframe_url=iframe_url)

@bp.errorhandler(DashboardNotFound)
def handle_error(error):
    return render_template('error.html')