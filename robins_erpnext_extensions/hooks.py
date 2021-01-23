# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "robins_erpnext_extensions"
app_title = "Robins Erpnext Extensions"
app_publisher = "Robin Rosenstock"
app_description = "Robins Erpnext Extensions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "robin.rosenstock@t-online.de"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/robins_erpnext_extensions/css/robins_erpnext_extensions.css"
# app_include_js = "/assets/robins_erpnext_extensions/js/robins_erpnext_extensions.js"

# include js, css files in header of web template
# web_include_css = "/assets/robins_erpnext_extensions/css/robins_erpnext_extensions.css"
# web_include_js = "/assets/robins_erpnext_extensions/js/robins_erpnext_extensions.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Vehicle Log" : "public/js/Vehicle_Log.js",
    "Timesheet" : "public/js/Timesheet.js",
    "Address" : "public/js/Address.js",
    "Communication" : "public/js/Communication.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "robins_erpnext_extensions.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "robins_erpnext_extensions.install.before_install"
# after_install = "robins_erpnext_extensions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "robins_erpnext_extensions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"robins_erpnext_extensions.tasks.all"
# 	],
# 	"daily": [
# 		"robins_erpnext_extensions.tasks.daily"
# 	],
# 	"hourly": [
# 		"robins_erpnext_extensions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"robins_erpnext_extensions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"robins_erpnext_extensions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "robins_erpnext_extensions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "robins_erpnext_extensions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "robins_erpnext_extensions.task.get_dashboard_data"
# }

