# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "modulo calyx",
    "summary": """
        modulo calyx
    """,
    "author": "Fabrii9",
    "maintainers": ["Fabrii9"],
    "website": "https://misitio.com.ar/",
    "license": "AGPL-3",
    "category": "Account",
    "version": "15.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["sale", "stock"],
    "data": [
        "views/sale_order_inherit.xml",
        "views/stock_picking_inherit.xml"
    ],
}