
def chainageAriere(goals, K, R):
    steps = []
    cycle = 1
    g = goals
    while goals:
        cycle_goals = goals.copy()   # copie de la list goals pour chaqu cycle      # g(c)
        applicable_rule = None


        for rule in R:
            if goals[0] == rule[1]:  #parti droit de R
                applicable_rule = rule
                break

        # but appartien l base de fait
        if goals[0] in K:
            steps.append((f"\nCycle {cycle} - \nGoals: {cycle_goals} - \n'{goals[0]}' appartient a la base de fait", None))
            goals.pop(0)  #supprimer le premier but
            cycle += 1
            continue #Passe à l'itération suivante de la boucle while.

        # exist
        if applicable_rule:
            steps.append((f"\n Cycle {cycle} - \n Goals: {cycle_goals} -  \n Applicable Rule: {applicable_rule}", None))
            goals = applicable_rule[0] # but ->  les prémisses de la règle applicable
        else:
            steps.append((f"\nCycle {cycle} - \nGoals: {cycle_goals} - \nNo applicable rule found", None))
            goals.pop(0)

        cycle += 1


    steps.append((f"\nCycle {cycle} - \nGoals: [] - \n arret MI le but {g}est preuvé", None))

    return steps

