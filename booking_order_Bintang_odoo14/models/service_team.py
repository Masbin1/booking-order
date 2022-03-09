from odoo import api, fields, models


class Service_team(models.Model):
    _name = 'service.team'
    _description = 'Team Service'

    team_name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one(comodel_name='res.user', string='Team Leader', required=True)
    team_members = fields.Many2many(comodel_name='res.user', string='Team Member', required=True)