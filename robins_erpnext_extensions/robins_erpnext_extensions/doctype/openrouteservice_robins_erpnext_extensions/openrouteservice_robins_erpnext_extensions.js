// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

// frappe.ui.form.on('OpenRouteService_robins_erpnext_extensions', {
// 	// refresh: function(frm) {

// 	// }
// });

frappe.ui.form.on("OpenRouteService_robins_erpnext_extensions", {
	refresh: function(frm) {
		frm.add_custom_button(__("Update All Adresses"), function() {
			
			frappe.call({
			method: "robins_erpnext_extensions.robins_erpnext_extensions.doctype.openrouteservice_robins_erpnext_extensions.openrouteservice_robins_erpnext_extensions.update_all",
			callback: function(r) {
				// console.log(r)
				//frm.doc.distance = r.message[0]
				//frm.doc.duration_from_home_address_in_minutes = r.message[1]
				// frm.refresh()
			}
			})
			
		}); 
	}
	});
	


