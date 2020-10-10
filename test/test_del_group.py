# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group2(app):
    if app.group.count() == 0:
        app.group.create(Group(name="llll"))
    app.group.delete_first_group2()