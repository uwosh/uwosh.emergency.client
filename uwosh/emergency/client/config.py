from zope.i18nmessageid import MessageFactory
mf = MessageFactory('uwosh.emergency.client')

from recipe import settings_file_name
from ZConfig.loader import ConfigLoader
from os import path
from Globals import INSTANCE_HOME

from ZConfig.datatypes import Registry
import ZConfig

import fnmatch, re

_this_dir = path.dirname(path.abspath(__file__))
schema_file = path.join(_this_dir, "config-schema.xml")
schema = ZConfig.loadSchema(schema_file)

class DefaultConfig(object):
    trusted_ips = []

try:
    CONFIG, hanlders = ZConfig.loadConfig(schema, path.join(INSTANCE_HOME, 'etc', settings_file_name))
    
    # enable wild card matching on domains
    CONFIG.trusted_ips = [re.compile(fnmatch.translate(d)) for d in CONFIG.trusted_ips.split(' ')]
except:
    CONFIG = DefaultConfig()

