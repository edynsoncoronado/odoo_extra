# -*- coding: utf-8 -*-
##############################################################################

#import time

from openerp.report import report_sxw
from openerp.addons.jasper_reports import jasper_report
from openerp.addons.jasper_reports import report_xml
import time
from openerp import pooler
#from openerp.addons.jasper_report_demo1.report import jasper_data_parser
import jasper_data_parser

class jasper_print_product(jasper_data_parser.JasperDataParser):
    
    def __init__(self, cr, uid, ids, data, context):
        if context is None:
            context = {}
        super(jasper_print_product,self).__init__(cr, uid, ids, data, context)
    
    def generate_records(self, cr, uid, ids, data, context):
        result=[]
        if not(data['origin_records']):return result  #no mandamos datos al reporte
        product_ids = []
        pool= pooler.get_pool(cr.dbname)
        if 'form' in data:
            product_ids = data['form']['product_ids']
        else:
            product_ids=pool.get('product.product').search(cr,uid,[])
                
        for obj_product in pool.get('product.product').browse(cr,uid,product_ids):
            data = {
                'id':obj_product.id,
                'name': obj_product.name if obj_product.name else 'None',
                'type': obj_product.type,
                'standard_price':obj_product.standard_price if obj_product.standard_price !=0 else 0,
                'categoria':obj_product.categ_id.name
                
#                 'purchase_value': asset.purchase_value if asset.purchase_value != 0 else 0.00,
#                 'salvage_value': asset.salvage_value if asset.salvage_value != 0 else 0.00,
#                 'feosco_code': asset.feosco_code,
#                 'value_residual': asset.value_residual if asset.value_residual != 0 else 0.00,
#                 'feosco_branch_id': asset.feosco_branch_id.name,
#                 'feosco_building_id': asset.feosco_building_id.name,
#                 'feosco_floor_id': asset.feosco_floor_id.name

            }
            result.append(data)

        #result = sorted(result, key=lambda d: (d['name'], d['purchase_value'],))
        print result
        return result
    
    def generate_data_source(self, cr, uid, ids, data, context):
        if not(data['origin_records']):
            return False
        else:
            return 'records'
    
    def generate_parameters(self, cr, uid, ids, data, context):
        return data.get('parameters',False)

jasper_report.report_jasper(
                            'report.report_product', 
                            'product.product',
                            parser=jasper_print_product
                            )