# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group2(app):
    app.group.create(Group(name="333", header="333", footer="3333"))


def test_add_empty_group2(app):
    app.group.create(Group(name="", header="", footer=""))
