# -*- coding: utf-8 -*-
{
     'name': "Knowledge Base Pro",

    'summary': """Confluence, Notion, Nuclino like documentation and wiki management in Odoo. Knowledge base. KnowSystem, Know system, Manage Notes ,React Documentation Tool, Odoo Wiki Module, Odoo Note-taking App, React UI for Odoo, Odoo Internal Wiki, tech finna, Odoo Business Documentation, React Integration in Odoo, Modern UI for Odoo, Odoo Collaboration Tool, Enterprise Wiki Odoo, Odoo Productivity Apps, Custom React Applications Odoo, Odoo Documentation Platform, React Notes Module, Odoo Knowledge Base. KMS. Wiki-like revisions. Knowledge management solution. Notion features. Docket features. Helpdesk knowledge. Collaborative library. Knowledge-based. Internal wiki. Documentation online. Knowledge online.""",

    'description': """
        React Documentation Tool, Odoo Wiki Module, Odoo Note-taking App, React UI for Odoo, Odoo Internal Wiki, Odoo Business Documentation, React Integration in Odoo, Modern UI for Odoo, Odoo Collaboration Tool, Enterprise Wiki Odoo, Odoo Productivity Apps, Custom React Applications Odoo, Odoo Documentation Platform, React Notes Module, Odoo Knowledge Base.
    """,

    'author': "TechFinna",
    'website': "https://techfinna.com/",
    'category': 'Productivity',
    'price': 147,
    'currency': 'USD',
    'version': '2.0',
    'installable': True,
    'live_test_url': 'https://demo.techfinna.com',
    'support': "info@techfinna.com",
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'images': ['static/description/banner11.gif'],
    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
