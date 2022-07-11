{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Your name',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
        'views/layouts.xml',
        'views/snippets/testimonial.xml',
        'views/options/testimonial_options.xml',
        'views/header.xml',
        'views/footer.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/theme-odoo/static/scss/_variables.scss',
            '/theme-odoo/static/scss/_common.scss',
            '/theme-odoo/static/scss/layouts/_footer.scss',
            '/theme-odoo/static/scss/layouts/_header.scss',
            '/theme-odoo/static/scss/layouts/_front-end.scss',
            '/theme-odoo/static/scss/snippets/_testimonial.scss',

            '/theme-odoo/static/js/totorial_editor.js',
            'https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,500&amp;family=Montserrat&amp;display=swap',
        ]
    },
     'images': [
        'static/img/asset/logo_240.jpg',
        'static/img/asset/tlogo_1024.png',
    ],
}
