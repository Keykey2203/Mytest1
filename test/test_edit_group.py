# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group2_name(app):
    app.group.edit_group2(Group(name="Новый"))


def test_edit_first_group2_header(app):
    app.group.edit_group2(Group(header="Новый"))