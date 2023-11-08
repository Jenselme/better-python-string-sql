import sqlite3

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

    logger.error("Oh no: trying to update non-existing thing: %s".format(), 23)

    # Check rendering.

    conn = sqlite3.connect(":memory:")

    logger.error("""Oh no: trying to update non-existing thing: %s""".format(), 23)

    # Check rendering.

    conn = sqlite3.connect(":memory:")

    logger.error(
        """
                 Oh no: trying to update non-existing thing: %s
                 """.format(),
        23,
    )

    # Check rendering.

    conn = sqlite3.connect(":memory:")

    logger.error(
        """
        Oh no: trying to update non-existing thing: %s
        """.format(),
        23,
    )
    # Check rendering.
    conn = sqlite3.connect(":memory:")

    logger.error(
        """
        Oh no: trying to
        update non-existing thing: %s
        """.format(),
        23,
    )
    # Check rendering.
    conn = sqlite3.connect(":memory:")

    logger.error(
        """
        Oh no: trying to
        I am try to UPDATE non-existing thing: %s
        """.format(),
        23,
    )
    # Check rendering.
    conn = sqlite3.connect(":memory:")

    logger.error(
        """
        Oh no: trying to
        I am try to    UPDATE non-existing thing: %s
        """.format(),
        23,
    )
    # Check rendering.
    conn = sqlite3.connect(":memory:")

    toto = "selectedFiles"

    conn.executescript(
        """
        -- Comment
        SELECT *
        -- Coucou
        FROM X
        -- Cocuou
        WHERE id IS NOT NULL
        """
    )

    # Check rendering.

    conn.executescript(
        """
        DROP TABLE IF EXISTS foobar;
        -- Cocuou
        CREATE TABLE foobar (
            last_name TEXT TEXT NOT NULL,
            start_day TEXT NOT NULL
        );
        """
    )

    # Check rendering.

    conn.executescript(
        """
        DROP TABLE IF EXISTS foobar;
        -- Cocuou
        CREATE TABLE foobar (
            last_name TEXT TEXT NOT NULL,
            start_day TEXT NOT NULL
        )
        """
    )

    # Check rendering.

    t = """SELECT auneisrta FROM auniestnarsuiet"""

    # Check rendering.

    tt = """SELECT tot FROM anursiet"""

    # Check rendering.

    t = """<p>Cocuou</p>"""

    """SELECT toto from toto"""

    # Check rendering.

    x = """SELECT * from toto"""

    # Check rendering.

    conn.executemany("INSERT INTO foobar VALUES (?, ?);", DATASET)

    # Check rendering.

    conn.executemany('INSERT INTO foobar VALUES (?, ?);', DATASET)

    # Check rendering.

    conn.executemany("INSERT INTO foobar VALUES (?, ?)", DATASET)

    # Check rendering.

    conn.executemany("INSERT INTO foobar VALUES ('toto', ?)", DATASET)

    qq = """
    SELECT
        CONCAT(tab.title, " activities") as tab
    FROM toto;
    """

    # Check rendering.

    query2 = """
        SELECT
            last_name,
            -- Test
            start_day,
            COUNT(*) AS num_entries
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10;
    """

    # Check rendering.

    query2 = '''
        SELECT
            last_name,
            -- Test with update
            start_day,
            COUNT(*) AS num_entries
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10;
    '''

    # Check rendering.

    query = """
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10;
    """

    # Check rendering.

    query3 = f"""
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries,
            tartiflette AS toto,
            {toto}
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10
    """

    # Check rendering.

    query3 = f'''
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries,
            tartiflette AS toto,
            {toto}
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10
    '''

    # Check rendering.

    query3 = f"""
        -- Coucou
        SELECT last_name,
            start_day,
            COUNT(*) AS num_entries,
            tartiflette AS toto,
            {toto}
        FROM foobar
        WHERE start_day >= '2019-01-01'
        GROUP BY last_name, start_day
        ORDER BY num_entries DESC
        LIMIT 10
    """

    # Check rendering.

    another_query = f"SELECT last_name FROM foobar WHERE {toto}"
    # Check rendering.

    another_query = "SELECT last_name FROM foobar;"
    # Check rendering.
    yaq = "SELECT last_name FROM foobar;"

    # Check rendering.

    another_query = "SELECT last_name FROM foobar"
    # Check rendering.
    yaq = "SELECT last_name FROM foobar"

    # Check rendering.

    yaq2 = """
        SELECT last_name FROM foobar
    """

    # Check rendering.

    yaq3 = """
         SELECT last_name FROM foobar
         WHERE start_day >= '2019-01-01' AND start_day < '2020-01-01'
            AND tartiflette = 'toto'
    """

    # Check rendering.

    yaq3 = """
         SELECT last_name FROM foobar -- toto
         WHERE start_day >= '2019-01-01' AND start_day < '2020-01-01'
            AND tartiflette = 'toto'
    """

    # Check rendering.

    yaq3 = """
         SELECT last_name FROM foobar
         WHERE start_day >= '2019-01-01' AND start_day < '2020-01-01'
            AND tartiflette = 'toto'
    """

    # Check rendering.

    print(conn.execute(query).fetchall())

    print(conn.execute("SELECT * FROM my_table"))

    # Check rendering.

    queries = {"toto": "SELECT * FROM my_table"}

    # Check rendering.

    conditions_arg = "--where"
    print(conditions_arg)

    # Check rendering.

    conditions_arg = "--where='"

    # Check rendering.

    conditions_arg = f"--where='{toto}'"

    # Check rendering.

    conditions_arg = ("--where='" + " AND ")

    # Check rendering.
    conditions = []
    conditions_arg = ("--where='" + " AND ".join(conditions) + "'") if conditions else ""

    # Check rendering.

    # Unsupported: nested scope: the SQL we master which will create a nested
    # comment which will only end with a \n
    # At this point, we cannot end the parsing. I don’t think it makes much
    # sense anyway, write comments in Python in this case.
    # conditions_arg = "SELECT * FROM toto --WHERE toto"

    # Check rendering.

    conditions_arg = """SELECT * FROM toto
                    --WHERE toto"""

    # Check rendering.


if __name__ == "__main__":
    main()


# ANCHOR SQL
single_SQL_with_Sign = """
--sql Highlight
select `last_name`, start_day, COUNT(*) AS num_entries
FROM schema_name.table_name
WHERE start_day >= '2019-01-01'
GROUP BY last_name, start_day
ORDER BY num_entries DESC
LIMIT 10;
-- Not Highlight
select column_name from schema_name.table_name;
"""

multi_SQL_with_Sign = """
--beginsql Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
select `last_name`, start_day FROM schema_name.table_name;
--endsql
-- Not Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
"""

SQL_without_Sign = """
-- Highlight
DROP TABLE schema_name.table_name;
INSERT INTO schema_name.table_name(id, grade) VALUES(1, 100);
SELECT `last_name`, start_day
FROM (SELECT * from schema_name.table_name) tmp;
-- Not Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
select column_name from schema_name.table_name;
"""

#
# --beginsql
# DROP TABLE schema_name.table_name;
# INSERT INTO schema_name.table_name(id, grade) VALUES(1, 100);
# SELECT `last_name`, start_day
# FROM schema_name.table_name
# ;
# --endsql
#

sql = "SELECT * FROM schema_name.table_name;"

html = """<p>Coucou</p>"""

totauienst = """<p>Cocuou</p>"""

# ANCHOR HTML
HTML = """
<!--html-->
<h1>I am a highlighted html</h1>
hello
<p>world</p>
<!--!html-->
<!--htmlcomment-->
<h1>I am also a highlighted html</h1>
<!--!htmlcomment-->
<h1>I amd not a highlighted html</h1>
"""
# ANCHOR JS
js = """
//js test
var a = 1;
alert(a);
console.log(a);
function b() {
    return 123;
};
//!js

http: // js
var a = 2;
// !js

var a=1;
://js
alert(a);
//!js
console.log(a);
function b() {
    return 123;
};
"""
# ANCHOR CSS
css = """
/*css*/
body {
    display: block;
    margin: 8px;
    color: #fff;
}
/*!css*/
body {
    display: block;
    margin: 8px;
    color: #fff;
}
"""

# ANCHOR variable test
SQL_with_Variable = """
SELECT
    `name`, birth
FROM
    users
WHERE birth > '{day}'
    AND `name` != '{banned}man'
;
""".format(
    banned="bat", day="2019-09-26"
)

# ANCHOR yaml test
"""
--- #yaml
name: test
values:
  - good
  - better
  # comment
#!yaml
"""

html = """
<table>
  <tr>
    <td>100</td>
  </tr>
</table>

<hr>
<h2>1 Row and 3 Columns:</h2>
<table>
  <tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
  </tr>
</table>
"""
