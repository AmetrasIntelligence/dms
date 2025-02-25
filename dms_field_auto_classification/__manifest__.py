# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Auto classify files into embedded DMS",
    "version": "16.0.1.0.3",
    "category": "Document Management",
    "website": "https://github.com/OCA/dms",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["dms_auto_classification", "dms_field"],
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/dms_classification_template_views.xml",
        "wizards/wizard_dms_classification_views.xml",
    ],
    "demo": ["demo/dms_classification_template_demo.xml"],
    "maintainers": ["victoralmau"],
}
