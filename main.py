# from client import get_errors
import json
import random
from functools import cmp_to_key
from math import floor, log
# SECRET_KEY = "bHRtM2tdEpzqpoPbqcA1AUanH132AcRNYNf8ure5UhV4l3506S"


def fitness(arr):
    # train_error, validation_error = get_errors(SECRET_KEY, arr)
    train_error = 1
    validation_error = 1
    # get_erros is in client.py and we don't have client.py so we commented that line and put random value in placea
    diff = abs(train_error - validation_error)
    return diff + validation_error / 2


def mutation(arr):
    for j in range(len(arr)):
        coeff = arr[j]
        if(coeff != 0):
            power = floor(log(abs(coeff), 10))
        else:
            power = -20
        mul = 1
        if(random.random() <= 0.5):
            mul = -1
        num = random.randint(1, 9)
        coeff = coeff + num * (10 ** (power - 1)) * mul
        coeff = max(coeff, -10)
        coeff = min(coeff, 10)
        arr[j] = coeff
    return arr


def crossover(par1, par2):
    offspring = []
    for i in range(0, len(par1)):
        if(random.random() <= 0.7):
            offspring.append(par1[i])
        else:
            offspring.append(par2[i])
    return mutation(offspring)


def compare(x, y):
    return x[1] - y[1]


def new_population(arr):
    new_population = []
    count = 0
    for i in range(3, 10):
        for j in range(1, i):
            if(2 * j >= i):
                break
            new_population.append(crossover(arr[j - 1][0], arr[i - j - 1][0]))
            new_population.append(crossover(arr[j - 1][0], arr[i - j - 1][0]))
            count += 2
            if(count == population_size):
                return new_population


def genetic_algorithm(population):
    arr = []
    for member in population:
        fitness_val = fitness(
            list(member))
        arr.append([member, fitness_val])
    arr = sorted(arr, key=cmp_to_key(compare))
    return new_population(arr)

# dummy data


initial_population = [[-5.4e-25, -5.19e-15, -5.68e-15, 4.81e-14, -6.41e-12, -8.01e-19, 1.74e-16, 3.61e-06, -3.27e-07, -1e-10, 5.72e-11],
                      [-5.3e-25, -4.39e-15, -4.48e-15, 5.51e-14, -5.51e-12, -
                          7.91e-19, 1.44e-16, 3.91e-06, -4.07e-07, -1e-10, 6.92e-11],
                      [-4.2e-25, -2.19e-15, -5.78e-15, 4.41e-14, -6.31e-12, -
                          7.61e-19, 1.94e-16, 4.81e-06, -4.17e-07, -1.08e-10, 5.82e-11],
                      [-4.3e-25, -3.99e-15, -5.08e-15, 4.01e-14, -4.71e-12, -
                          6.71e-19, 5.89e-17, 3.01e-06, -3.17e-07, -9.83e-11, 6.32e-11],
                      [-5.9e-25, -5.29e-15, -4.18e-15, 4.81e-14, -6.11e-12, -
                       6.41e-19, 2.94e-16, 3.21e-06, -4.07e-07, -8.13e-11, 5.72e-11],
                      [-5.1e-25, -4.09e-15, -3.78e-15, 4.61e-14, -3.91e-12, -
                       6.41e-19, 1.94e-16, 2.91e-06, -3.37e-07, -1.05e-10, 6.22e-11],
                      [-5.3e-25, -3.09e-15, -4.08e-15, 4.11e-14, -3.11e-12, -
                       6.81e-19, 6.69e-17, 2.91e-06, -2.27e-07, -5.33e-11, 6.02e-11],
                      [-4.1e-25, -2.09e-15, -6.28e-15, 5.71e-14, -5.31e-12, -6.31e-19, 6.19e-17, 2.01e-06, -3.37e-07, -5.33e-11, 5.12e-11]]
population_size = len(initial_population)

arr = genetic_algorithm(initial_population)
