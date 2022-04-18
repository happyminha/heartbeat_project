import pymysql


class MemVo:
    def __init__(self, id=None, pwd=None, name=None, region=None, tel=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.region = region
        self.tel = tel

    def __str__(self):
        return self.id + ' / ' + self.pwd + ' / ' + self.name + ' / ' + self.region + ' / ' + self.tel


class MemDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='heartbeat_project',
                                    charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self, m):
        self.connect()
        cur = self.conn.cursor()
        sql = 'insert into member values(%s, %s, %s, %s, %s)'
        vals = (m.id, m.pwd, m.name, m.region, m.tel)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def select(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from member where id=%s'
        vals = (id,)
        cur.execute(sql, vals)
        row = cur.fetchone()
        self.disconnect()
        if row != None:
            return MemVo(row[0], row[1], row[2], row[3], row[4])

    def update(self, m):  # 수정할 사람의 id, 수정할 새pwd
        self.connect()
        cur = self.conn.cursor()
        sql = 'update member set pwd=%s, tel=%s where id=%s'
        vals = (m.pwd, m.tel, m.id)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def delete(self, id):  # id로 찾아서 삭제
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from member where id=%s'
        vals = (id,)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()


class MemService:
    def __init__(self):
        self.dao = MemDao()

    def addMember(self, m):
        self.dao.insert(m)

    def getMember(self, id):
        return self.dao.select(id)

    def editMember(self, m):
        self.dao.update(m)

    def delMember(self, id):
        self.dao.delete(id)
