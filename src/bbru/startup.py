import zope.app.wsgi

def application_factory(global_conf):
    zope_conf = global_conf['zope_conf']
    return zope.app.wsgi.getWSGIApplication(zope_conf)
