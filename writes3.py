import pandas as pd
import pyarrow
import psycopg2

df = pd.read_sql_table('table_name', '')

s3_path = 's3://{buckt_name}/{partition}/{file_name}.parquet/gzip'
df.to_parquet(s3_path, compression='gzip')