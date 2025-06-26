# -*- coding: utf-8 -*-
from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    execute_activity_ids = fields.Many2many(
        "project.task.execute.activity",
        string="Ejecutante"
    )

class ExecuteActivity(models.Model):  # Usé la convención PascalCase para el nombre de la clase
    _name = "project.task.execute.activity"

    name = fields.Char(string="Ejecutante")  # Incluí el argumento 'string' para mantener consistencia
