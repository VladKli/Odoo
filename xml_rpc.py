import xmlrpc.client

url = 'http://localhost:8569'
db = 'o15-learn'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# create course
models.execute_kw(db, uid, password, 'session', 'create', [{'name': 'XML RPC', 'course_id': '1'}])
# get session and number of seats
ids = models.execute_kw(db, uid, password, 'session', 'search', [[[1, '=', 1]]], )
print(models.execute_kw(db, uid, password, 'session', 'read', [ids], {'fields': ['name', 'seats_num']}))
