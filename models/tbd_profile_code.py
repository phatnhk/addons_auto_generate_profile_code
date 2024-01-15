import logging
from odoo import fields, models
from odoo.exceptions import UserError, AccessError, ValidationError

class TbdProfileCode(models.Model):
    _inherit = 'crm.lead'

    name = fields.Char(default="New Lead")  # Giá trị mặc định cho trường name

    selected_count = fields.Integer(
        string="Số lượng đã chọn",
        compute='_compute_selected_count',
        store=True,
    )

    def _compute_selected_count(self):
        for lead in self:
            record_ids = self._context.get('active_ids')
            selected_leads = self.env['crm.lead'].browse(record_ids)
            lead.selected_count = len(selected_leads)
            logging.info(f'Hồ sơ đã chọn: {lead.selected_count}.')

    def action_generate_profile_code(self):
        for lead in self:
            record_ids = self._context.get('active_ids')
            selected_leads = self.env['crm.lead'].browse(record_ids)
            lead.selected_count = len(selected_leads)
            logging.info(f'Hồ sơ đã chọn: {lead.selected_count}.')
        if not self.name:
            self.name = "New Lead"  # Đặt giá trị mặc định nếu trường name không được điền
        raise UserError("Bạn đã quên chọn!")