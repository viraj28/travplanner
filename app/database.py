from sqlalchemy import create_engine, text
import os

db = os.environ["DB_STRING"]

engine = create_engine(db)


def load_places_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM places'))
    places = []
    for row in result.mappings().all():
      places.append(dict(row))
    return places


def load_place_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM places where id=:val'),dict(val=id))
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
  

def add_contact_data_to_db(application):
    application = dict(application)
    print(type(application), application, application["full_name"])
    with engine.connect() as conn:
        query = text("INSERT into contact_us_data (full_name, email, mail_subject, message) values (:full_name, :email, :mail_subject, :message)")
        conn.execute(query, {
            "full_name": application["full_name"],
            "email": application["email"],
            "mail_subject": application["mail_subject"],
            "message": application["message"]
        })
        conn.commit()


def add_itenary_req(application, id):
    application = dict(application)
    with engine.connect() as conn:
        query = text("INSERT into itenary_req (place_id, email) values (:place_id, :email)")
        conn.execute(query, {
            "place_id": id,
            "email": application["email"]
        })
        conn.commit()
