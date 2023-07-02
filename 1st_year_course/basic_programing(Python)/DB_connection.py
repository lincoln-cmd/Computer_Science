'''
 required packages for DB connection:
     - pymysql
     - sqlalchemy
'''


'''
 데이터베이스(DB)란?
 특정 다수의 이용자들에게 조직 내에서 필요로 하는 정보를
체계적으로 축적하는 저장소. 이 저장소에 자주 쓰이는 표준 언어로
sql이 있다.
'''


import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///test.sqlite')
conn = engine.connect()
conn.execute('CREATE TABLE test3 (col1 text, col2 text)')
conn.execute("INSERT INTO test3 VALUES ('test1','test2')")
conn.execute('select * from test').fetchall()
conn.close()

import pandas as pd
pd.read_sql('select * from test', conn)




'''
 다른 상용 DB들과 Python의 연동법:
     e.g)
    
    import sqlalchemy
    engine = sqlalchemy.create_egine("{driver}://{username}:{password}@{ip}:{port}/{db이름}")
    conn = engine.connect()
    conn.execute('~~~~(내용)')
    conn.close()
    
    
    여기서 driver 값:
        Postgres: 'postgresql+pg8000'
        Oracle: 'oracle+cx_oracle'
        Mysql: 'mysql+pymysql'
        Mariadb: 'mysql+pymysql'
        Mssql: 'mssql+pymsslq'
        
        e.g) "postgresql+pg8000://id:password@localhost:5432/postgres"
    
'''


'''
 아마존 S3와 Python 연결법:
     e.g)
    
    import boto3
    
    client = boto3.client(
        's3',
        aws_access_key_id = 'accessKeyId',
        aws_secret_access_key = 'secretAccessKey',
        use_ssl = False
    )
    obj = client.get_object(Bucket = 'bucketName', Key = 'object_key')
    
    
'''