import frappe
from frappe import _

@frappe.whitelist()
def submit_contribution(payment_id, amount):
    member = frappe.get_value("Church Member", {"payment_id": payment_id}, "name")
    if not member:
        frappe.throw(_("Invalid Payment ID"))
    
    payment = frappe.get_doc({
        "doctype": "Church Payment",
        "member": member,
        "payment_date": frappe.utils.today(),
        "amount": amount,
        "payment_status": "Completed"
    })
    payment.insert()
    return True

@frappe.whitelist()
def get_recent_contributions():
    return frappe.get_all("Church Payment",
        fields=["member", "payment_date", "amount"],
        filters={"payment_status": "Completed"},
        order_by="payment_date desc",
        limit=5
    )
