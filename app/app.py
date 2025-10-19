import yfinance as yf
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os 

load_dotenv()

commodities = ['CL=F', 'SI=F']

DB_HOST = os.getenv("DB_HOST_PROD")
DB_PORT = os.getenv("DB_PORT_PROD")
DB_NAME = os.getenv("DB_NAME_PROD")
DB_USER = os.getenv("DB_USER_PROD")
DB_PASS = os.getenv("DB_PASS_PROD")
DB_SCHEMA = os.getenv("DB_SCHEMA_PROD")


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_data (): 
    query = f"""
        SELECT
            * 
        FROM public.dm_commodities;
        """
    
    df = pd.read_sql(query, engine)

    return df 

st.set_page_config(page_title="dash", layout="wide")

st.title("dash title")

st.write("""
         dash de commodties, seja bem vindo
         """)

df = get_data()

st.dataframe(df)

