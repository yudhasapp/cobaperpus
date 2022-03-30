from odoo import api, fields, models


class Penerbit(models.Model):
    _name = 'perpus.penerbit'
    _description = 'tabel Penerbit'

    name = fields.Char(string='Nama Penerbit')
    alper = fields.Char(string='Alamat Penerbit')
    noper = fields.Integer(string='No Telp Penerbit')
    
    
