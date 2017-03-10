# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class marcas(osv.osv):
    _name='unefa.productos'
    _rec_name='codigo'

    _columns={
        'marca':fields.char('Marca',size=50,required=True,help='Marca del producto'),
        'active':fields.boolean('Activo'),
    }
	
	_defaults={
		'active';True,
	}
