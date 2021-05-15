#!/usr/bin/env python3

import imdb

movie = 0120616
i = imdb.IMDb()

import random
i.update(movie, info=['trivia'])
trivia = movie.get('trivia')
if trivia:
   rand_trivia = trivia[random.randrange(len(trivia))]
   print 'Random trivia: %s' % rand_trivia
