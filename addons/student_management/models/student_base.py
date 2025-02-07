 #-*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api, _

class StudentBase(models.Model):
	_name = 'student.base'
	_description = 'Description module'
	_inherit = ['mail.thread', 'mail.activity.mixin']

 	
	name = fields.Char(string='Name', tracking=True)
	lastname = fields.Char(string='Last name', tracking=True)
	birth_date = fields.Date(string='Birth date', tracking=True)
	matricule = fields.Char(string='Matricule')
	photo = fields.Image(string='Image')
	age = fields.Integer(string="age", compute="age_calc", store=True)


	@api.model
	def create(self, vals):
		if 'company_id' in vals:
			self = self.with_company(vals['company_id'])
		vals['matricule'] = self.env['ir.sequence'].next_by_code('student.base') or 'New'
		result = super(StudentBase, self).create(vals)
		return result
    
	@api.depends('birth_date')
	def age_calc(self):
		if self.birth_date is not False:
			self.age = (datetime.today().date() - datetime.strptime(str(self.birth_date), '%Y-%m-%d').date()) // timedelta(days=365)

   