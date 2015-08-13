import time

from openerp import SUPERUSER_ID
from openerp.osv import fields, osv
from datetime import datetime, date
import time

class project_gantt(osv.osv):
    _name ='project.gantt'
    _description = 'Project Gantt'
    _rec_name = "user_id"
    #_inherit ="project.task"
    def _progress_rate(self, cr, uid, ids, date_starting,date_ending, args, context=None):
        res = {}
        for date1 in self.browse(cr, uid, ids, context=context):
            res[date1.id] = (datetime.strptime(date1.date_ending,"%Y-%m-%d") - datetime.strptime(date1.date_starting,"%Y-%m-%d") ).days or False
        print "res!!!!!!!!!!!!!!!!!!!!!!!!!!",res,type(res)
        return res
        
        
    _columns = {
        'date_starting': fields.date('Starting Date'),
        'date_ending': fields.date('Ending Date'),
        'user_id':fields.many2one('res.users','User'),
        'progress_rates': fields.function(_progress_rate, string='Progress', type='char',store=True),
        }
        
#class project_task_new(osv.osv):
 #   _inherit ="project.task"
  #  _columns = {
   #     'user_id':fields.many2one('res.users','user'),
    #            }
