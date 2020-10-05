# -*- coding: utf-8 -*-

def test_delete_first_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group2()
    app.session.logout()