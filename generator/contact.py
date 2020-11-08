from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_image():
    list = [
        "C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg",
        "C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg",
        "C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg",
        "C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg",
        "C:\\Users\\79120\\PycharmProjects\\Mytest1\\scale_1200-15.jpg",
    ]
    return list[random.randrange(len(list))]


def random_email():
    postfix = ["ru", "com", "org", "net"]
    name = random_string("", 10)
    domain = random_string("", 10)
    return name + "@" + domain + "." + postfix[random.randrange(len(postfix))]


def random_day():
    return str(random.randrange(30))

def random_month():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[random.randrange(len(months))]

def random_year():
    return random.randint(1990, 2020)


def random_phone():
    return "".join([random.choice(string.digits) for i in range(11)])


testdata = [Contact(firstname="", title="", middlename="", photo="", lastname="", nickname="", company="", address="",
                    homepage="", email="", email2="", email3="", fax="", home="", mobile="", work="", bday="", bmonth="-",
                    byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), photo=random_image(),
          title=random_string("title", 10), middlename=random_string("middlename", 10),
          lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
          company=random_string("company", 10), address=random_string("address", 10),
          homepage=random_string("homepage", 10), email=random_email(),
          email2=random_email(), email3=random_email(),
          fax=random_string("fax", 10), home=random_phone(),
          mobile=random_phone(), work=random_phone(),
          bday=random_day(), bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
          address2=random_string("address2", 10), phone2=random_phone(), notes=random_string("notes", 10))
    for i in range(5)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

