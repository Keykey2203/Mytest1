# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
    else:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_to_group(app, db, json_contacts, check_ui):
    contact = Contact()
    contacts_whitout_group = db.get_contacts_whitout_group()
    if len(contacts_whitout_group) == 0:
        app.contact.create(json_contacts[0])
        contact = db.get_contacts_whitout_group()[0]
    else:
        contact = random.choice(contacts_whitout_group)
    group = random.choice(db.get_group_list())
    app.contact.move_contact_to_group(contact.id, group.id)
    if check_ui:
        assert app.contact.is_contact_in_group(contact.id, group.id) == True
    else:
        assert contact in db.get_contacts_in_group(group)


def test_remove_contact_from_group(app, db, json_contacts, check_ui):
    group = random.choice(db.get_group_list())
    contacts_in_group = db.get_contacts_in_group(group)
    contact = Contact()
    if len(db.get_contacts_in_group(group)) == 0:
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        if len(contacts_not_in_group) == 0:
            app.contact.create(json_contacts[0])
            contact = db.get_contacts_not_in_group(group)
        else:
            contact = random.choice(contacts_not_in_group)
        app.contact.move_contact_to_group(contact.id, group.id)
        contact = db.get_contacts_in_group(group)[0]
    else:
        contact = contacts_in_group[0]

    app.contact.remove_contact_from_group(contact.id, group.id)
    if check_ui:
        assert app.contact.is_contact_not_in_group(contact.id, group.id) == True
    else:
        assert contact in db.get_contacts_not_in_group(group)