# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group2(Group(name="Новый", header="Новый", footer="Новый"))
    app.session.logout()