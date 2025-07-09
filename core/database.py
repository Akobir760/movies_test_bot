from core.db_settings import execute_query

def create_table():
    db_table = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    file_id TEXT
);"""

    execute_query(query=db_table)



def add_movie(name, description, file_id):
    add_movie_query = "INSERT INTO movies (name, description, file_id) VALUES (%s, %s, %s);"
    execute_query(query=add_movie_query, params=(name, description, file_id))


def get_all_movies():
    get_movie_query = "SELECT id, name FROM movies;"
    movies = execute_query(query=get_movie_query, fetch='all')
    print(movies)
    return execute_query(query=get_movie_query, fetch='all')


def get_movie_by_id(movie_id):
    by_id_query = "SELECT name, description, file_id FROM movies WHERE id=%s"
    return execute_query(query=by_id_query, params=(movie_id,), fetch='one')


def update_movie_name(movie_id, new_name):
    update_movie_name_query = "UPDATE movies SET name=%s WHERE id=%s"
    execute_query(query=update_movie_name_query, params=(new_name, movie_id))


def delete_movie(movie_id):
    delete_movie_query = "DELETE FROM movies WHERE id=%s"
    execute_query(query=delete_movie_query, params=(movie_id,))



