#-*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _


class StudentClass(models.Model):
	_name = 'student.class'
	_description = 'Description module'

	name = fields.Char(string='Name')
	student_number = fields.Integer(string='Student number')
	stage= fields.Char(string='Stage')
	old_stud = fields.Integer(compute='_compute_old_stud', string='Number Old Student')
	new_stud = fields.Integer(string='Number New Student')

	@api.depends("student_number", "new_stud")
	def _compute_old_stud(self):
		for record in self:
			record.old_stud = record.student_number - record.new_stud
	
	@api.constrains('student_number')
	def _check_number(self):
		for record in self:
			if record.student_number <= 0:
				raise ValidationError("Number of Student in Class must be over 0 to list it there")

	@api.onchange("name")
	def _onchange_name(self):
		if self.name:
			self.name = self.name + "(Customized)"

	@api.model
	def create_wizard(self, new_stud):
		wizard = self.env['model.wizard'].create({
   
			'new_stud': self.name
   			})
		return{
			'name': _('Model Wizard'),
			'type': 'ir.actions.act_window',
   			'res_model': 'model.wizard',
   			'view_mode': 'form',
   			'res_id': wizard.id,
   			'target': 'new'
		}

		
	