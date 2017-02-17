from django.test import TestCase
from app1.models import *


class ModelAttrJoinTestCase(TestCase):
    def setUp(self):
        _t1 = Thing.objects.create(id=1, name='data1')
        _t2 = Thing.objects.create(id=2, name='data2')
        #
        ThingAttr.objects.create(name='attr-1', parent=_t1)
        ThingAttr.objects.create(name='attr-2', parent=_t1)
        #
        ThingAttr2.objects.create(name='attr2-1', parent=_t2.id)
        ThingAttr2.objects.create(name='attr2-2', parent=_t2.id)
        ThingAttr2.objects.create(name='attr2-3', parent=_t2.id)

    def testWithForeignKey(self):
        _t = Thing.objects.get(id=1)
        _qs = ThingAttr.objects.filter(parent=_t)
        for o in _qs:
            print(o)

        print('ThingAttr count = %s' % (len(_qs)))
        print('----')

    def testManualForeignKey(self):
        _t = Thing.objects.get(id=2)
        _qs = ThingAttr2.objects.filter(parent=_t.id)
        for o in _qs:
            print(o)

        print('ThingAttr2 count = %s' % (len(_qs)))
        print('----')
