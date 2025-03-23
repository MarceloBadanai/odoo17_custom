from odoo import models, fields

class Detail(models.Model):
    _name = "model.detail"
    _description = "descrição do detail"    

    # string
    char_field = fields.Char(
        string="Char field",
        size = 15
    )

    master_id = fields.Many2one("model.master", 
        string = "master",
        ondelete = "set null"
    )
    
