# -*- encoding: utf-8 -*-

__all__ = [
  'get_last_events'
]

import os

from readlogs_generic import GenericLogReader

def get_last_events(count=10, includes=[], excludes=[]):
    for d in ['/var/log']:
        if os.path.isdir(d):
            return GenericLogReader(d).get_last_events(count, includes, excludes)
