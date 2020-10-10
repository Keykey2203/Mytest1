# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(company="llll", address2="Ленина,51"))
    app.contact.edit_contact(Contact(company="Мимоза", address="Энгельса,36"))

def test_edit_contact_fio(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ромашкина", middlename="Зинаида", lastname="Андреевна"))
    app.contact.edit_contact(Contact(firstname="Иванова", middlename="Мария", lastname="Ивановна"))