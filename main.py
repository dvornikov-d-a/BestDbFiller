from json_work.json_worker import JsonWorker
from db.db_worker import DbWorker


def main():
    JsonWorker().serialize_db_data()
    db_data = JsonWorker().get_db_data()
    DbWorker().insert_db_data(db_data)


if __name__ == '__main__':
    main()
