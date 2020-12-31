frappe.ui.form.on('Address', {
	before_save(frm) {
		
		var destination_address_string = frm.doc.address_line1+", "+frm.doc.pincode+" "+frm.doc.city+", "+frm.doc.country
		
		    frappe.call({
            method: "robins_erpnext_extensions.robins_erpnext_extensions.doctype.openrouteservice_robins_erpnext_extensions.openrouteservice_robins_erpnext_extensions.get_distance_and_duration",
            args:{
                destination_address: destination_address_string
            },
            callback: function(r) {
                console.log(r)
                frm.doc.distance = r.message[0]
                frm.doc.duration_from_home_address_in_minutes = r.message[1]
            }
        })
		
		frm.refresh()
	}
})


frappe.ui.form.on("Address", {
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