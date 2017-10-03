import random
def test(q):
    max_reward = 0.0
    list_of_draws = []
    for act in q:
        print act
        print q[act] > max_reward
        if q[act] > max_reward:
            list_of_draws = [act]
            max_reward = q[act]
        elif q[act] == max_reward:
            list_of_draws.append(act)

    #action = random.choice(list_of_draws)
    print list_of_draws






q0 = q = {
        "l": 2,
        "r": 0,
        "f": 0
    }
test(q0)