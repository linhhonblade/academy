# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        teachers = http.request.env['academy.teacher']
        return http.request.render('academy.index', {
            'teachers': teachers.search([]),
        })

    @http.route('/academy/<model("academy.teacher"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {'person': teacher})

