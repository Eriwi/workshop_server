from server import db
from server.models import Data

db.reflect()
db.drop_all()
db.create_all()