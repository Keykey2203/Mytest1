

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_info(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.return_to_groups_page()

    def delete_first_group2(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_group2(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        self.fill_info(group)
        wd.find_element_by_name("update").click()

    def fill_info(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()