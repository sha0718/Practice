from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    name = fields.Char(string='Name')

    def my_method(self):
        # Create a new record
        new_record = self.create({'name': 'New Record'})

        # Read records
        records = self.search([('name', '=', 'New Record')])

        # Update the record
        if records:
            records.write({'name': 'Updated Record'})

        # Delete the record
        records.unlink()
