/*

frappe.ui.form.on("Timesheet", "onload", function(frm) {
    frm.fields_dict['time_logs'].grid.get_field('project').get_query = function() {
       return{
           filters: {
            'company': frm.doc.company,
               'status': ["!=", "Completed"]
           }
       }
}
});

*/