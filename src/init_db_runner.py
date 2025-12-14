# Used to initialize the database, allowed me to run the program instead of calling in the terminal
from src.database import init_db

if __name__ == '__main__':
    init_db()
    print('Done')
