from odoo import api, fields, models, _

class NamaPesawat(models.Model):
    _name = "nama.pesawat"
    _description = "Nama Pesawat"

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))
    age = fields.Integer(string='age')
    tanggal = fields.Date(string='tanggal')
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
    kota_keberangkatan = fields.Selection([
        ('bandung', 'Bandung'),
        ('surabaya', 'Surabaya'),
        ('samarinda', 'Samarinda'),
        ('banjarmasin', 'Banjarmasin'),
        ('jakarta', 'Jakarta'),
        ('bali', 'Bali')],
        required=True, default='bandung')
    maskapai = fields.Selection([
        ('garuda', 'Garuda'),
        ('lion_air', 'Lion_Air'),
        ('air_asia', 'Air_Asia'),
        ('super_air_jet', 'Super_Air_Jet'),
        ('sriwijaya_air', 'Sriwijaya_Air')],
        required=True, default='garuda')
    kelas_pesawat = fields.Selection([
        ('economy_class', 'Economy_Class'),
        ('bisnis_class', 'Bisnis_Class'),
        ('first_class', 'First_Class')],
        required=True, default='economy_class')
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('success', 'Success'), ('canceled', 'Canceled')], default='draft', string="status")
    image = fields.Binary(string="Penumpang Image" ,max_width=10 ,max_height=10)
    
    @api.model
    def create(self, vals):
        if vals.get('note'):
            vals['note'] = 'New'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('nama.pesawat') or _('New')
        res = super(NamaPesawat, self).create(vals)
        return res
    