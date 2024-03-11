
import random
import matplotlib.pyplot as plt
import gymnasium as gym


def initialize():
    initial_state = (3, 0)
    q = {(i, j): dict.fromkeys(['up', 'down', 'left', 'right'], 0) for i in range(4) for j in range(12)}
    print(q)
    cliff = set([(3, i) for i in range(1, 11)])
    final_state = (3, 11)
    rewards = {(i, j): -100 if (i, j) in cliff else -1 for i in range(4) for j in range(12)}
    rewards[(3, 11)] = 100
    alfa = 0.5
    gama = 1
    choices = ["up", "down", "left", "right"]
    epsilon = 1
    return initial_state, final_state, q, cliff, rewards, alfa, gama, choices, epsilon


def take_action(state, action, rewards):
    next_state = (3, 0)
    if action == 'up':
        next_state = (state[0] - 1 if state[0] > 0 else state[0], state[1])
    elif action == 'down':
        next_state = (state[0] + 1 if state[0] < 3 else state[0], state[1])
    elif action == 'right':
        next_state = (state[0], state[1] + 1 if state[1] < 11 else state[1])
    elif action == 'left':
        next_state = (state[0], state[1] - 1 if state[1] > 0 else state[1])
    return next_state, rewards[next_state]


def update_q(q, current_state, next_state, action, alfa, gama, r):
    q[current_state][action] = q[current_state][action] + alfa * (r + gama * max(q[next_state].values()) - q[current_state][action])


# def animate(policy, initial_state, final_state, rewards):
#     translate_actions = {"up": 0, "right": 1, "down": 2, "left": 3}
#     env = gym.make('CliffWalking-v0', render_mode="human")
#     env.reset()
#     episode_reward = 0
#     while initial_state != final_state:
#         env.step(translate_actions[policy[initial_state]])
#         initial_state, reward = take_action(initial_state, policy[initial_state], rewards)
#         episode_reward += reward
#     print(episode_reward)
#
#
def q_learning():
    # env = gym.make('CliffWalking-v0', render_mode="human")
    # env.reset()
    translate_actions = {"up": 0, "right": 1, "down": 2, "left": 3}
    initial_state, final_state, q, cliff, rewards, alfa, gama, choices, epsilon = initialize()
    episodes_rewards = []
    for i in range(1000):
        state = initial_state
        episode_reward = 0
        while state != final_state:
            policy_action = max(q[state], key=q[state].get)
            print(policy_action)
            random_action = random.choice(choices)
            action = random_action if random.uniform(0, 1) <= epsilon else policy_action
            # if i >= 39:
            #     env.step(translate_actions[action])
            next_state, reward = take_action(state, action, rewards)
            update_q(q, state, next_state, action, alfa, gama, reward)
            state = next_state
            if state in cliff:
                state = initial_state
            episode_reward += reward
        # env.reset()
        print("ajunge aici")
        episodes_rewards.append(episode_reward)
        epsilon = max(epsilon-0.05, 0.1)
    return {state: max(q[state], key=q[state].get) for state in q}, episodes_rewards  # policy


policy, episodes_rewards = q_learning()
plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.plot([i for i in range(len(episodes_rewards))], episodes_rewards)
plt.show()
# initial_state, final_state, q, cliff, rewards, alfa, gama, choices, epsilon = initialize()
# animate(policy, initial_state, final_state, rewards)