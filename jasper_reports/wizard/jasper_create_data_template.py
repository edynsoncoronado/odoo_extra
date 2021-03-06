#import wizard
import pooler
import os
import base64
from osv import osv,fields
from tools.translate import _


class create_data_template(osv.osv_memory):
    _name = 'jasper.create.data.template'
    _description = 'Create data template'


    def escribir_archivo_manualmente(self, cadena, name):
        path = os.path.expanduser('~')
	archivo=open(path + '/' + name + '_jasper.xml','a')
	archivo.write(cadena)
	archivo.close()

    def action_create_xml(self, cr, uid, ids, context=None):
        for data in  self.read(cr, uid, ids, context=context):
            model = self.pool.get('ir.model').browse(cr, uid, data['model'][0], context=context)
            xml = self.pool.get('ir.actions.report.xml').create_xml(cr, uid, model.model, data['depth'], context)

	    self.escribir_archivo_manualmente(xml, model.model.replace('.', '_'))
		
            self.write(cr,uid,ids,{
                'data' : base64.encodestring( xml ), 
                'filename': 'template.xml'
            })
        return {
            'type': ''
        }

    _columns = {
        'model': fields.many2one('ir.model', 'Model', required=True),
        'depth': fields.integer("Depth", required=True),
        'filename': fields.char('File Name', size=32),
        'data': fields.binary('XML')
    }

    _defaults = {
        'depth': 1
    }    
create_data_template()
