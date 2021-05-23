# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group2(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given agroup list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When a add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('When a I add a group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            def clean(group):
                return Group(id=group.id, name=group.name.strip())
            new_groups = map(clean, new_groups)

            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

