import sqlite3


def read_product_from_db(input_file='bangazon.db'):
    """ Reads product information from database file.
        =============
        input = name of database file from which to read.
        output = list of tuples from sqlite db/ true. The true is returned
        to denote that this particular list of tuples will have a column for
        price that the other handler database loading functions wont have.
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()

        try:
            db.execute("SELECT * FROM Product")

        except sqlite3.OperationalError:
            return False

        finally:
            return db.fetchall(), True
