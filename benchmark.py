#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import timeit
import dis
import os
import itertools


def imper1(path):
    result = []
    for i in range(1, len(path.split('/'))):
        y = '/'.join(path.split('/')[:i]) or '/'
        result.append(y)
    return result


def imper2(path):
    i = len(path) - 1
    l = []
    while i > 0:
        while i != 0 and path[i] != '/':
            i -= 1
        l.append(path[:i] or '/')
        i -= 1
    return l


def decl1(path):
    return ['/' + '/'.join(path.split('/')[1:l]) for l in range(len(path.split('/')))[::-1] if l]


def decl2(path):
    return ['/' + '/'.join(path.split('/')[1:-l]) for l in range(-len(path.split('/'))+1, 1) if l]


def decl3(path):
    sp = path.split('/')
    return ['/' + '/'.join(sp[1:-l]) for l in range(-len(sp)+1, 1) if l]


def dunj3_1(path):
    return ['/' + item for item in itertools.accumulate(path.split('/'), os.path.join)]


def curry(f):
  def wrapper(*args):
    return f(args)
  return wrapper


def dunj3_2(path):
	return list(itertools.accumulate(path.split('/'), curry('/'.join)))


short_path = '/lel'
regular_path = '/jakie/jest/srednie/zagniezdzenie?'
long_path = '/z/lekka/dlugasna/sciezka/co/by/pierdzielnik/mial/troche/roboty'


def benchmark(function):
    print('testing ' + function)
    print('bytecode:')
    dis.dis(globals()[function])
    print('short:   ' + str(timeit.timeit(function + '(short_path)', number=1000000, globals=globals())))
    print('regular: ' + str(timeit.timeit(function + '(regular_path)', number=1000000, globals=globals())))
    print('long:    ' + str(timeit.timeit(function + '(long_path)', number=1000000, globals=globals())))

benchmark('imper1')
benchmark('imper2')
benchmark('decl1')
benchmark('decl2')
benchmark('decl3')
benchmark('dunj3_1')
benchmark('dunj3_2')
