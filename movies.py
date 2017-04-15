#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tmdb
import webbrowser


class OpenFavoriteListMovie():
   """docstring for OpenFavoriteListMovie"""

   def __init__(self):
      rt = tmdb.TMDB_Request_Token()
      vt = tmdb.TMDB_Validade_Token(rt.RequestToken)

      if vt.ValidatedToken == True:
         cs = tmdb.TMDB_CreateSession(rt.RequestToken)

         if cs.ValidatedSession == True:
            print("Sessão validada com token "+rt.RequestToken +
                  " e sessão criada com ID "+cs.SessionID)

            acid = tmdb.TMDB_GetAccountID(cs.SessionID)

            if not acid.AccountID == 0:

               tmfl = tmdb.TMDB_FavoriteMovies(
                   cs.SessionID, acid.AccountID)

               dataFavMovies = tmfl.MovieList

               movies_data = {}

               for i in dataFavMovies['results']:
                  m_identifier = i['original_title']
                  movies_data[m_identifier] = {}
                  movies_data[m_identifier]['original_title'] = m_identifier
                  movies_data[m_identifier]['poster_path'] = "https://image.tmdb.org/t/p/w150_and_h225_bestv2/"+i['poster_path']
                  movies_data[m_identifier]['overview'] = i['overview']
                  movies_data[m_identifier]['id'] = i['id']

                  trailer = tmdb.TMDB_Trailer(i['id'])

                  dataFavMovieTrailers = trailer.TrailerList

                  trailer_data = {}

                  count_trailer = 0

                  for t in dataFavMovieTrailers['results']:
                     t_identifier = "Trailer #" + str(count_trailer)
                     trailer_data[t_identifier] = {}
                     trailer_data[t_identifier]['url'] = "https://www.youtube.com/watch?v="+t['key']
                     trailer_data[t_identifier]['trailer_name'] = t['name']
                     count_trailer = count_trailer + 1

                  movies_data[m_identifier]['trailers'] = trailer_data

               self.FavoriteMovieData = movies_data
            else:
               print("Erro ao encontrar o Account ID")

         else:
            print("Sessão não validado por algum tipo de erro")
      else:
         print("Token não validado por algum tipo de erro")
