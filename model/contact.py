from sys import maxsize

class Contact:


    def __init__(
            self,
            firstname=None,
            middlename=None,
            lastname=None,
            nickname=None,
            company=None,
            address=None,
            homepage=None,
            email=None,
            email2=None,
            email3=None,
            fax=None,
            home=None,
            mobile=None,
            work=None,
            bday=None,
            bmonth=None,
            byear=None,
            aday=None,
            amonth=None,
            ayear=None,
            address2=None,
            phone2=None,
            notes=None,
            title=None,
            photo=None,
            id=None,
        ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homepage = homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.fax = fax
        self.home = home
        self.mobile = mobile
        self.work = work
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.title = title
        self.photo = photo
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int (self.id)
        else:
            return maxsize
