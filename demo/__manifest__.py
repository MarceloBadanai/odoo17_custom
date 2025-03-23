{
    'name' : 'demo',
    'version' : '1.0',
    'description' : 'demo - description *',
    'summary' : 'demo - summary',
    'author' : 'demo - author - badarov',

    'category': 'Demo/Demo',

    "depends" : [
        "sale",
        "account"
    ],

    "data" : [
        "views/demo_actions.xml",
        "views/demo_menus.xml",
        "security/demo_security.xml",
        #"security/ir.model.access.csv"        
    ],
    
    # para definir se o módulo é um application 
    # necessário dar upgrade no aplicativo
    'application' : 'true'
}