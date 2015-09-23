# coding: utf-8

from nose.tools import with_setup

import ML
from ML import Object
from ML import Relation

__author__ = 'czhou <czhou@ilegendsoft.com>'


def setup_func():
    ML.init(
        '55d1480960b2430132e9b19e',
        'T2N5aGQxY25vLU9EMkJkdFNSQVY1dw',
    )


class Band(Object):
    pass


class Album(Object):
    pass


def test_create_relation():
    album = Album()
    r = Relation(album, 'band')
    assert r


@with_setup(setup_func)
def test_query_relation():
    album = Album(title='variety')
    band1 = Band(name='xxx')
    band1.save()
    band2 = Band(name='ooo')
    band2.save()

    relation = album.relation('band')
    relation.add(band1)
    relation.add(band2)
    album.save()

    album = ML.Query('Album').get(album.id)
    relation = album.relation('band')
    bands = relation.query().find()
    assert band1.id in [x.id for x in bands]
    assert band2.id in [x.id for x in bands]

    album.destroy()
    band1.destroy()
    band2.destroy()
