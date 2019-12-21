from odoo import models, fields, api


class resPartner(models.Model):
    _inherit='res.partner'
    _name = 'res.partner'

    servidor = fields.Boolena(string='Es Servidor', default=False)
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')


class actividadJuventud(models.Model):
    _name = 'actividad.juventud'
    _description = 'Actividad Juventud'

    name = fields.Char(string='Nombre de Actividad')
    estado = fields.Boolean(string='')
    

class AsistenciaJuventud(models.Model):
    _name = 'asistencia.juventud'
    _description = 'Asistencia Juventud'


    estado = fields.Selection(
        string='Estado',
        selection=[
            ('asistencia','Asistencia'),
            ('inasistencia','No Asistencia'),
            ('justificado','Justificado')
        ])