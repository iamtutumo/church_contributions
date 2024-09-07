import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "payment_date",
            "label": _("Payment Date"),
            "fieldtype": "Date",
            "width": 100
        },
        {
            "fieldname": "member",
            "label": _("Member"),
            "fieldtype": "Link",
            "options": "Church Member",
            "width": 200
        },
        {
            "fieldname": "parish",
            "label": _("Parish"),
            "fieldtype": "Link",
            "options": "Church Parish",
            "width": 150
        },
        {
            "fieldname": "archdeaconry",
            "label": _("Archdeaconry"),
            "fieldtype": "Link",
            "options": "Church Archdeaconry",
            "width": 150
        },
        {
            "fieldname": "diocese",
            "label": _("Diocese"),
            "fieldtype": "Link",
            "options": "Church Diocese",
            "width": 150
        },
        {
            "fieldname": "amount",
            "label": _("Amount"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "payment_status",
            "label": _("Payment Status"),
            "fieldtype": "Data",
            "width": 120
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql("""
        SELECT
            cp.payment_date,
            cp.member,
            cm.parish,
            cm.archdeaconry,
            cm.diocese,
            cp.amount,
            cp.payment_status
        FROM
            `tabChurch Payment` cp
        JOIN
            `tabChurch Member` cm ON cp.member = cm.name
        WHERE
            1=1 %s
        ORDER BY
            cp.payment_date DESC
    """ % conditions, filters, as_dict=1)
    
    return data

def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " AND cp.payment_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND cp.payment_date <= %(to_date)s"
    if filters.get("member"):
        conditions += " AND cp.member = %(member)s"
    if filters.get("parish"):
        conditions += " AND cm.parish = %(parish)s"
    if filters.get("archdeaconry"):
        conditions += " AND cm.archdeaconry = %(archdeaconry)s"
    if filters.get("diocese"):
        conditions += " AND cm.diocese = %(diocese)s"
    return conditions
