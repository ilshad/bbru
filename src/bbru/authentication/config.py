# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

import zope.event
import zope.schema
import zope.interface
import z3c.configurator
import zope.pluggableauth
from zope.security.proxy import getObject
from zope.authentication.interfaces import IAuthentication
from zope.lifecycleevent import ObjectCreatedEvent, ObjectModifiedEvent
from zope.app.authentication.principalfolder import (PrincipalFolder,
                                                     InternalPrincipal)
from zope.app.authentication.groupfolder import (GroupFolder,
                                                 GroupInformation)
from zope.securitypolicy.interfaces import (IPrincipalRoleManager,
                                            IPrincipalPermissionManager)

class AuthenticationConfigurator(z3c.configurator.ConfigurationPluginBase):
    """ При использовании `стандартных` средств, доступных из
    пакетов ztk и zopeapp, все кодирование аутентификации в BlueBream
    сводится к установке готовых локальных компонент.

    Т.е. можно вообще не кодировать, а поставить через
    административный интерфейс. Но мы фиксируем порядок манипуляций,
    описав их в конфигураторе.
    """

    def __call__(self, *args):
        site = getObject(self.context)
        sm = site.getSiteManager()

        # устанавливаем утилиту аутентификации
        if u'authentication' not in sm:
            pau = zope.pluggableauth.PluggableAuthentication(prefix='bbru.')
            zope.event.notify(ObjectCreatedEvent(pau))
            sm[u'authentication'] = pau
            sm.registerUtility(pau, IAuthentication)

        pau = sm.getUtility(IAuthentication)

        # устанавливаем в утилиту аутентификации
        # стандартный контейнер для пользователей
        if u'principals' not in pau:
            plugin = PrincipalFolder(prefix='principal.')
            zope.event.notify(ObjectCreatedEvent(plugin))
            pau[u'principals'] = plugin
            pau.authenticatorPlugins += (u'principals',)
            zope.event.notify(ObjectModifiedEvent(pau))

        # устанавливаем в утилиту аутентификации
        # стандартный контейнер для групп пользователей
        if u'group' not in pau:
            groupfolder = GroupFolder(prefix='group.')
            zope.event.notify(ObjectCreatedEvent(groupfolder))
            pau[u'group'] = groupfolder
            pau.authenticatorPlugins += (u'group',)
            zope.event.notify(ObjectModifiedEvent(pau))

        groupfolder = pau[u'group']
        roles = IPrincipalRoleManager(site)

        # создаем одну предустановленную группу
        if u'members' not in groupfolder:
            group = GroupInformation(title=u'members')
            zope.event.notify(ObjectCreatedEvent(group))
            groupfolder[u'members'] = group
            roles.assignRoleToPrincipal('bbru.Member', 'bbru.group.members')

        # конфигрируем утилиту подключаемой аутентификации так, чтобы
        # использовать сессии для хранения удостоверений безопасности
        if u'Session Credentials' not in pau.credentialsPlugins:
            pau.credentialsPlugins += (u'Session Credentials',)

class ICreateUser(zope.interface.Interface):
    """Этот интерфейс используется для генерации формы конфигуратора ниже.
    """

    title = zope.schema.TextLine(
        title=u"Title")

    login = zope.schema.TextLine(
        title=u"Login")

    password = zope.schema.Password(
        title=u"Password")

    roles = zope.schema.List(
        title=u'Site roles',
        value_type=zope.schema.TextLine(
            title=u'role'),
        unique=True)
    
class CreateUserConfigurator(z3c.configurator.SchemaConfigurationPluginBase):
    """Этот конфигуратор нужен для того, чтобы:

    - во время разработки на чистых базах данных каждый раз не создавать
    пользователей врчную - устанешь кликать мышой;

    - на продакшн экземпляре системный пользователь включается только
    один (первый) раз. После этого нужно иметь администратора,
    зарегистрированного локально.

    Этот конфигуратор - с формой. Не будем делать его зависимостью для
    основного, чтобы он не заставлял администартора каждый раз при
    апгрейде сайта заполнять свою форму.
    """

    schema = ICreateUser
    dependencies = ('_initialize', 'authentication')

    def __call__(self, data):
        self.verify(data)

        site = getObject(self.context)
        sm = site.getSiteManager()

        self.create_user(
            site, sm, {'login': data.get('login'),
                       'password': data.get('password'),
                       'title': data.get('title')},
            site_roles=data.get('roles'))

    def create_user(self, site, sm, data,
                          site_roles=(), site_permissions=(),
                          prefix='bbru.principal.', folder_key=u'principals'):
        auth = sm.getUtility(IAuthentication)
        principalfolder = auth[folder_key]
        key = data['login'] # convenient

        principal = InternalPrincipal(
            data['login'], data['password'],
            data.get('title') or data['login'].title(),
            data.get('description') or u'',
            data.get('passwordManagerName') or 'SSHA')

        if key not in principalfolder:
            principalfolder[key] = principal

            roles = IPrincipalRoleManager(site)
            for role in site_roles:
                roles.assignRoleToPrincipal(role, prefix + data['login'])

            permissions = IPrincipalPermissionManager(site)
            for permission in site_permissions:
                permissions.grantPermissionToPrincipal(
                    permission, prefix + data['login'])
