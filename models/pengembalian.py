from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'perpus.pengembalian'
    _description = 'Pengembalian Buku'

    name = fields.Char(compute='_compute_nama_penyewa', string='Nama Costumer')
    peminjaman_id = fields.Many2one(comodel_name='perpus.peminjaman', string='No. Transaksi', required=True)
    
    @api.depends('peminjaman_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.name = self.env['perpus.peminjaman'].search([('id', '=', record.peminjaman_id.id)]).mapped('pemesan').name

    tgl_kembali = fields.Date(string='', default=fields.Date.today())
        
    @api.model
    def create(self,vals):
        record = super(Pengembalian, self).create(vals) 
        if record.tgl_kembali:
            self.env['perpus.peminjaman'].search([('id','=',record.peminjaman_id.id)]).write({'sudah_kembali':True})         
            return record

    @api.model
    def unlink(self):
        for xx in self:
            self.env['perpus.peminjaman'].search([('id','=',xx.peminjaman_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()
   
        
            