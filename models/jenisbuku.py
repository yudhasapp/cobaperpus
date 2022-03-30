from odoo import api, fields, models


class Jenisbuku(models.Model):
    _name = 'perpus.jenisbuku'
    _description = 'Tabel Jenis Buku'

    name = fields.Char(string='Nama Jenis Buku')
