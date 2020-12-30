# Copyright (c) 2013, Robin Rosenstock and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.desk.form.linked_with import get_linked_docs, get_linked_doctypes



def get_data():

	list_of_dict_for_data = []

	# get all "Wishlist_entries"-documents from wishlist:
	names_of_wishlistentries_docs = frappe.db.get_all("Wishlist_entries_robins_erpnext_extensions")
	# print(names_of_wishlistentries_docs)

	for entry in names_of_wishlistentries_docs:

		wishlistentries_doc = frappe.get_doc("Wishlist_entries_robins_erpnext_extensions", entry)
		# print(wishlistentries_doc.name1)
		name = wishlistentries_doc.name1
		wishlist = wishlistentries_doc.wishlist
		link = wishlistentries_doc.get_url()
		link = "<a href=\""+link+"\">Link"+"</a>"
		doctype = "Wishlist_entries_robins_erpnext_extensions"
		dict_for_data = {
		"name": name,
		"wishlist": wishlist,
		"link": link,
		"doctype": doctype
		}
		list_of_dict_for_data.append(dict_for_data)


	# and get all "Item"-documents which are linked to wishlist (where wishlist is set):
	names_of_itemdocs = frappe.db.get_all("Item", filters={'wishlist': ['is', 'set']})

	for entry in names_of_itemdocs:

		item_doc = frappe.get_doc("Item", entry)
		name = item_doc.item_name
		wishlist = item_doc.wishlist
		link = item_doc.get_url()
		link = "<a href=\""+link+"\">Link"+"</a>"
		doctype = "Item"
		dict_for_data = {
		"name": name,
		"wishlist": wishlist,
		"link": link,
		"doctype": doctype
		}
		list_of_dict_for_data.append(dict_for_data)


	return list_of_dict_for_data



def execute(filters=None):
	columns = [
		{
		"fieldname": "name",
		"label": "Name",
		"fieldtype": "Data",
		},
		{
		"fieldname": "wishlist",
		"label": "Wishlist",
		"fieldtype": "Link",
		"options": "Wishlist_robins_erpnext_extensions"
		},
		{
		"fieldname": "link",
		"label": "Link",
		"fieldtype": "HTML",
		},
		{
		"fieldname": "doctype",
		"label": "Doctype",
		"fieldtype": "Link",
		"options": "DocType",
		}
	]

	data = get_data()

	return columns, data
