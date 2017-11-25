#!/usr/bin/python3
# -*- coding:ytf-8 -*-
from transwarp.orm import Model,StringField,IntegerField

class Model(dict):
    __metaclass__ = MOdelMetaclass
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict ' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key = True)
    name = StringField()

user = User(id = 123,name = 'Michael')
user.insert()
