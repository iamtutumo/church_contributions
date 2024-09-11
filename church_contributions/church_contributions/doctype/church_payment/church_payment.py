import frappe
from frappe.model.document import Document

class ChurchPayment(Document):
    def before_save(self):
        self.set_payment_id()

    def set_payment_id(self):
        if not self.payment_id:
            member = frappe.get_doc("Church Member", self.member)
            self.payment_id = member.payment_id
