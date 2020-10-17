# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact_company(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Мимоза", lastname="Энгельса,36")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="llll", lastname="Ленина,51"))
    app.contact.edit_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_contact_fio(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="Ромашкина", middlename="Зинаида", lastname="Андреевна"))
    #app.contact.edit_contact(Contact(firstname="Иванова", middlename="Мария", lastname="Ивановна"))