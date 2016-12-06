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
import openerp.addons.decimal_precision as dp


class stock_production_lot(models.Model):
    _inherit='stock.production.lot'
    
    @api.multi
    def put_into_production(self):
        server_host = self.env['hercules.config.settings'].search([], limit=1)
        if not server_host:
            return False
        
        mrp_track_lot_obj = self.env['mrp.track.lot']
        for record in self:  
            mrp_track_lot_id = mrp_track_lot_obj.search([('product_lot', '=', self.name)])
            if not mrp_track_lot_id:
                return False
            
            matlist = {}
            for mrp_track_lot in mrp_track_lot_id:
                    matlist.update({mrp_track_lot.component_lot.name: mrp_track_lot.component.name})
            
            json = {
                u'position': [self.last_location_id.posx, self.last_location_id.posy, self.last_location_id.posz],
                u'lot': self.name,
                u'prod_name': self.product_id.name,
                u'materials': matlist,
                u'operation': u'create',
                
            }
            print json
            #self.buoy_prod = True
        
    @api.one
    def for_production(self):
        return True
    
    @api.one
    def _is_buoy(self):
        if not self.product_id:
            self.is_buoy=False
        self.is_buoy=self.product_id.buoy

    @api.one
    def _is_buoy_prod(self):
        if not self.product_id:
            self.is_buoy_prod=False
        self.is_buoy_prod=self.product_id.buoy_prod
        
    is_buoy = fields.Boolean(compute='_is_buoy', readonly=True)
    is_buoy_prod = fields.Boolean(compute='_is_buoy_prod', readonly=True)
    