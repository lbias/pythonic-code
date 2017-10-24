import records
# noinspection PyProtectedMember
from c45_just_write_sql_support import conn_str

print(conn_str)

db = records.Database(conn_str)
rows = db.query("SELECT * FROM Measurement WHERE value > .9 "
                "ORDER BY value DESC")

for r in rows[:5]:
    print(r)
