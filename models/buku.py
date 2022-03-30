from email.policy import default
from odoo import api, fields, models


class Buku(models.Model):
    _name = 'perpus.buku'
    _description = 'Tabel Buku'

    name = fields.Char(string='Judul Buku')
    isbn = fields.Char(string='ISBN')
    
    jenisbuku_id = fields.Many2one(comodel_name='perpus.jenisbuku', 
                                string='Jenis Buku', 
                                required=True)  
    penulis = fields.Char(string='Nama Penulis')
    penerbit_id = fields.Many2one(comodel_name='perpus.penerbit', 
                                string='Penerbit', 
                                required=True)
    #terbit = fields.Date(string='Tahun Terbit', default = fields.Date.year())
    thnterbit = fields.Char(string='Tahun Terbit')
    rak_id = fields.Many2one(comodel_name='perpus.rak', 
                                string='Rak', 
                                required=True)
    stok = fields.Integer(string='Stok')
    
    
    
