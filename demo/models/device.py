from odoo import models, fields

class Master(models.Model):
    _name = "demo.device"
    _description = "Dispositivos"    

    nome = fields.Char(
        string="Nome",        
        size=30
    )

    ip = fields.Char(
        string="IP",        
        size=20
    )

    vendors_ids = fields.One2many("demo.vendor", "device_id",
        string="Fornecedore(s)"
    )


    
