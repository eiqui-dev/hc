# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Solucións Aloxa S.L. <info@aloxa.eu>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
#===============================================================================
# # REMOTE DEBUG
#import pydevd
# 
# # ...
# 
# # breakpoint
#pydevd.settrace("10.0.3.1")
#===============================================================================
from openerp import models, fields, api
from openerp.http import request
import openerp.addons.decimal_precision as dp


class product_product(models.Model):
    _inherit='product.template'
    
    buoy = fields.Boolean(string='Buoy', default=False)
    buoy_prod = fields.Boolean(string='Buoy Production', default=False)
