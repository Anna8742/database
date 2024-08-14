from taskmanager import db

class Table(db.Model):
    # Schema for the Table model
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    reservations = db.relationship("Reservation", backref="table", cascade="all, delete", lazy=True)

    def __repr__(self):
        # Representing the Table object in the form of a string
        return f"Table {self.table_number} (Capacity: {self.capacity})"


class Reservation(db.Model):
    # Schema for the Reservation model
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100), nullable=False)
    guest_email = db.Column(db.String(100), nullable=False)
    guest_phone = db.Column(db.String(15), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey("table.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # Representing the Reservation object in the form of a string
        return f"Reservation by {self.guest_name} on {self.date} at {self.time} for {self.guests} guests"
