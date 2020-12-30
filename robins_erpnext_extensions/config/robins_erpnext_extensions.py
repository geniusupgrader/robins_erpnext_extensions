from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Robins Erpnext Extensions"),
        "items": [
                                   {
              "type": "doctype",
              "name": "Lead_Type_robins_erpnext_extensions",
              "label": _("Item Group Website Link"),
              "description": _("Description of Jugglingtricks"),
            },
                    {
              "type": "doctype",
              "name": "OpenRouteService_robins_erpnext_extensions",
              "label": _("Open Route Service"),
              "description": _("Description of Lists"),
            },
                                   {
              "type": "doctype",
              "name": "WebGroup_robins_erpnext_extensions",
              "label": _("Web Category"),
              "description": _("Description of Categories"),
            },
                                   {
              "type": "doctype",
              "name": "Wishlist_robins_erpnext_extensions",
              "label": _("Wishlist"),
              "description": _("Wishlist"),
            },
                                               {
              "type": "doctype",
              "name": "Wishlist_entries_robins_erpnext_extensions",
              "label": _("Wishlist Entries"),
              "description": _("Wishlist"),
            }
        ]
      }
  ]
