Emergency Client
================
This package is a Plone product that is designed to receive push notifications
from another Plone site running the "Emergency Master" product. Once the push
emergency notifications are received, they are displayed on the site exactly
the same way uwosh.simpleemergency works.


Setup
-----

In order for the push notifications to work, you need to setup a public key that
this site will use to handle authentication of the push notifications.

On the master site, a site that has uwosh.emergency.master installed, use a url
similar to `http://www.mysite.com/@@uwosh-emergency-master-public-key` to retrieve
the public key or just go to the `Emergency Notification Sites` control panel page. 
Then on the site that has this product installed, go to 
ZMI -> portal_properties -> uwosh_emergency_client and enter the values for the
`e` and `n` parts of the public key.

And finally, on the master site, you'll need to go to the "Emergency Notification Sites"
control panel page and enter the url of the client sites that have the master site's
public key registered.


Compatibility
-------------

Plone 3 and 4


Uninstall
---------

To uninstall deactivate the product in the plone control panel and also run the import step `Client Emergency Notification Uninstall Profile` in the zmi -> portal_setup -> Import tab.