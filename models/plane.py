from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date
from odoo.exceptions import UserError

class NamaPesawat(models.Model):
    _name = "nama.pesawat"
    _description = "Nama Pesawat"

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))
    age = fields.Integer(string='age')
    tanggal = fields.Date(string='tanggal')
    
    @api.constrains('tanggal')
    def _check_tanggal(self):
        for record in self:
            if record.tanggal and record.tanggal < fields.Date.today():
                raise UserError("Anda tidak dapat memilih tanggal penerbangan sebelum dari hari ini.")
    
    gender = fields.Selection([
        ('Male', 'male'),
        ('Female', 'female'),
        ('other', 'other')],
        required=True, default='male')
    tujuan_kota = fields.Selection([
        ('bandung', 'Bandung'),
        ('surabaya', 'Surabaya'),
        ('samarinda', 'Samarinda'),
        ('banjarmasin', 'Banjarmasin'),
        ('jakarta', 'Jakarta'),
        ('bali', 'Bali')],
        required=True, default='bali')
    @api.onchange('tujuan_kota', 'kota_keberangkatan')
    def _onchange_tujuan_kota_kota_keberangkatan(self):
        if self.tujuan_kota == self.kota_keberangkatan:
            raise UserError("Kota tujuan dan kota keberangkatan tidak boleh sama!")

    kota_keberangkatan = fields.Selection([
        ('bandung', 'Bandung'),
        ('surabaya', 'Surabaya'),
        ('samarinda', 'Samarinda'),
        ('banjarmasin', 'Banjarmasin'),
        ('jakarta', 'Jakarta'),
        ('bali', 'Bali')],
        required=True, default='bandung')
    @api.onchange('kota_keberangkatan', 'tujuan_kota')
    def _onchange_kota_keberangkatan_tujuan_kota(self):
        if self.kota_keberangkatan == self.tujuan_kota:
            raise UserError("Kota asal dan tujuan tidak boleh sama!")

    maskapai = fields.Selection([
        ('garuda', 'Garuda'),
        ('lion_air', 'Lion Air'),
        ('air_asia', 'Air Asia'),
        ('super_air_jet', 'Super Air Jet'),
        ('sriwijaya_air', 'Sriwijaya Air')],
        required=True, default='garuda')
    kelas_pesawat = fields.Selection([
        ('economy_class', 'Economy Class'),
        ('bisnis_class', 'Bisnis Class'),
        ('first_class', 'First Class')],
        required=True, default='economy_class')
    note = fields.Text(string='Description', default='New Penumpang')
    # state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('success', 'Success'), ('canceled', 'Canceled')], default='draft', string="status")
    state = fields.Selection([ 
        ('inprogress', 'Inprogress'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='inprogress', tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
    
    def action_inprogress(self):
        self.state = 'inprogress'

    def action_cancel(self):
        self.state = 'cancel'
    image = fields.Binary(string="Penumpang Image" ,max_width=10 ,max_height=10)
    
    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New Penumpang'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('nama.pesawat') or _('New')
        res = super(NamaPesawat, self).create(vals)
        return res
    