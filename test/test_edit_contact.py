# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact_company(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname="llll", lastname="Ленина,51"))
    contact = random.choice(old_contacts)
    contact.firstname="Мимоза"
    contact.lastname="Энгельса,36"
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    else:
        assert old_contacts == new_contacts


#def test_edit_contact_fio(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="Ромашкина", middlename="Зинаида", lastname="Андреевна"))
    #app.contact.edit_contact(Contact(firstname="Иванова", middlename="Мария", lastname="Ивановна"))