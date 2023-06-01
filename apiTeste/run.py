from root.repository.filmes_repository import FilmesRepository


repo = FilmesRepository()

#repo.insert('Barbie', 'comedia', 2023)
#repo.delet('Batman')

data = repo.select()

print(data)