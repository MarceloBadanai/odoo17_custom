from odoo import models, fields

class Vendor(models.Model):
    _name = "demo.vendor"
    _description = "Fornecedor"

    razaoSocial = fields.Char(
        string="Nome",        
        size=30
    )

    cidade = fields.Char(
        string="Cidade",        
        size=20
    )
    
    device_id = fields.Many2one("demo.device", 
        string = "Device",
        ondelete = "set null"
    )
