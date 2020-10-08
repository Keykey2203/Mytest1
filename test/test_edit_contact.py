# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="Игнатьева", photo="C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg", title="2222", middlename="Мария", lastname="Ивановна", nickname="воов", company="Мимоза", address="Луначарского", homepage="222", email="555@mail.ru", email2="666@mail.ru", email3="777@mail.ru", fax="888", home="111", mobile="888888", work="44444", bday="30", bmonth="April", byear="1990", aday="22", amonth="March", ayear="1990", address2="Декабристов", phone2="545", notes="лялял"))
    app.session.logout()