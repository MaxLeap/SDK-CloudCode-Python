# coding: utf-8

from ML import Object
from ML import utils

__author__ = 'czhou <czhou@ilegendsoft.com>'


def test_encode():
    Foo = Object.extend('Foo')
    obj = Foo()
    assert utils.encode(obj) == {
        'className': 'Foo',
        '__type': 'Pointer',
        'objectId': None,
    }


def test_util():
    obj = Object.extend('Foo')()

    def callback(o):
        callback.count += 1
        if callback.count == 1:
            assert o == {}
        elif callback.count == 2:
            assert o == obj

    callback.count = 0

    utils.traverse_object(obj, callback)

    assert callback.count == 2
