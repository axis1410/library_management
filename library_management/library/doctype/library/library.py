# Copyright (c) 2025, Aditya Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Library(Document):
    def before_save(self):
        self.set_library_address()

    def set_library_address(self):
        if self.address:
            address = frappe.get_doc("Address", self.address)
            self.address_data = f"{address.address_line1}\n{address.address_line2}\n{address.city}\n{address.state}\n{address.country}\nPIN Code: {address.pincode}"
        else:
            self.address_data = ""
