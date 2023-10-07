def create_table(cursor: object,table_name: str):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (ID INTEGER PRIMARY KEY)")