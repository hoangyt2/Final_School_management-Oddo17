# -*- coding: utf-8 -*-
from contextlib import nullcontext

import re
from odoo import api, fields, models
from odoo.exceptions import UserError


class ClassInformation(models.Model):
    _name = "class.information"  # nameofTable
    _description = "Class Management"

    # Moi quan he giua Truong va lop va quan he 1-n (1 truong - nhiều lớp)
    name = fields.Char(string=("Tên lớp"), required=True)
    grade = fields.Char(compute="_auto_compute_grade", string=("Tên khối"), required=True)
    mainTeacher = fields.Char(string=("GVCN"), required=True)
    school_id = fields.Many2one("school.information", string="Trường", required=True)
    student_list = fields.One2many("student.information", 'class_id', string="Danh sách học sinh", store=True)
    address = fields.Text(related="school_id.address", store=True, string="Địa chỉ trường")

    # function compute grade
    @api.depends("name")
    def _auto_compute_grade(self):
        for rc in self:
            if rc.name == False:
                rc.grade = ''
            else:
                # rc.grade = ''.join(list(rc.name)[0:2])
                pos_Alpha = re.search("[a-zA-Z]", rc.name).start()
                rc.grade = rc.name[:pos_Alpha]

# class SchoolInformation(models.Model):
#     _inherit = 'school.information'
#     class_list = fields.One2many('class.information', 'school_id', string="Danh sách lớp")
