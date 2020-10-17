# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_first_group2_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="llll"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Новый")
    group.id = old_groups[index].id
    app.group.edit_group2_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group2_header(app):
    #old_groups = app.group.get_group_list()
    #if app.group.count() == 0:
        #app.group.create(Group(header="rrrr"))
    #app.group.edit_group2(Group(header="Новый"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
