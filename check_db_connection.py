from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    items = db.get_contacts_whitout_group()
    for item in items:
       print(item)
    print(len(items))
finally:
    pass # db.destroy()