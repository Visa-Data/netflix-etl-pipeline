import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv(r'data\raw\netflix_titles.csv', encoding='latin1')
df=df.drop_duplicates()
df=df.fillna('Unknown')
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
engine=create_engine('postgresql://postgres:admin@localhost:5432/netflix_db')
df.to_sql('netflix_shows',engine,if_exists='replace',index=False)
print("ETL complete!")
