# -*- coding: utf-8 -*-
# Created by zed
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="toor",   # 数据库密码
    database="main",
)
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')


def create_table():
    student_table = '''
    CREATE TABLE IF NOT EXISTS stu
    (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(25) NOT NULL,
        age INT(11) NOT NULL,
        PRIMARY KEY (id)
    )ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
    '''

    grade_table = '''
    CREATE TABLE IF NOT EXISTS grade
    (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(25),
        PRIMARY KEY (id)
    )ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
    '''

    cursor.execute(student_table)
    cursor.execute(grade_table)
    db.commit()


def fake():
    for i in range(10):
        cmd = '''
        INSERT INTO stu (name, age) VALUE ('{}', {});
        '''.format('student' + str(i), 10 + i)
        cursor.execute(cmd)
    for i in range(2):
        cmd = '''
        INSERT INTO grade (name) VALUE ('{}');
        '''.format('班级' + str(i))
        cursor.execute(cmd)
    db.commit()


def main():
    create_table()
    fake()

    # 查询年龄大于等于16的学生
    query = '''
    SELECT * FROM stu WHERE age >= 16;
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    print('年龄大于或等16岁的学生有：')
    for item in result:
        print('学生：{}, 年龄：{}'.format(item[1], item[2]))

    # 将id1的班级改成三班
    cmd='''
    UPDATE grade SET name='三班' WHERE id=1
    '''
    cursor.execute(cmd)
    db.commit()
    print('已将其中一个班级名称改为"三班"')

    # 修改id1学生姓名为张三
    cmd='''
    UPDATE stu SET name='张三' WHERE id=1
    '''
    cursor.execute(cmd)
    db.commit()
    print('已将其中一个学生姓名改为三班')

    # 删除年龄大于16岁的学生
    cmd='''
    DELETE FROM stu WHERE age > 16;
    '''
    cursor.execute(cmd)
    db.commit()
    print('已删除年龄大于16岁的学生')

    db.close()


if __name__ == '__main__':
    main()