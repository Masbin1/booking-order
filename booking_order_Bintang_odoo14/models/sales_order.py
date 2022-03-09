from importlib.metadata import requires
from pickletools import read_uint1

from setuptools import Require
from odoo import api, fields, models


class SalesOrder(models.Model):
    _name = 'sales.order'
    _description = 'New Description'

    is_boolean_order = fields.Boolean(string='')
    team = fields.Many2one(comodel_name='service.team', string='Team', required=True)
    team_leader = fields.Many2one(comodel_name='res.user', string='Team Leader', required=True)
    team_members = fields.Many2one(comodel_name='res.user', string='Team Member', required=True)
    booking_start = fields.Date(string='Booking Start')
    booking_end = fields.Date(string='Booking Start')