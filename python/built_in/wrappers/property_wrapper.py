"""
Make callback functions on a member of class in case of get, set, del.
"""

import uuid

class User1:
    def __init__(self):
        self._id = uuid.uuid4()
    def get_id(self):
        return self._id
    def set_id(self, *args):
        print('warning! changing id is not permitted except authorized methods')
    def del_id(self):
        print('reissuing the user id')
        self._id = uuid.uuid4()
    id = property(get_id, set_id, del_id, "unique id for user")
    

class User2:
    def __init__(self):
        self._id = uuid.uuid4()

    @property
    def id(self):
        "unique id for user"
        return self._id

    @id.setter
    def id(self, *args):
        print('warning! changing id is not permitted except authorized methods')
    @id.deleter
    def id(self):
        print('reissuing the user id')
        self._id = uuid.uuid4()

mode = 1

u1 = User1()

print(f'user id of u1 is {u1.id}')
print('trying to change user id of u1'); u1.id = 33
print('trying to remove user id of u1'); del u1.id; print(f'user id of u1 is {u1.id}')

print('--------------------------------------------------------------')

u2 = User2()

print(f'user id of u1 is {u2.id}')
print('trying to change user id of u1'); u2.id = 33
print('trying to remove user id of u1'); del u2.id; print(f'user id of u1 is {u2.id}')

"Note: setter, deleter of @id should have same name as id"
