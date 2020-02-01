# -*- coding: utf-8 -*-
##############################################################################

from openerp.osv import fields, osv
#from openerp.addons.jasper_reports import jasper_report
#import logging

class product_report_stock_wizard(osv.osv_memory):
    _name="product.report.stock_wizard"
    #__logger = logging.getLogger(_name)
    _columns={
              #'product_ids':fields.many2many('product.product',string="Productos"),
              #'select_product':fields.boolean("Seleecionar lista de productos"),
              'product_id':fields.many2one('product.product',"Producto",required=True),
              #'report_type':fields.selection([("pdf","PDF"), ("xls","Excel"), ("html","HTML")],'Tipo'),
              }

#     _defaults = {
#         'report_type': lambda *a: 'pdf',
#         'select_product': False
#     }
    
    def check_report(self, cr, uid, ids, context=None):
        data={}
        data['model']='product.product'
        data['ids']=ids
        data['origin_records']=False
#         if data['origin_records']:
#             data['form']=self.read(cr,uid,ids,['product_ids'])[-1]
        #else:
#             dic=self.read(cr,uid,ids,['product_ids'])[-1]
#             product_ids_demo=dic['product_ids']
#             text_p=""
#             count=0
#             total=len(product_ids_demo)-1
#             for p in product_ids_demo:
#                 if (count==total):
#                     text_p +=str(p)
#                 else:
#                     text_p +=str(p)+","
#                 count+=1
                
        data.update({'parameters':{
                            'report_title':"Reporte Producto con jasper",
                            'product_id':self.browse(cr,uid,ids[0]).product_id.id
                            }
                  })
        r= {
                'type':'ir.actions.report.xml',
                'report_name':'report_product',
                'datas':data,
        }
        return r

product_report_stock_wizard()