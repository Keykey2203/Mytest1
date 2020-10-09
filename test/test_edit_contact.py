# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact_company(app):
    app.contact.edit_contact(Contact(company="Мимоза", address="Энгельса,36"))

def test_edit_contact_fio(app):
    app.contact.edit_contact(Contact(firstname="Иванова", middlename="Мария", lastname="Ивановна"))