import pandas as pd


# -------------------------
# Individual table loaders
# -------------------------

def load_accounts(conn):
    query = "SELECT * FROM accounts"
    return pd.read_sql(query, conn)


def load_events(conn):
    query = "SELECT * FROM events"
    return pd.read_sql(query, conn)


def load_subscriptions(conn):
    query = "SELECT * FROM subscriptions"
    return pd.read_sql(query, conn)


def load_feature_usage(conn):
    query = "SELECT * FROM feature_usage"
    return pd.read_sql(query, conn)


def load_support_tickets(conn):
    query = "SELECT * FROM support_tickets"
    return pd.read_sql(query, conn)

# -------------------------
# Convenience loader (optional)
# -------------------------

def load_data(conn):
    """
    Loads all tables into a dictionary for quick EDA.
    """
    return {
        "accounts": load_accounts(conn),
        "events": load_events(conn),
        "subscriptions": load_subscriptions(conn),
        "feature_usage": load_feature_usage(conn),
        "support_tickets": load_support_tickets(conn),
    }


# -------------------------------------------------------
# Manual test block commented out (for quick local debugging only)
# -------------------------------------------------------
# This block was used to test DB connection + verify
# that all loader functions return expected DataFrames.
# It is not actually being used in notebooks or production code.
# The block of code below has therefore been commented out

# if __name__ == "__main__":
#     conn = get_connection()
#
#     df_accounts = load_accounts(conn)
#     df_events = load_events(conn)
#     df_subscriptions = load_subscriptions(conn)
#     df_feature_usage = load_feature_usage(conn)
#     df_support_tickets = load_support_tickets(conn)
#
#     print("Accounts DataFrame:")
#     print(df_accounts.head())
#
#     print("\nEvents DataFrame:")
#     print(df_events.head())
#
#     print("\nSubscriptions DataFrame:")
#     print(df_subscriptions.head())
#
#     print("\nFeature Usage DataFrame:")
#     print(df_feature_usage.head())
#
#     print("\nSupport Tickets DataFrame:")
#     print(df_support_tickets.head())
