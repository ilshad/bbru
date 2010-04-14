from setuptools import setup, find_packages

setup(name='bbru',
      version='0.1.0',
      description='Open Source Web Service and Community Portal bluebream.ru',
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='bluebream zope russian',
      author='bluebream.ru community',
      author_email='dev@bluebream.ru',
      url='http://bluebream.ru',
      license='Public Domain',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zope.securitypolicy',
                        'zope.component',
                        'zope.annotation',
                        'zope.browserresource',
                        'zope.app.dependable',
                        'zope.app.appsetup',
                        'zope.app.content',
                        'zope.publisher',
                        'zope.app.broken',
                        'zope.app.component',
                        'zope.app.generations',
                        'zope.app.error',
                        'zope.app.interface',
                        'zope.app.publisher',
                        'zope.app.security',
                        'zope.app.form',
                        'zope.app.i18n',
                        'zope.app.locales',
                        'zope.app.zopeappgenerations',
                        'zope.app.principalannotation',
                        'zope.app.basicskin',
                        'zope.app.rotterdam',
                        'zope.app.folder',
                        'zope.app.wsgi',
                        'zope.formlib',
                        'zope.i18n',
                        'zope.app.pagetemplate',
                        'zope.app.schema',
                        'zope.app.container',
                        'zope.app.debug',
                        'z3c.testsetup',
                        'zope.app.testing',
                        'zope.testbrowser',
                        'zope.login',
                        'zope.app.zcmlfiles',

                        'zope.intid',

                        'ice.control',
                        ],
      entry_points = """
      [paste.app_factory]
      main = bbru.startup:application_factory

      [paste.global_paster_command]
      shell = bbru.debug:Shell
      """,
      )
