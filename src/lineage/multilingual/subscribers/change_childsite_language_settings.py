from lineage.multilingual.interfaces import IBrowserLayer
from lineage.multilingual.utils import get_current_context
from plone.app.multilingual.interfaces import IPloneAppMultilingualInstalled
from zope.component.hooks import getSite
from zope.globalrequest import getRequest


def handler(proxy, settings):
    """Taken from plone.app.multilingual.subscriber
    and modified to setup the multilingual configuration
    in the LRFs inside the current childsite.
    """
    if settings.record.__name__ != "plone.available_languages":
        return
    request = getRequest()

    # We can't restrict subscribers to be run when some browser layer
    # is provided, so we check it here
    #
    if IPloneAppMultilingualInstalled.providedBy(request) and IBrowserLayer.providedBy(
        request
    ):
        # Now try to get the current context and apply the settings there
        context = get_current_context()
        if context is not None:
            # The import is added here to avoid circular import errors
            from plone.app.multilingual.browser.setup import SetupMultilingualSite

            setup_tool = SetupMultilingualSite()
            setup_tool.setupSite(context)

    elif IPloneAppMultilingualInstalled.providedBy(request):
        # In case our product is not installed, behave like the p.a.multilingual
        # subscriber.
        # This is done like this because we are unconfiguring the original subscriber
        # because it clashes its behavior with ours.

        # The import is added here to avoid circular import errors
        from plone.app.multilingual.browser.setup import SetupMultilingualSite

        setupTool = SetupMultilingualSite()
        portal = getSite()
        setupTool.setupSite(portal)

    return
