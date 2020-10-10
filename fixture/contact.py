from selenium.webdriver.support.ui import Select

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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        self.submit_new_contact()

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
