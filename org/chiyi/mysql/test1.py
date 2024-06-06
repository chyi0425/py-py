#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @author : chiyi
# @desc :


import mysql.connector
from mysql.connector import Error


def insert_data(cursor):
    insert_query = "insert into t_user_copy1(user_name, user_type, email, phone, phone_area, sex, wbc, nts, pe_nts, invite_user_id, invite_user_path, invite_code, invite_count, activation, status, remark, create_by, create_time, create_ip, update_by, update_time, deleted) VALUES ( NULL, 1, '', '3232204072', '+1', '0', 0.000000, 0.00, 0.00, 0,'', 'ee8uCZ', 0, 1, '1', NULL, NULL, '2024-04-10 10:24:09', '', NULL, '2024-04-10 10:29:53', 0)"
    cursor.execute(insert_query)


# url: jdbc:mysql://rm-bp13bco80x74sbta3uo.mysql.rds.aliyuncs.com:3306/pulse?serverTimezone=Asia/Shanghai&useUnicode=true&characterEncoding=utf-8&useSSL=false&autoReconnect=true&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true
 #    username: testdbadmin
 #    password: iAmpAssWord2401!@#

def main():
    try:
        connection = mysql.connector.connect(
            host='rm-bp13bco80x74sbta3uo.mysql.rds.aliyuncs.com',
            port=3306,
            database='pulse_test',
            user='testdbadmin',
            password='iAmpAssWord2401!@#'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE()")
            record = cursor.fetchone()
            print("Connected to database: ", record)

            # Prepare data
            data = [(i, f'data_{i}') for i in range(10000)]

            # Insert data in chunks to avoid memory issues
            chunk_size = 10000
            for i in range(chunk_size):
                insert_data(cursor)
                connection.commit()
                print(f'Inserted {i + chunk_size} records')

            print("All data inserted successfully")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    main()
