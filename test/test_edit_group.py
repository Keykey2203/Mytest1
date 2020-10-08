# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group2_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group2(Group(name="Новый"))
    app.session.logout()

def test_edit_first_group2_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group2(Group(header="Новый"))
    app.session.logout()