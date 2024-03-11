# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from queue import PriorityQueue

import numpy


# funcția de inițializare
def initial_state(m, n, k):
    return [m, n, k, 0, 0]


# funcția booleană
def final_state(S) -> bool:
    k = S[2]
    return k == S[3] or k == S[4]


# Tranzitie - Umplerea unui vas
def fill_container(S, index):
    S[index] = S[index - 3]
    return S


# functie de validare

def valid_fill_contanier(S, index):
    if (S[index] == S[index - 3]):
        return False
    return True


# Tranzitie - Golirea unui vas
# functie de tranzitie
def empty_container(S, index):
    S[index] = 0
    return S


# functie de validare tranzitie
def valid_empty_contanier(S, index):
    if (S[index] == 0):
        return False
    return True


# Tranzitie dintr-un vas in celălalt vas pana un vase fie golește fie un vas se umple
# functie de tranzitie
def pour_container_into_other(S, index_source, index_destination):
    destination_space_left = S[index_destination - 3] - S[index_destination]

    if (S[index_source] < destination_space_left):
        S[index_destination] = S[index_destination] + S[index_source]
        S[index_source] = 0
    else:
        S[index_destination] = S[index_destination - 3]
        S[index_source] -= destination_space_left
    return S


# functie booleana
def valid_pour_container_into_othe(S, index_source, index_destination):
    if (S[index_source] == 0 or S[index_destination] == S[index_destination - 3]):
        return False
    return True


def pour(S, index_source, index_destination, list_tranzactioins):
    pour_container_into_other(S, index_source, index_destination)
    return BKT(S, list_tranzactioins)


def empty(S, index, list_tranzactioins):
    empty_container(S, index)
    return BKT(S, list_tranzactioins)


def fill(S, index, list_tranzaction):
    fill_container(S, index)
    return BKT(S, list_tranzaction)


def print_list(list):
    for i in list:
        print(i)


#
def BKT(S, list_tranzactions):
    if S in list_tranzactions:
        return False
    list_tranzactions.append(S)
    if final_state(S):
        print_list(list_tranzactions)
        return True
    if valid_pour_container_into_othe(S, 3, 4):
        response = pour(S.copy(), 3, 4,
                        list_tranzactions)  # copy pentru ca nu stiu daca il transmit ca param isi face singur copie
        if response is not False:
            return response
    if valid_pour_container_into_othe(S, 4, 3):
        response = pour(S.copy(), 4, 3, list_tranzactions)
        if response is not False:
            return response
    if valid_empty_contanier(S, 3):
        response = empty(S.copy(), 3, list_tranzactions)
        if response is not False:
            return response
    if valid_empty_contanier(S, 4):
        response = empty(S.copy(), 4, list_tranzactions)
        if response is not False:
            return response
    if valid_fill_contanier(S, 3):
        response = fill(S.copy(), 3, list_tranzactions)
        if response is not False:
            return response
    if valid_fill_contanier(S, 4):
        response = fill(S.copy(), 4, list_tranzactions)
        if response is not False:
            return response
    return False


# 9 - bonus
def instance_has_solution(m, n, k):
    if k % numpy.gcd(m, n) == 0 and (m + n) > k:
        return True
    return False


# 6 - implementarea hillclimbing
def heuristic(S):
    return abs(S[0] - S[3]) + abs(S[1] - S[4])


def hill_climbing(S):
    list_explored = []
    list_explored.append(S)
    if instance_has_solution(S[0], S[1], S[2]):

        neighbours = []
        response = S
        while True:

            choice = random.randrange(0, 5, 1)
            print(choice)
            if (choice == 0):
                if valid_pour_container_into_othe(S, 3, 4):
                    response = pour_container_into_other(S, 3, 4)
                    neighbours.append(response)

            elif (choice == 1):
                if valid_pour_container_into_othe(S, 4, 3):
                    response = pour_container_into_other(S, 4, 3)
                    neighbours.append(response)

            elif (choice == 2):
                if valid_empty_contanier(S, 3):
                    response = empty_container(S, 3)
                    neighbours.append(response)

            elif (choice == 3):
                if valid_empty_contanier(S, 4):
                    response = empty_container(S, 4)
                    neighbours.append(response)

            elif (choice == 4):
                if valid_fill_contanier(S, 3):
                    response = fill_container(S, 3)
                    neighbours.append(response)

            else:
                if valid_fill_contanier(S, 4):
                    response = fill_container(S, 4)
                    neighbours.append(response)

            if response not in list_explored:
                # print(next_state)
                if final_state(response):
                    return True
                if heuristic(response) < heuristic(S):
                    S = response
                    print(S)

    else:
        print("Instanta nu are solutie")
        return False


# 7 - A*

def a_star_algorithm(m, n, k):
    frontier = PriorityQueue()
    frontier.put((0, tuple(initial_state(m, n, k))))
    parents = {}
    cost = {}

    if instance_has_solution(m,n,k) :

        parents[tuple(initial_state(m, n, k))] = None
        cost[tuple(initial_state(m, n, k))] = 0

        while not frontier.empty():
            current = frontier.get()[1]


            # am gasit solutia -> reconstituim drumul
            if current[3] == k or current[4] == k:
                now = current
                path = []

                while now != (m, n, k, 0, 0):
                    path.append(now)
                    now = parents[now]

                path.append(tuple(initial_state(m, n, k)))
                path.reverse()

                print(path)
                break

            # umplere completa vas 1
            if valid_fill_contanier(current, 3):
                next = fill_container(list(current).copy(), 3)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current

            # umplere completa vas 2
            if valid_fill_contanier(current, 4):
                next = fill_container(list(current).copy(), 4)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current



            # cele doua turnari posibile
            if valid_pour_container_into_othe(current, 3, 4):
                next = pour_container_into_other(list(current).copy(), 3, 4)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current

            if valid_pour_container_into_othe(current, 4, 3):
                next = pour_container_into_other(list(current).copy(), 4, 3)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current

            # cele doua goliri
            if valid_empty_contanier(current, 4):
                next = empty_container(list(current).copy(), 4)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current

            if valid_empty_contanier(current, 3):
                next = empty_container(list(current).copy(), 3)
                new_cost = cost[current] + 1

                if tuple(next) not in cost or new_cost < cost[tuple(next)]:
                    cost[tuple(next)] = new_cost
                    priority = new_cost + heuristic(next)
                    frontier.put((priority, tuple(next)))
                    parents[tuple(next)] = current
    else:
        print("This instance doesn't have solutions")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m = int(input("Enter value for m: "))
    n = int(input("Enter value for n: "))
    k = int(input("Enter value for k: "))
    S = [m, n, k, 0, 0]

#8 meniu implementat
    print("====== Today's MENU strategies ======")
    print("Choose a strategy: ")
    print("1 - BKT ")
    print("2 - A* ")
    strategy = input("The strategy is: ")

    if strategy == '1' or strategy == "BKT":
        print(BKT(S, []))
        print()
    elif strategy == '2' or strategy == "A*":
        a_star_algorithm(m, n, k)
    # hill_climbing(S)
