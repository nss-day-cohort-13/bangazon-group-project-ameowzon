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

        except sqlite3.OperationalError:  # pragma: no cover
            return False

        finally:
            return db.fetchall(), True


def get_product_from_db(prod_id, input_file='bangazon.db'):
    """
    Gets single product info from db

    Args-product id
    """
    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()

        db.execute("SELECT p.Name FROM Product p WHERE p.ProductId=?", [prod_id])
        product_name = db.fetchone()
        return product_name[0]


def add_new_product(name, price):  # pragma: no cover
    """
    If logged in as admin, add new product to product table
    ============
    Method Arguments:
    name - the name of the product to be added
    price - the price of the product to be added
    """
    try:
        with sqlite3.connect('bangazon.db') as conn:
            db = conn.cursor()

            db.execute("""
INSERT INTO Product
    (Name, Price)
VALUES
    (?, ?)
                """, (name, price))

            conn.commit()
        return True

    except sqlite3.OperationalError:
        return False
