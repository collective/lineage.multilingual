from lineage.multilingual.interfaces import IBrowserLayer
from zope.globalrequest import getRequest

def handler(obj, event):
    """ Event handler
    """
    # exit when add-on is not activated:
    if not IBrowserLayer.providedBy(getRequest()):
        return
    print(f"{event.__class__} on object {obj.absolute_url()}")
