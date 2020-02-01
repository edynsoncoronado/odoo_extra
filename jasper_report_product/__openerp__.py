# -*- coding: utf-8 -*-
##############################################################################

{
    'name': 'Reportes Jasper Demo1',
    'version': '0.1',
    'website': 'http://coronadoedgar.wordpress.com',
    'category': 'Jasper',
    'description': """
Generar reportes con jasper
""",
    'author': 'CoronadoEdgar',
    'depends': ['jasper_reports','product'],
    'data': [
             'report.xml',
             'wizard/report_wizard_view.xml'
            ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
