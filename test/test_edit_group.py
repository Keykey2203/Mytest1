# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group2_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="llll"))
    app.group.edit_group2(Group(name="Новый"))


def test_edit_first_group2_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="rrrr"))
    app.group.edit_group2(Group(header="Новый"))