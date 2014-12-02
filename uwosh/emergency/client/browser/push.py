# handle push notifications

from uwosh.simpleemergency.browser.controlpanel import SimpleEmergencyControlPanelAdapter
from uwosh.simpleemergency.events import SimpleEmergencyModifiedEvent
from uwosh.simpleemergency.config import SUCCESS_MESSAGE
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from uwosh.simpleemergency.config import text_to_test_cypher_with
from uwosh.emergency.client.config import CONFIG
from Acquisition import aq_inner
import rsa
from zope.event import notify
from DateTime import DateTime
import cgi

def get_ip(request):
    """  Extract the client IP address from the HTTP request in proxy compatible way.
    stolen mostly from http://plonemanual.twinapex.fi/serving/http_request_and_response.html
    @return: IP address as a string or None if not available
    """
    ip = ''
    if "HTTP_X_FORWARDED_FOR" in request.environ:
        # Virtual host
        ip = request.environ["HTTP_X_FORWARDED_FOR"]
    elif "HTTP_HOST" in request.environ:
        # Non-virtualhost
        ip = request.environ.get("REMOTE_ADDR", None)

    return ip


class RemoteUpdateEmergencyMessage(BrowserView):
    

    def __call__(self):
        props = getToolByName(self.context, 'portal_properties').uwosh_emergency_client
        
        public_key = {
            'e' : long(props.getProperty('public_key_e')),
            'n' : long(props.getProperty('public_key_n'))
        }
        
        signature = self.request.get('signed_data')
        data = dict(cgi.parse_qsl(rsa.verify(signature, public_key)))
        
        enabled = data['enabled'] == 'True' and True or False
        last_updated = DateTime(data['last_updated'])
        message = data['emergency_message']
        show_on_all_pages = data['show_on_all_pages'] == 'True' and True or False
            
        # look to see if the ip address is valid
        # only do it if they actually specified a list
        # of only accepted valid ips
        user_ip = get_ip(self.request)
        if CONFIG.trusted_ips: # an empty list evals to False
            valid_ip = False
        else:
            valid_ip = True
        for ip in CONFIG.trusted_ips:
            if ip.match(user_ip):
                valid_ip = True
                break
        
        if not valid_ip:
            raise Exception("You are not coming from a valid ip address for this to work. You do not belong here!")
        
        adapter = SimpleEmergencyControlPanelAdapter(self.context)
        
        if adapter.props.last_updated:
            # might not have ever been updated yet.
            current_last_updated = DateTime(adapter.props.last_updated)
            if current_last_updated > last_updated:
                # In case someone intercepted the traffic and tries to replay
                # an emergency message earlier than the previous update
                raise Exception("The message you are trying to update with is earlier than the most recent udpated message! #fail :)")
        
        adapter.emergency_message = message
        adapter.props.last_updated = last_updated.pCommonZ()
        adapter.display_emergency = enabled
        adapter.show_on_all_pages = show_on_all_pages
        notify(SimpleEmergencyModifiedEvent(self.context, self.request))
        return SUCCESS_MESSAGE

        