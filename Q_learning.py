import random
import gym
import numpy as np
import matplotlib.pyplot as plt
def epsilon_greedy(actions,epsilon):
    p=random.uniform(0,1)
    if p>0.15:
        return np.argmax(actions)
    return random.randrange(6)
"""
Enviroment Details:

0- R
1- G
2- Y
3- B
4- Inside Taxi

Blue- Passenger Location
Pink- Destination
"""

env = gym.make('Taxi-v3').env
learning_rate=0.1
discount_factor=0.9
ans=[]
# list=[10,100,500,999,2000,5000,9999]
Q=np.zeros((500,6),dtype=np.float64)

for i_episode in range(10000):
    no_of_iterations=0
    observation = env.reset()
    t=0
    total_steps=0
    while(True):
        t+=1
        env.render()
        decoded = list(env.decode(observation))
        print("X_idx=%d Y_idx=%d Pass_loc=%d Dest_idx=%d" %(decoded[0],decoded[1],decoded[2],decoded[3]))
        action = epsilon_greedy(Q[observation],0.15)
        new_observation, reward, done, info = env.step(action)
        next_max=max(Q[new_observation])
        old_q=Q[observation][action]
        Q[observation][action]=Q[observation][action]+learning_rate*(reward+discount_factor*next_max-Q[observation][action])
        print("reward=%d,next_max=%f,old q_value=%f, q value updated to %f" %(reward,next_max,old_q,Q[observation][action]))
        observation=new_observation
        if done:
            print("Episode finished after {} timesteps".format(t))
            total_steps+=t
            ans.append(t)
            break
env.close()
print(ans)
plt.plot(ans)
plt.xlabel('Episode Number')
plt.ylabel('Number of steps taken to reach goal')
plt.show()
# print(list)