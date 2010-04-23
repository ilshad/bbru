# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.app.generations.generations import SchemaManager

pkg = 'bbru.generations'

schemaManager = SchemaManager(minimum_generation=0,
                              generation=0,
                              package_name=pkg)
