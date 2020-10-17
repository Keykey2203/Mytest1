# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Игнатьева", photo="C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg", title="354235", middlename="Екатерина", lastname="Сергеевна", nickname="Катя", company="Ромашка", address="Декабристов", homepage="123", email="123@mail.ru", email2="132@mail.ru", email3="123@mail.ru", fax="122", home="323", mobile="833234", work="23232", bday="22", bmonth="March", byear="1992", aday="12", amonth="April", ayear="1992", address2="Декабристов", phone2="545", notes="лялял")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", title="", middlename="", photo="", lastname="", nickname="", company="", address="", homepage="", email="", email2="", email3="", fax="", home="", mobile="", work="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




