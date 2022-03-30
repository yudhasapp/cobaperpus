from odoo import api, fields, models
# from odoo.exceptions import ValidationError

class Peminjaman(models.Model):
    _name = 'perpus.peminjaman'
    _description = 'Tabel peminjaman'

    # detailpeminjaman_ids = fields.One2many(
    #     comodel_name='perpus.detailpeminjaman', 
    #     inverse_name='order_id', 
    #     string='Buku')
    

    name = fields.Char(string='No Transaksi', Required=True)
    buku_id = fields.Many2one(comodel_name='perpus.buku', 
                                string='Judul Buku', 
                                required=True)

    # isbn_buku = fields.Char(compute='_compute_isbn_buku', string='ISBN')
    
    # @api.depends('buku_id')
    # def _compute_isbn(self):
    #     for record in self:
    #         record.isbn = self.env['perpus.buku'].search([('id', '=', record.buku_id.id)]).mapped('isbn').isbn

    # def _compute_isbn_buku(self):
    #     isbn_buku = self.env['perpus.buku'].search([('id', '=', self.id)]).mapped('isbn').name
    #     self.isbn_buku = isbn_buku


    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)
    tanggal_pinjam = fields.Datetime('Tanggal Peminjaman',default=fields.Datetime.now())
    tanggal_kembali = fields.Date(string='Tanggal Pengembalian')
    

    # class DetailPeminjaman(models.Model):
    #     _name = 'perpus.detailpeminjaman'
    #     _description = 'New Description'
    
    #     order_id = fields.Many2one(comodel_name='perpus.peminjaman', string='peminjaman')
        
    #     buku_id = fields.Many2one(comodel_name='perpus.buku', string='Buku')
        
    #     name = fields.Char(string='Name')
    #     qty = fields.Integer(string='Quantity')


    # @api.constrains('qty')
    # def _check_stok(self):
    #     for record in self:
    #         aa = self.env['perpus.buku'].search([('stok', '<',record.qty),('id', '=',record.id)])
    #         if aa:
    #             raise ValidationError("Buku Tidak Tersedia")

    # @api.model
    # def create(self,vals):
    #     record = super(Peminjaman, self).create(vals) 
    #     if record.qty:
    #         self.env['perpus.buku'].search([('id','=',record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    
