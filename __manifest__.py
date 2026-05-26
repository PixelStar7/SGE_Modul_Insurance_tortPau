# -*- coding: utf-8 -*-
{
    'name': 'Insurance',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Insurance Management',
    'description': """
          Module prepared by department 'Informàtica i comunicacions'
          of Institute Milà i Fontanals in Igualada (Barcelona-Spain)
          for learning in development and adaptation of modules of Odoo ERP.

          It is part of the learning materials for the module
          'Sistemes de gestió empresarial' in the course
          'CFS Desenvolupament d''aplicacions multiplataforma'.
    """,
    'author': 'Group DAM2 - Course 2025-2026',
    'website': 'http://www.infomila.info',
    'depends': ['base', 'product', 'sale', 'purchase'],
    'data': [
        'views/insurance_views.xml',
        # 'report/insurance_report_qweb.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}