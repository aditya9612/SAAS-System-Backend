from app.models.fine_report import FineReport


def get_all_fines(db):
    return db.query(FineReport).all()