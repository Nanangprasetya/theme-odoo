{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Your name',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
        'views/footer.xml',
        
    ],
    'assets': {
        'web.assets_frontend': [
            '/theme_totorial/static/scss/style.scss',
            '/theme_totorial/static/scss/bootstrap_overridden.scss',
            '/theme_totorial/static/js/totorial_editor.js',
            
        ]
    },
     'images': [
        'static/img/user-1.png'
    ],
}
