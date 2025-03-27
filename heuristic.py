from koks import goal_number
import global_variables

def calculate_heuristic(number, points, bank):
    """
    Heiristiskā funkcija mezgla stāvokļa novērtēšanai.
    
    :param numurs: Pašreizējais numurs
    :param punkti: Spēlētāju punkti
    :param banka: Punkti bankā
    :return: heiristiskā vērtība (jo augstāka, jo labāk)
    """

    # # Jo tuvāk pie goal number, jo labāk
    # distance_to_goal = goal_number - number

    # # Banka: ja skaitlis ir pāra, banka dod plusu, pretējā gadījumā nē
    # bank_bonus = bank if number % 2 == 0 else -bank

    # # Pāra/nepāra punkti (pāra punkti ir labāki)
    # even_or_odd_bonus = 10 if points % 2 == 0 else -10

    # # Galīgā heiristika (jo augstāks, jo labāk)
    # return -distance_to_goal + bank_bonus + even_or_odd_bonus

    parity_factor = 0

    if global_variables.chosenPlayer == 1:
        if (points % 2 == 0 and bank % 2 == 0) or (points % 2 != 0 and bank % 2 != 0):
            parity_factor = 1
        else:
            parity_factor = -1
    else:
        if (points % 2 == 0 and bank % 2 == 0) or (points % 2 != 0 and bank % 2 != 0):
            parity_factor = -1
        else:
            parity_factor = 1
    

    

    return parity_factor
    # parity_factor = 1 if node.points % 2 == 0  else -1
    # adjusted_score = node.points + (node.bank * parity_factor)
    
    # # 2. Attāluma līdz mērķim faktors (normalizēts 0-1)
    # distance = max(3000 - node.number, 0)
    # distance_factor = 1 - (distance / (3000 - 20))  # 20 ir minimālais sākuma skaitlis
    
    # # 3. Skaitļa īpašību analīze
    # num_str = str(node.number)
    # last_digit = int(num_str[-1])
    
    # # 3a. Pāra/nepāra ietekme uz nākamajiem punktiem
    # even_boost = 0.3 if node.number % 2 == 0 else -0.3
    
    # # 3b. Bankas trigerēšanas potenciāls
    # bank_potential = 0.5 if last_digit in {0,5} else 0
    
    # # 4. Reizinātāju stratēģiskā vērtēšana
    # multiplier_impact = 0
    # if node.depth < 5:  # Tuvākajiem gājieniem lielāka nozīme
    #     for m in [3,4,5]:
    #         next_num = node.number * m
    #         # Vērtējam katru iespējamo reizinātāju
    #         if next_num >= 3000:
    #             multiplier_impact += 2.0 if m == 5 else 1.5  # Dodam priekšroku ātrai beigšanai
    #         else:
    #             if next_num % 2 == 0:
    #                 multiplier_impact += 0.2
    #             if next_num % 10 in {0,5}:
    #                 multiplier_impact += 0.3

    # # 5. Stratēģiskā kombinācija
    # strategic_value = (
    #     4.0 * adjusted_score +          # Galvenais punktu komponents
    #     1.5 * distance_factor +         # Mērķa sasniegšanas skuba
    #     0.8 * even_boost +              # Pašreizējā stāvokļa stabilitāte
    #     1.2 * bank_potential +          # Bankas augšanas potenciāls
    #     0.6 * multiplier_impact          # Nākamo gājienu ietekme
    # )
    
    # # 6. Normalizācija un perspektīvas korekcija
    # if node.player == "computer":
    #     return strategic_value * (1 + 0.1 * node.depth)  # Dators dod priekšroku dziļākiem variantiem
    # else:
    #     return -strategic_value * (1 + 0.05 * node.depth)  # Pretinieka perspektīva