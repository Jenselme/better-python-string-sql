import sqlite3
import logging

logger = logging.getLogger(__name__)

DATASET = [
    ("Tencho", "2018-12-03"),
    ("Bessho", "2018-12-03"),
    ("Emoto", "2020-12-03"),
    ("Gamo", "2020-12-03"),
    ("Funakoshi", "2020-12-03"),
    ("Funakoshi", "2020-12-03"),
    ("Doigaki", "2020-12-03"),
    ("Doigaki", "2020-20-03"),
    ("Chikura", "2020-12-03"),
    ("Akabane", "2020-12-03"),
]


def main():
    """Let’s try with a docstring that will select stuff"""
    conn = sqlite3.connect(":memory:")
    where_cond = "start_day >= '2019-01-01' AND start_day < '2020-01-01'"

    # Basic examples.
    query = "SELECT last_name FROM foobar;"
    # Check rendering.
    query = 'SELECT last_name FROM foobar;'
    # Check rendering.
    query = f"SELECT last_name FROM foobar WHERE {where_cond}"
    # Check rendering.
    query = f'SELECT last_name FROM foobar WHERE {where_cond}'
    # Check rendering.
    query = """
        SELECT last_name FROM foobar
    """
    # Check rendering.
    query = '''
        SELECT last_name FROM foobar
    '''
    # Check rendering.
    query = """SELECT last_name FROM foobar"""
    # Check rendering.
    query = '''SELECT last_name FROM foobar'''
    # Check rendering.
    query = """
        SELECT last_name FROM foobar
        WHERE start_day >= '2019-01-01' AND start_day < '2020-01-01'
            AND column = 'toto'
    """
    # Check rendering.
    query = """
        SELECT last_name FROM foobar  -- comment
        WHERE start_day >= '2019-01-01' AND start_day < '2020-01-01'
            AND column = 'toto'
    """
    # Check rendering.
    my_value = "value"
    query = f"""
        -- Coucou
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries,
            tartiflette AS toto,
            {my_value}
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10
    """
    # With trailing whitespaces.
    query = "SELECT last_name FROM foobar;"     
    # Check rendering.
    # With trailing comment
    query = "SELECT last_name FROM foobar;"       # comment
    # Check rendering.

    # In function calls.
    conn.executemany("INSERT INTO foobar VALUES (?, ?);", DATASET)
    # Check rendering.
    conn.executemany('INSERT INTO foobar VALUES (?, ?);', DATASET)
    # Check rendering.
    conn.executemany("INSERT INTO foobar VALUES (?, ?)", DATASET)
    # Check rendering.
    # With trailing spaces.
    conn.executemany("INSERT INTO foobar VALUES (?, ?)", DATASET)     
    # Check rendering.
    # With trailing comment.
    conn.executemany("INSERT INTO foobar VALUES (?, ?)", DATASET)     # comment
    # Check rendering.
    my_value = 'toto'
    conn.executemany(f"INSERT INTO foobar VALUES ({my_value}, ?)", DATASET)
    # Check rendering.
    print(conn.execute("SELECT * FROM my_table"))
    # Check rendering.
    print(conn.execute("""SELECT * FROM my_table"""))
    # Check rendering.
    # With trailing spaces.
    print(conn.execute("SELECT * FROM my_table"))     
    # Check rendering.
    # With trailing comment.
    print(conn.execute("SELECT * FROM my_table"))     # comment
    # Check rendering.
    conn.executescript(
        """
        DROP TABLE IF EXISTS foobar;
        -- Comment
        CREATE TABLE foobar (
            last_name TEXT TEXT NOT NULL,
            start_day TEXT NOT NULL
        );
        """
    )
    # Check rendering.
    conn.executescript(
        """
        -- Comment
        CREATE TABLE foobar (
            last_name TEXT TEXT NOT NULL,   -- comment
            start_day TEXT NOT NULL
        )
        """
    )
    # Check rendering.

    # In dict
    queries = {"query1": "SELECT * FROM my_table"}
    # Check rendering.
    queries = {"query1": "SELECT * FROM my_table", "query2": "UPDATE my_table SET column = 'toto'"}
    # Check rendering.

    # More complex queries.
    multiple_queries = """
    SELECT `last_name`, start_day, COUNT(*) AS num_entries
    FROM schema_name.table_name
    WHERE start_day >= '2019-01-01'
    GROUP BY last_name, start_day
    ORDER BY num_entries DESC
    LIMIT 10;
    select column_name from schema_name.table_name;
    """
    # Check rendering.

    # Must not render SQL.
    logger.error("Oh no: trying to update non-existing thing: %s".format(), 23)
    logger.error("""Oh no: trying to UPDATE non-existing thing: %s""".format(), 23)
    logger.error("Update non-existing thing: %s""".format(), 23)
    logger.error(
        """
        Oh no: trying to
        update non-existing thing: %s
        """.format(),
        23,
    )
    logger.error(
        """
        Oh no: trying to
        I am try to UPDATE non-existing thing: %s
        """.format(),
        23,
    )
    logger.error(
        """
        Oh no: trying to
        I am try to    UPDATE non-existing thing: %s
        """.format(),
        23,
    )
    variable = "selectedFiles"

    # Condition building
    conditions_arg = "--where"
    print(conditions_arg)
    # Check rendering.
    conditions_arg = "--where='"
    # Check rendering.
    conditions_arg = f"--where='{my_value}'"
    # Check rendering.
    conditions_arg = ("--where='" + " AND ")
    # Check rendering.
    conds = []
    conditions_arg = ("--where='" + " AND ".join(conds) + "'") if True else ""
    # Check rendering.

    # Unsupported: nested scope: the SQL we master which will create a nested
    # comment which will only end with a \n
    # At this point, we cannot end the parsing. I don’t think it makes much
    # sense anyway, write comments in Python in this case.
    # conditions_arg = "SELECT * FROM toto --WHERE toto"
    # conditions_arg = """SELECT * FROM toto --WHERE toto
    # """


if __name__ == "__main__":
    main()
