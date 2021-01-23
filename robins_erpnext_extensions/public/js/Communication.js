frappe.ui.form.on('Communication', {
	refresh(frm) {
		frm.add_custom_button(__("Create Todo"), function() {
        var tododoc = frappe.model.get_new_doc('ToDo');
		//new_exercise_doc.exercise = frm.doc.name;
		frappe.set_route('Form', 'ToDo', tododoc.name);
    }); 
	}
})