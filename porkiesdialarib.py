from app import app, db
from app.models import customer, driver, order, item, quantity

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'customer': customer, 'driver': driver, 'order': order, 'item': item, 'quantity':quantity}
