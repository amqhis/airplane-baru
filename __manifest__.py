{
    'name': 'tiket pesawat',
    'version': '1.0',
    'author': 'amira Balqhis',
    'summary': 'module yang berisikan Pesawat, Form pesawat, Harga',
    'description': """ ini adalah module custom di udoo mengenai tiket pesawat """,
    'application': False,
    'website': 'https://www.odooairplane.com',
    'depends': ['base'], 
    'data': [
        'views/plane.xml',
        'views/template.xml',
        'views/dashboard.xml',
        'reports/report.xml',
        'reports/boarding_pass.xml',
        'data/data.xml',
        'security/ir.model.access.csv'
    ],
    'qweb' : [
        'static/xml/*.xml',
    ]
    
}