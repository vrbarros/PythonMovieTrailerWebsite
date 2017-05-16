#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tmdb
import webbrowser


class OpenFavoriteListMovie():
   """This class is responsible to create the favorite movie list from the TMDB API"""

   def __init__(self):
      """It is necessary to request a validy token to connect the API"""
      rt = tmdb.TMDB_Request_Token()
      vt = tmdb.TMDB_Validade_Token(rt.RequestToken)

      if vt.ValidatedToken == True:
         cs = tmdb.TMDB_CreateSession(rt.RequestToken)

         """With the API validated, it is necessary to start a session to read some information"""
         if cs.ValidatedSession == True:
            print("Sessão validada com token "+rt.RequestToken +
                  " e sessão criada com ID "+cs.SessionID)

            acid = tmdb.TMDB_GetAccountID(cs.SessionID)

            """Check if there is any authentication made ID diff 0"""
            if not acid.AccountID == 0:

               """With the session validated, it is time to build the favorite movie list"""
               tmfl = tmdb.TMDB_FavoriteMovies(
                   cs.SessionID, acid.AccountID)

               dataFavMovies = tmfl.MovieList

               movies_data = {}

               """Build the output array to be used in our HTML page"""
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

                  """Build the sub-array Trailers to be used in our HTML page"""
                  for t in dataFavMovieTrailers['results']:
                     t_identifier = "Trailer #" + str(count_trailer)
                     trailer_data[t_identifier] = {}
                     trailer_data[t_identifier]['url'] = "https://www.youtube.com/watch?v="+t['key']
                     trailer_data[t_identifier]['trailer_name'] = t['name']
                     count_trailer = count_trailer + 1

                  movies_data[m_identifier]['trailers'] = trailer_data

               """Return the array to be used at our HTML page"""
               self.FavoriteMovieData = movies_data
            else:
               print("Erro ao encontrar o Account ID")

         else:
            print("Sessão não validado por algum tipo de erro")
      else:
         print("Token não validado por algum tipo de erro")
