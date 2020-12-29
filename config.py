import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '192.168.12.1',
            'DB_NAME': 'project_development',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_PASS')

        },
        'TARGET_DB': {
            'DB_TYPE': 'oracle',
            'DB_HOST': '192.168.12.1',
            'DB_NAME': 'project_development',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS')
        }
    }
}