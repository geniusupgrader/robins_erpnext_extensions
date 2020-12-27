frappe.ui.form.on("Vehicle Log", "validate", function(frm) {
    frm.set_value("fuel_cost", frm.doc.fuel_qty * frm.doc.price);
  })