from koks import goal_number

def calculate_heuristic(number, points, bank):
    """
    Heiristiskā funkcija mezgla stāvokļa novērtēšanai.
    
    :param numurs: Pašreizējais numurs
    :param punkti: Spēlētāju punkti
    :param banka: Punkti bankā
    :return: heiristiskā vērtība (jo augstāka, jo labāk)
    """

    # Jo tuvāk pie goal number, jo labāk
    distance_to_goal = goal_number - number

    # Banka: ja skaitlis ir pāra, banka dod plusu, pretējā gadījumā nē
    bank_bonus = bank if number % 2 == 0 else -bank

    # Pāra/nepāra punkti (pāra punkti ir labāki)
    even_or_odd_bonus = 10 if points % 2 == 0 else -10

    # Galīgā heiristika (jo augstāks, jo labāk)
    return -distance_to_goal + bank_bonus + even_or_odd_bonus