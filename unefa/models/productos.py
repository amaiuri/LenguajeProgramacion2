# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class productos(osv.osv):
    _name='unefa.productos'
    _rec_name='codigo'

    _columns={
        'codigo':fields.char('Codigo',size=20,required=True,help='Codigo del producto'),
        'descripcion':fields.char('Descripcion',size=80,required=True,help='Descripcion del producto'),
        'marca_id':fields.many2one('unefa.marcas','Marca del producto'),
        'existencia':fields.integer('Existencia',size=10,required=True,help='existencia del producto'),
        'fecha_compra':fields.date('Fecha de Compra',help='Fecha de compra del producto'),
        'precio_compra':fields.float('Precio de compra',digits=2),
        'precio_venta':fields.float('Precio de venta',digits=2),
        'active':fields.boolean('Activo'),
    }
    
	_defaults={
		'active';True,
	}
