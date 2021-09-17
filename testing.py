from sqlalchemy.sql.functions import random
from my_app import db, Publication, Book, Store
#from sqlalchemy import desc
output = Store.query.filter(Store.inventory>50).delete()
db.session.commit()
print(output)

