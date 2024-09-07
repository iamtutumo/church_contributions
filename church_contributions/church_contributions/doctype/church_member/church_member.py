import frappe
from frappe.model.document import Document

class ChurchMember(Document):
    def before_save(self):
        self.generate_payment_id()
        self.set_hierarchy()

    def generate_payment_id(self):
        if not self.payment_id:
            self.payment_id = f"CHURCH-{frappe.generate_hash(length=8)}"

    def set_hierarchy(self):
        if self.parish:
            parish = frappe.get_doc("Church Parish", self.parish)
            self.archdeaconry = parish.archdeaconry
            archdeaconry = frappe.get_doc("Church Archdeaconry", self.archdeaconry)
            self.diocese = archdeaconry.diocese
