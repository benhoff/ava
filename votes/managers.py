from django.conf import settings
from django.db import connection, models

try:
    from django.db.models.sql.aggregates import Aggregate
except ImportError:
    supports_aggregates = False
else:
    supports_aggreagates = True

from django.contrib.contenttypes.models import ContentType

if supports_aggregates:
    pass

#https://code.google.com/p/django-voting/source/browse/trunk/voting/managers.py
