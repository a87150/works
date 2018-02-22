import random
import logging


def _log():
    logging.basicConfig(level=logging.DEBUG,
                        filename='test.log',
                        format='[%(levelname)s]: [%(asctime)s]: %(message)s',
                        datefmt='%d-%b-%Y %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s-%(asctime)s]: %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger('').addHandler(handler)
    return logging

log = _log()
t = ('a', 'b', 'c', 'd')

def examination_questions(num):
    l = []
    for eq in range(num):
        d = dict.fromkeys(t)
        d[random.choice(list(d.keys()))] = True
        l.append(d)
    return l

def answer(eq):
    num = len(eq)
    l = []
    for eq in range(num):
        l.append(random.choice(t))
    return l

def test(eq, an):
    n = 0
    num = len(eq)
    for i in range(num):
        if eq[i][an[i]]:
            n = n + 1
    return n

eq = examination_questions(20)
an = answer(eq)
number = test(eq, an)
log.info('{0} {1}'.format('大大', str(number)))
print(eq, an, number)