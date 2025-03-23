from odoo import models, fields

class Detail(models.Model):
    _name = "model.config"
    _description = "descrição do config"    

    # string
    char_field = fields.Char(
        string="Char field",
        size = 15
    )

    
