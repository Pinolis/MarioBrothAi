# MarioBrothAi
Mario ai project


FITNESS FUNCTION DI CHRISTPRESSO: 
[GeneticAlgorithm]
fitness_func = lambda frames, distance, game_score, did_win: \
frames:     Number of frames that Mario has been alive for
distance:   Total horizontal distance gone through the level
game_score: Actual score Mario has received in the level through power-ups, coins, etc.
did_win:    True/False if Mario beat the level
    max(distance ** 1.8 - \ 
    frames ** 1.5 +   \
    min(max(distance-50, 0), 1) * 2500 + \
    did_win * 1e6, 0.00001)
