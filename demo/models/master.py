from odoo import models, fields

class Master(models.Model):
    _name = "model.master"
    _description = "descrição do master"    
    
    int_field = fields.Integer(
        string="label intField",         
        help="help do campo inteiro",
        #translate=True, # indica q o campo pode ser traduzido para outros idiomas
        required = True,
        readonly = False,
        default = 10,       
    )
    
    compute_field = fields.Integer(
        string="compute field",         
        required = True,
        readonly = True,
        store = False,      # não persiste no banco
        compute = "_compute_x"
    )    
    
    def _compute_x(self):
        self.int_field = 10 + 10

    bool_field = fields.Boolean(
        string="bool field",
        required = True,
        readonly = True,
        store = False,
    )

    float_field = fields.Float(
        string="Float field",
        digits=(10,2)
    )

    # string
    char_field = fields.Char(
        string="Char field",
        index=True, # cria indica na base de dados
        size=20
    )

    # memo
    text_field = fields.Text(
        string = "Text field",
        size = 50
    )

    # enum
    selection_field = fields.Selection([
            ('a', 'Active'),
            ('i', 'Inactive'),
        ],
        string='Selection field',
        required = True        
    )

    # date 
    date_field = fields.Date(
        string="date field"
    )

    # date time
    datetime_field = fields.Datetime(
        string="date field"
    )

    # FK

    sales_order_id = fields.Many2one("sales_order", 
        string = "Sales order",
        help="somente ordem com has message",
        ondelete = "cascade",                       #``'set null'``, ``'restrict'``, ``'cascade'``        
        domain = [('has_message', '=', 'True')]     # Filtro dos registros pai
    )

    
    detail_ids = fields.One2many("model.detail", "master_id",
        string="Detail(s)"
    )

    # many2mane será criada a tabela de relacionamento_(sufixo _rel) com as 2 chaves
    # db1=# select * from model_config_model_master_rel;
    # model_master_id | model_config_id 
    #-----------------+-----------------
    
    config_ids = fields.Many2many("model.config", 
        string = "configs (Relacionamento)"
    )

    
