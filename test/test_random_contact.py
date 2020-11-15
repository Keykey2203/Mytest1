import re
from model.contact import Contact

def test_all_on_home_page(app, db):
    rows_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    rows_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(rows_from_ui)):
        assert rows_from_ui[index].all_phones_from_home_page == merge_phones_like_on_home_page(
            rows_from_db[index])
        assert rows_from_ui[index].all_emails_from_home_page == merge_emails_like_on_home_page(
            rows_from_db[index])
        assert rows_from_ui[index].lastname == rows_from_db[index].lastname.strip()
        assert rows_from_ui[index].firstname == rows_from_db[index].firstname.strip()
        assert rows_from_ui[index].address == rows_from_db[index].address.strip()
        index += 1
    # index = randrange(len(rows)-1)
    # contact_from_home_page = rows[index]
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    # assert contact_from_home_page.address == contact_from_edit_page.address

# def test_random_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "", [contact.email, contact.email2, contact.email3]))




