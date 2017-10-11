# -*- coding: utf-8 -*-
 
from openerp import models, fields, api
import subprocess
import time
from openerp.exceptions import Warning


# ---------------------------- CLASE HEREDADA - ORDER LINE ------------------------------------
class sale_line(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'
    imagen_lleno = fields.Binary (string="Imagen Lleno")
    imagen_vacio = fields.Binary (string="Imagen Vacio")



