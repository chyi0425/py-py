import pandas as pd
import mysql.connector

# 设置MySQL连接参数
db_config = {
    'host': 'your_mysql_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
}

# 连接到MySQL数据库
conn = mysql.connector.connect(**db_config)

# 执行SQL查询语句
query = "select * from saas_department where tenant_id=3 and level=2"
df = pd.read_sql(query, conn, chunksize=10000)  # 使用chunksize分批读取数据，以防止内存溢出

# 关闭数据库连接
conn.close()

# 将数据导出为CSV文件
output_csv_path = 'output_data.csv'
for i, chunk in enumerate(df):
    if i == 0:
        chunk.to_csv(output_csv_path, index=False, mode='w')
    else:
        chunk.to_csv(output_csv_path, index=False, header=False, mode='a')
    print(f"Processed {i + 1} chunks.")

print("CSV导出完成。")
