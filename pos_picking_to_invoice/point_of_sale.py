# -*- encoding: utf-8 -*-
########################################################################
#
# @authors: Ignacio Ibeas <ignacio@acysos.com>
# Copyright (C) 2013  Acysos S.L.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
# This module is GPLv3 or newer and incompatible
# with OpenERP SA "AGPL + Private Use License"!
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see http://www.gnu.org/licenses.
########################################################################

from osv import osv
from osv import fields
import decimal_precision as dp
from tools.translate import _
import time

class pos_order(osv.osv):
    _inherit = 'pos.order'

    _columns = {
            
        }
    
    def create_picking(self, cr, uid, ids, context=None):
        super(pos_order, self).create_picking(cr, uid, ids, context=None)
        picking_obj = self.pool.get('stock.picking')
        for order in self.browse(cr, uid, ids, context=context):
            if not order.state=='draft':
                continue
            for payment in order.statement_ids:
                if payment.statement_id.journal_id.to_invoiced:
                    picking_obj.write(cr,uid,[order.picking_id.id],{'invoice_state':'2binvoiced'})
        return True
        
pos_order()