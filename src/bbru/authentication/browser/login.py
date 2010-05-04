### -*- coding: utf-8 -*- ####################################################
#
#  Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
#
#  This library is free software: you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License.
#
#  This software is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#  for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this software.  If not, see <http://www.gnu.org/licenses/>.
#
#  Project homepage: <http://launchpad.net/ice.control>
#
#  This pagelet is modified browser view based on code of zope.*,
#  Copyright (C) Zope Corporation and Contributors.
#
##############################################################################

from zope import interface, component
from zope.app.publisher.interfaces.http import ILogin
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from zope.authentication.interfaces import IAuthentication
from zope.app.pagetemplate import ViewPageTemplateFile

class Pagelet(object):
    interface.implements(ILogin)

    confirmation = ViewPageTemplateFile('login.pt')
    failed = ViewPageTemplateFile('login_failed.pt')

    def render(self):
        nextURL = self.request.get('nextURL')
        if IUnauthenticatedPrincipal(self.request.principal, False):
            component.getUtility(IAuthentication).unauthorized(
                self.request.principal.id, self.request)
            return self.failed()
        if nextURL is None:
            return self.confirmation()
        self.request.response.redirect(nextURL)
