from odoo import api, fields, models


class Rak(models.Model):
    _name = 'perpus.rak'
    _description = 'Tabel Rak'

    name = fields.Char(string='Kode Rak')
    locrak = fields.Char(string='Lokasi Rak')
    
