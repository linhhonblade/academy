# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

logger = logging.getLogger(__name__)

class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'encapsulate teachers information in academy'

    name = fields.Char(string="Teacher Name")
    biography = fields.Html()

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
    major_ids = fields.Many2many('academy.major', string="Majors")
    
    @api.model
    def _create(self, data_list):
        return super()._create(data_list)

class Course(models.Model):
    _inherit = 'product.template'
    _description = 'encapsulate courses information'
    
    name = fields.Char(string="Course Name")
    
    teacher_id = fields.Many2one('academy.teacher', string="Teacher Name")
    major_ids = fields.Many2many('academy.major', string="Majors")

    @api.onchange('major_ids')
    def _onchange_teacher_id(self):
        teachers = self.env['academy.teacher'].search([('major_ids', 'in', self.major_ids.ids)])
        logger.warning("============")
        logger.warning(teachers.major_ids)
        logger.warning(type(teachers.major_ids))
        if self.major_ids.ids:
            res = {
                'domain':{
                    'teacher_id':[(
                        'id', 'in', teachers.ids,
                    )]
                }
            }
        else:
            return
        return res
        
class Major(models.Model):
    _name = 'academy.major'
    _description = "encapsulate majors information"
    
    name = fields.Char(string="Major Name")