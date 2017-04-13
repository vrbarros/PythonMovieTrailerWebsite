import tmdb
import webbrowser

rt = tmdb.TMDB_Request_Token()
vt = tmdb.TMDB_Validade_Token(rt.RequestToken)

if vt.ValidatedToken == True:
    cs = tmdb.TMDB_CreateSession(rt.RequestToken)

    if cs.ValidatedSession == True:
        print("Sessão validada com token "+rt.RequestToken +
              " e sessão criada com ID "+cs.SessionID)

        acid = tmdb.TMDB_GetAccountID(cs.SessionID)

        if not acid.AccountID == 0:

            tmfl = tmdb.TMDB_FavoriteMovies(cs.SessionID, acid.AccountID)

            dataFavMovies = tmfl.MovieList

            for i in dataFavMovies['results']:
                original_title = i['original_title']
                poster_path = i['poster_path']
                movie_id = i['id']

                trailer = tmdb.TMDB_Trailer(movie_id)

                dataFavMovieTrailers = trailer.TrailerList

                for t in dataFavMovieTrailers['results']:
                    yt_url = "https://www.youtube.com/watch?v="+t['key']

        else:
            print("Erro ao encontrar o Account ID")

    else:
        print("Sessão não validado por algum tipo de erro")
else:
    print("Token não validado por algum tipo de erro")
