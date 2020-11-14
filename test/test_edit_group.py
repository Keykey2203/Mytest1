# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_first_group2_name(app, db, check_ui):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="llll"))
    group = random.choice(old_groups)
    group.name = 'Edited'
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, new_groups)

        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    else:
        assert new_groups == old_groups

#def test_edit_first_group2_header(app):
    #old_groups = app.group.get_group_list()
    #if app.group.count() == 0:
        #app.group.create(Group(header="rrrr"))
    #app.group.edit_group2(Group(header="Новый"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
