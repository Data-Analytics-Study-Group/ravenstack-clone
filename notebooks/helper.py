import psycopg
import pandas as pd


conn_string = "postgresql://neondb_owner:npg_bJClhV9r5mqi@ep-icy-dawn-apa9ijea-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

conn = psycopg.connect(conn_string)

def load_data():

    pass

def load_accounts():
    query = "SELECT * FROM accounts"
    df_accounts = pd.read_sql(query, conn)
    return df_accounts

def load_events():
    query = "SELECT * FROM events"
    df_events = pd.read_sql(query, conn)
    return df_events

def load_subscriptions():
    query = "SELECT * FROM subscriptions"
    df_subscriptions = pd.read_sql(query, conn)
    return df_subscriptions

def load_feature_usage():
    query = "SELECT * FROM feature_usage"
    df_feature_usage = pd.read_sql(query, conn)
    return df_feature_usage

def load_support_tickets():
    query = "SELECT * FROM support_tickets"
    df_support_tickets = pd.read_sql(query, conn)
    return df_support_tickets

if __name__ == "__main__":
    df_accounts = load_accounts()
    df_events = load_events()
    df_subscriptions = load_subscriptions()
    df_feature_usage = load_feature_usage()
    df_support_tickets = load_support_tickets()

    print("Accounts DataFrame:")
    print(df_accounts.head())

    print("\nEvents DataFrame:")
    print(df_events.head())

    print("\nSubscriptions DataFrame:")
    print(df_subscriptions.head())

    print("\nFeature Usage DataFrame:")
    print(df_feature_usage.head())

    print("\nSupport Tickets DataFrame:")
    print(df_support_tickets.head())