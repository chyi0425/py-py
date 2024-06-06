#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @author : chiyi
# @desc :

import pymysql
import sys


def connect_to_db():
    """Connect to the MySQL database and return the connection and cursor."""
    conn = pymysql.connect(
        host='rm-bp13bco80x74sbta3uo.mysql.rds.aliyuncs.com',
        port=3306,
        db='pulse_test',
        user='testdbadmin',
        password='iAmpAssWord2401!@#'
    )
    cursor = conn.cursor()
    return conn, cursor


def fetch_all_rows(cursor, start_id, end_id, batch_size=1000):
    """Fetch rows from the database in batches within the specified ID range."""
    current_id = start_id
    while current_id <= end_id:
        cursor.execute(f"SELECT invite_user_id,receive_user_id FROM t_user WHERE id >= %s AND id <= %s ORDER BY id ASC LIMIT %s",
                       (current_id, end_id, batch_size))
        rows = cursor.fetchall()
        if not rows:
            break
        for row in rows:
            yield row
        current_id = rows[-1][0] + 1  # 假设id在查询结果的第一列


def process_data(cursor,row):
    """Process each row of data."""
    # 在这里添加你的数据处理逻辑

    print(row)



def fetch_rows_by_ids(cursor, ids):
    """Fetch rows from the database using an IN query for the specified IDs."""
    if not ids:
        return {}

    # Create a query string with placeholders for each ID
    format_strings = ','.join(['%s'] * len(ids))
    query = f"SELECT id, FROM t_user_copy1 WHERE id IN ({format_strings})"

    # Execute the query
    cursor.execute(query, ids)
    rows = cursor.fetchall()

    # Convert rows to a dictionary
    result = {row['id']: row for row in rows}
    return result


def main(start_id, end_id, batch_size):
    # 连接到数据库
    conn, cursor = connect_to_db()

    try:
        # 批量读取和处理数据
        for row in fetch_all_rows(cursor, start_id, end_id, batch_size):
            process_data(cursor, row)
    finally:
        # 关闭连接
        cursor.close()
        conn.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <start_id> <end_id> <batch_size>")
        sys.exit(1)

    start_id = int(sys.argv[1])
    end_id = int(sys.argv[2])
    batch_size = int(sys.argv[3])

    main(start_id, end_id, batch_size)
