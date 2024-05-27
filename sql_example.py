from models import *
from repositories import *

if __name__ == '__main__':
    sqlrepo = SQLRepository()
    stud = Student(1,'bbbbbbb','g','уg','f','345','3568776')
    sqlrepo.add(stud)
    print(sqlrepo.get_all(stud.__class__))
    sqlrepo.remove(8,Student)