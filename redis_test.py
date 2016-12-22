
import redis
import random

#name_group = {'name1':'kate', 'name2':'sara', 'name3':'john', 'name4':'yuki'}

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def update_redis(key, value):
    r.set(key,value)
    print "update_redis...key:",key, "value:",value


def show_data(key, value):
    print "calling show_data..."
    print "key:",key,"value:",value
    print "end show_data..."


def get_data_from_mysql(key):
    print "Searching mysql.....key:",key
    has_data = random.randrange(2)
    if has_data:
        print "mysql search success...."
        m_data = {'name1':"kate", "name2":"sara","name3": "johb"}
        print m_data
        return m_data
    else:
        print "mysql search failed , no such data:",key
        return None


def get_data_from_redis(key):
    print "calling get_data_from_redis..."
    value = r.get(key)
    if value:
        print "redis search success...", key
        return value
    else:
        print "redis search failed...", key
        return None


key = "name_groupxxx"

result = get_data_from_redis(key)
if result:
    show_data(key,result)
else:
    ret = get_data_from_mysql(key)
    if ret:
        show_data(key,ret)
        update_redis(key,ret)

#r.set("test","123")
#print dir(r)
#print r.get("test")
#r.delete("test")
#print r.get("test")
#print r.keys()
