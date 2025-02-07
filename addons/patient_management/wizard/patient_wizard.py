# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from datetime import date


class PatientWizard(models.TransientModel):
    _name = 'patient.wizard'
    _description = 'Wizard to calculate age'

    birth_date = fields.Date(string='Bith date')

    @api.depends('birth_date')
    def calcul_age(self):
        Patient_ids = self.env['patient.base']
        active_id = self.env.context.get('active_id')

        Patient = Patient_ids.search([('id', '=', active_id)])
        birth_date = self.birth_date
        current_date = date.today()
        age = relativedelta(current_date, birth_date).years
        Patient.age = age