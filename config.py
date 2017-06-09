# coding=utf-8
# Author: rsmith
# Copyright ©2016 iProspect, All Rights Reserved

import os
from logging.config import dictConfig as logger_config

log_dir = os.getenv('CWA_LOG_DIR', 'logs')

logger_config({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(log_dir, 'creativewebadmin.log'),
            'when': 'midnight'
        },
        'stdout': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'stdout'],
            'level': 'DEBUG',
            'propagate': True
        },
        # 'werkzeug': {
        #     'handlers': ['default', 'stdout'],
        #     'level': 'INFO',
        #     'propagate': True
        # },
        'requests': {
            'handlers': ['default', 'stdout'],
            'level': 'WARN',
            'propagate': True
        },
    }
})
