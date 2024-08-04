
#sans et avec le but
def chainageAvant(K, R ,G = None ):
    steps = []
    while G is None or set(G).difference(set(K)):
        regleApplicable = None
        for regl in R:
            if set(regl[0]).issubset(set(K)): #existe in BF
                K.append(regl[1])
                K = list(set(K)) #pour éliminer les doublons
                regleApplicable = f"{regl[0]} => {regl[1]}"
                steps.append({'base_de_fait': K.copy(), 'regle_Applicable': regleApplicable})
                R.remove(regl)
                break
        else:
            # If no rule applied, break the loop
            break

        if G and set(G).issubset(set(K)):
            steps.append({'base_de_fait': K.copy(), 'regle_Applicable': f"But {G} preuvé arret MI "})

    return steps



