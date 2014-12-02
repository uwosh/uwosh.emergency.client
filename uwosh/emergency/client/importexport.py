import rsa

from Products.CMFCore.utils import getToolByName
from uwosh.simpleemergency.utils import disable_emergency

se_default_profile = 'profile-uwosh.simpleemergency:default'

def install(context):
    
    if not context.readDataFile('uwosh.emergency.client.txt'):
        return
    
    site = context.getSite()
    
    qi = getToolByName(site, 'portal_quickinstaller')
    if qi.isProductInstalled('uwosh.simpleemergency') or qi.isProductInstalled('uwosh.emergency.master'):
        raise Exception('You can not install uwosh.simpleemrgency or uwosh.emergency.master on the same site as the client.')
    
    portal_setup = getToolByName(site, 'portal_setup')
    portal_setup.runImportStepFromProfile(se_default_profile, 'propertiestool')
    portal_setup.runImportStepFromProfile(se_default_profile, 'cssregistry')
    disable_emergency(site) # disable by default