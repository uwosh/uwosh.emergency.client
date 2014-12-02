from zope.interface import Interface, Attribute
from zope import schema
from uwosh.emergency.client.config import mf as _

class IUWOshEmergencyClientLayer(Interface):
    """Marker interface that defines a browser layer
    """