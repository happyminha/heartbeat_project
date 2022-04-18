import pymysql


class RentVo:
    def __init__(self, aed_name=None, rental_id=None, location=None, r_start_date=None, r_end_date=None, r_check=None,
                 r_num=None):
        self.aed_name = aed_name
        self.rental_id = rental_id
        self.location = location
        self.r_start_date = r_start_date
        self.r_end_date = r_end_date
        self.r_check = r_check
        self.r_num = r_num

    def __str__(self):
        return self.aed_name + ' / ' + self.rental_id + ' / ' + self.location + ' / ' + self.r_start_date + ' ~ ' + self.r_end_date + ' / ' + self.r_check + ' / ' + self.r_num


class RentDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='heartbeat_project',
                                    charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, r):
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into rental(aed_name, rental_id, location, r_start_date, r_end_date, r_num) values(%s, %s, %s, %s, %s, %s)'
        vals = (r.aed_name, r.rental_id, r.location, r.r_start_date, r.r_end_date, r.r_num)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def selectById(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from rental where rental_id=%s'
        vals = (id,)
        cur.execute(sql, vals)
        rentals = []
        for row in cur:
            rentals.append(RentVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.disconnect()
        return rentals

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from rental'
        cur.execute(sql, )
        rentals = []
        for row in cur:
            rentals.append(RentVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.disconnect()
        return rentals

    def selectByLoc(self, location):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from rental where location=%s'
        vals = (location,)
        cur.execute(sql, )
        rentals = []
        for row in cur:
            rentals.append(RentVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.disconnect()
        return rentals

    def selectByRnum(self, r_num):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from rental where r_num=%s'
        vals = (r_num,)
        cur.execute(sql, vals)
        rentals = []
        for row in cur:
            rentals.append(RentVo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.disconnect()
        return rentals

    def delete(self, aed_name):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from rental where aed_name=%s'
        vals = (aed_name,)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()


class RentService:
    def __init__(self):
        self.dao = RentDao()

    def addHeart(self, r):
        self.dao.insert(r)

    def getAll(self):
        return self.dao.selectAll()

    def getHeartById(self, id):
        return self.dao.selectById(id)

    def getHeartByLoc(self, loc):
        return self.dao.selectByLoc(loc)

    def getHeartByRnum(self, r_num):
        return self.dao.selectByRnum(r_num)

    def delHeart(self, aed_name):
        return self.dao.delete(aed_name)

