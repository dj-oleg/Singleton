import mysql.connector
class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton
class DBConnection(object):

    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="singlton"
        )
        self.cursor = self.db.cursor()

    def __str__(self):
        return 'Database connection object'
        return self.cursor

c1 = DBConnection.Instance()
c2 = DBConnection.Instance()

print("Id of c1 : {}".format(str(id(c1))))
print("Id of c2 : {}".format(str(id(c1))))

print("c1 is c2 ? " + str(c1 is c2))
myresult = DBConnection.__str__
myresult2 = myresult.fetchall()
for x in myresult2:
    print(x)