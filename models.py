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

# ---------------------------- CLASE HEREDADA - SALE ORDER ------------------------------------
class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    peso_lleno = fields.Float(string="Peso Lleno")
    peso_vacio = fields.Float(string="Peso Vacio")
    peso_neto = fields.Float( string="Peso Neto")
    placa = fields.Char( string="Placa")


# Calcular el peso neto
    @api.onchange('peso_lleno', 'peso_vacio')
    def _action_peso_neto(self):

      if self.peso_lleno > 0 and self.peso_vacio > 0:
        self.peso_neto = self.peso_lleno - self.peso_vacio


