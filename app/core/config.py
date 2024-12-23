import pathlib

path = pathlib.Path(__file__).parent.parent.resolve()
file_loc = str( path.joinpath('db','database.db'))

SECRET = "SECRET"


# DATABASE_URL = f"sqlite+aiosqlite:///{file_loc}"
DATABASE_URL = f"sqlite+aiosqlite:////root/project/projectX/app/db/database.db"


print(DATABASE_URL)
