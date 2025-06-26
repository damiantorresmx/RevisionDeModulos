# -*- coding: utf-8 -*-
from odoo import models, fields


class ProjectRRHH(models.Model):
    _inherit = 'project.task'

    # Variables de Recursos Humanos
    vac_date_emition = fields.Date(string="Fecha de Emisión de la autorización")
    vac_date_begin = fields.Date(string="Fecha de inicio de la toma de vacaciones")
    vac_date_end = fields.Date(string="Fecha de terminación de la toma de vacaciones")
    vac_days = fields.Integer(string="Total de Días de vacaciones tomadas")
    vac_taken = fields.Date(string="Día de vacaciones tomadas")
    vac_changed = fields.Date(string="Día de vacaciones tomadas a cambio")
    antiquity_date = fields.Date(string="Día de inicio laboral")
    
    # Permiso con/sin goce de sueldo
    permission_datebegin = fields.Date(string="Fecha de inicio de ausencia solicitada")
    permission_dateend = fields.Date(string="Fecha de terminación de la ausencia")
    return_work = fields.Date(string="Día de retorno laboral")
    concept_permission = fields.Text(string="Motivo de la solicitud")

    # Toma de tiempo x horas
    permission_day = fields.Datetime(string="Fecha de inicio de permiso por horas")
    timereturn_work = fields.Datetime(string="Día de retorno laboral")
    hours_taken = fields.Integer(string="Total de horas tomadas")
    concept_permissiontime = fields.Text(string="Motivo de la solicitud de uso de tiempo por horas")

    




