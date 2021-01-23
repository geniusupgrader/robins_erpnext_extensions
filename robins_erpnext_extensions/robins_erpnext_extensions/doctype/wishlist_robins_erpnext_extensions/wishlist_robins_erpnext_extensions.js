// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt


frappe.ui.form.on('Wishlist_robins_erpnext_extensions', {
	onload(frm) {
			frappe.call({
			method: "frappe.desk.form.linked_with.get_linked_doctypes",
			args: {
			    'doctype': 'Wishlist_robins_erpnext_extensions'
			},
			callback: function(r) {
				console.log(r)
				
							frappe.call({
			method: "frappe.desk.form.linked_with.get_linked_docs",
			args: {
			    'doctype': 'Wishlist_robins_erpnext_extensions',
			    'name': 'Future-Tech',
			    'linkinfo': r.message
			},
			callback: function(r2) {
				console.log(r2)
			}
			})
			}
			})
	}
})