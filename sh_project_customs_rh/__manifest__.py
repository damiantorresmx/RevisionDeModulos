
{
    'name': 'Projects: Extra Fields anf print forms',
    'category': 'Customs ',
    'sequence': 1,
    'author': 'Damian Veniu',
    'version': '1.0',
    'description': """""",
    'depends': [
        'base', 
        'project'
    ],
    'data': [
        'views/project_rrhh.xml',
        'views/project_task_views.xml',
        'security/ir.model.access.csv',
        'security/res_group.xml'
    ],
    'installable': True,
    'application': True,
    'external_dependencies': {
    },
    'license': 'LGPL-3',
}
