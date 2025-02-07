from odoo import models, fields, api, _


class ModelWizard(models.TransientModel):
	_name = 'model.wizard'
	_description = 'Model Wizard'
	new_stud = fields.Integer(string="Number")

	@api.model
	def create_wizard(self, new_stud):
		wizard = self.env['model.wizard'].create({
   
			'new_stud': self.name
   			})
		

	@api.model
	def action_done(self):
		records = self.env['model.wizard'].browse(self.env.context.get('active_ids'))
		for rec in records: 
			rec.write({'state':'done'})	

	