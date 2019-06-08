# -*- coding: UTF-8 -*-
import os
project_env = 'prod'
if project_env == 'prod':
    from .product import *
elif project_env == 'dev':
    from .develop import *
else:
    from .test import *
