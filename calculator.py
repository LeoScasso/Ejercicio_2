# Obtener el nombre del goleador o goleadora, junto con sus goles.
def get_scorer(players):
    scorer = ["",-1]
    for player in players.items():
        if player[1][0] > scorer[1]:
            scorer = [player[0],player[1][0]]
    return scorer

#Obtener nombre del jugador mas influyente
def get_most_influential_player(players):
    max_pts = -1
    influential_name = ""
    for player in players.items():
        pts = (player[1][0] * 1.5) + (player[1][1] * 1.25) + (player[1][2])
        if pts > max_pts:
            influential_name = player[0]
            max_pts = pts
    return influential_name       

#Obtener promedio de goles por partido

average = lambda goals: goals / 25

def get_average_goals_per_game(players):
    goals=0
    for player in players.items():
        goals += player[1][0]
    return average(goals)

def get_average_scorer_goals(scorer):
    return average(scorer[1])