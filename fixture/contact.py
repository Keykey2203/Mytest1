from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_secondary(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def fill_aday(self, contact):
        wd = self.app.wd
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def fill_bday(self, contact):
        wd = self.app.wd
        self.change_select_value("bmonth", contact.bmonth)
        self.change_select_value("bday", contact.bday)
        self.change_field_value("byear", contact.byear)

    def fill_contacts_info(self, contact):
        wd = self.app.wd
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def fill_company_info(self, contact):
        wd = self.app.wd
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def fill_title(self, contact):
        wd = self.app.wd
        self.change_field_value("title", contact.title)

    def fill_fio(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_file_value("photo", contact.photo)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("a[href='edit.php?id=%s']" % id)[0].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def move_contact_to_group(self, contact_id, group_id):
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        self.move_to_group(group_id)

    def move_to_group(self, group_id):
        wd = self.app.wd
        form = wd.find_element_by_css_selector("form[name='MainForm']")
        Select(form.find_element_by_css_selector("select[name='to_group']")).select_by_value(str(group_id))
        form.find_element_by_css_selector("input[name='add']").click()

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        self.submit_new_contact()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_fio(contact)
        self.fill_title(contact)
        self.fill_company_info(contact)
        self.fill_contacts_info(contact)
        self.fill_bday(contact)
        self.fill_aday(contact)
        self.fill_secondary(contact)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_file_value(self, field_name, text):
        wd = self.app.wd
        if text != "" and text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, select_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(select_name).click()
            Select(wd.find_element_by_name(select_name)).select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            table = wd.find_elements_by_css_selector("table#maintable")[0]
            rows = table.find_elements_by_css_selector("tr[name='entry']")
            for row in rows:
                cells = row.find_elements_by_css_selector("td")
                id = row.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name ("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email,
                       email2=email2, email3=email3, home=home, mobile=mobile, work=work, phone2=phone2)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def is_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_group(group_id)
        items = wd.find_elements_by_css_selector("input[name='selected[]'][value='%s']" % contact_id)
        if len(items) > 0:
            return True
        else:
            return False

    def is_contact_not_in_group(self, contact_id, group_id):
        if self.is_contact_in_group(contact_id, group_id):
            return False
        else:
            return True

    def open_group(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_css_selector("select[name='group']")).select_by_value(group_id)

    def remove_contact_from_group(self, contact_id, group_id):
        self.open_group(group_id)
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_css_selector("input[name='remove']").click()