# -*- coding: utf-8 -*-
from contextlib import nullcontext
from odoo import api, fields, models
from odoo.exceptions import UserError


class StudentInformation(models.Model):
    _name = "student.information"  # nameofTable
    _description = "Student Management"

    name = fields.Char(string=("Họ và Tên"), required=True)
    birthday = fields.Date(string=("Ngày sinh"), required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)
    subject_list = fields.Many2many("subject.information", 'relation_subject_student', 'student_id', 'subject_id',
                                    string="Bảng quan hệ giữa môn học và học sinh")
    school_id = fields.Many2one("school.information", string="Trường học")
    fee_per_semester = fields.Float(related="school_id.tuition", string="Học phí kỳ 1")
    semester = fields.Integer(compute="_auto_compute_semester", string="Số học kỳ")
    grade = fields.Char(related="class_id.grade", string="Khối")
    currency_id = fields.Many2one("res.currency", string="Đơn vị")
    tuition = fields.Monetary(compute="_auto_compute_tuition", string="Tổng số học phí")
    # ref_id = fields.Reference()

    @api.depends("grade")
    def _auto_compute_semester(self):
        for rc in self:
            if rc.grade == "10":
                rc.semester = 2
            elif rc.grade == "11":
                rc.semester = 4
            else:
                rc.semester = 6

    @api.depends("semester", "fee_per_semester")
    def _auto_compute_tuition(self):
        for rc in self:
            rc.tuition = rc.semester * rc.fee_per_semester

    def write(self, values):
        # function write get all values of model
        rtn = super(StudentInformation, self).write(values)
        if not self.subject_list:
            raise UserError("Bạn cần chọn môn học")
        return rtn

# class ClassInformation(models.Model):
#     _inherit = 'class.information'
#     student_list = fields.One2many('student.information', 'class_id', string="Danh sách học sinh")

class SubjectInformation(models.Model):
    _name = "subject.information"  # nameofTable
    _description = "Subject Management"

    name = fields.Char(string=("Tên môn học"), required=True)
    author = fields.Char(string=("Tác giả"), required=True)
