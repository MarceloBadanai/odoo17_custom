from odoo import models, fields

class Master(models.Model):
    _name = "demo.device"
    _description = "Dispositivos"    

    nome = fields.Char(
        string="Nome",        
        size=30
    )

    ip = fields.Char(
        string="Nome",        
        size=20
    )

    
