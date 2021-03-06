#-*- coding: utf-8 -*-
from datetime import datetime
from tzlocal import get_localzone
import os


def iso_to_datetime(iso):
    return datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S%z')


def get_file_modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t, tz=get_localzone())

def get_free_memory():
    with open('/proc/meminfo', 'r') as mem:
        total, free, buffers, cached = [int(next(mem).split()[1])
                                        for x in xrange(4)]
        return free + cached
