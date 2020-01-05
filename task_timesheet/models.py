# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    date_start = fields.Datetime(
        string='Inicio'
    )
    date_end = fields.Datetime(
        string='Fin'
    )
    state = fields.Selection(selection=[
        ('todo', 'Nuevo'),
        ('doing', 'Iniciado'),
        ('done', 'Terminado')
    ], string='Estado', default='todo')

    def action_start(self):
        if not self.date_start:
            self.date_start = fields.Datetime.now()
        self.state = 'doing'
        self.update({
            'state': 'doing',
            'unit_amount': 0
        })

    def action_restart(self):
        self.update({
            'state': 'todo',
            'unit_amount': 0
        })

    def action_end(self):
        if not self.date_end:
            self.date_end = fields.Datetime.now()
        self.state = 'done'
        self.action_calculate()

    def action_calculate(self):
        result = self.date_end - self.date_start
        self.unit_amount = result.total_seconds() / 3600
