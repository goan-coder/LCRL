import random
import gym
import numpy as np
from LDBA import LDBA
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
ans2=[]
# list=[10,100,500,999,2000,5000,9999]
Q=np.zeros((5,500,6),dtype=np.float64)
ldba=LDBA()
for i_episode in range(10000):
    no_of_iterations=0
    observation = env.reset()
    curr_state=ldba.state_no()
    ldba.reset()
    t=0
    total_steps=0
    while(True):
        t+=1
        env.render()
        decoded = list(env.decode(observation))
        print("X_idx=%d Y_idx=%d Pass_loc=%d Dest_idx=%d" %(decoded[0],decoded[1],decoded[2],decoded[3]))
        action = epsilon_greedy(Q[curr_state][observation],0.15)
        new_observation, reward, done, info = env.step(action)
        success=done
        e=done
        decoded_new = list(env.decode(new_observation))
        pass_loc=decoded[2]
        c=(pass_loc==4)
        ldba.step(c,e)
        new_state=ldba.state_no()
        reward=ldba.reward()
        ldba.acc()
        if ldba.current_state in ldba.sinks:
            done=True
            success=False
        next_max=max(Q[new_state][new_observation])
        old_q=Q[curr_state][observation][action]
        Q[curr_state][observation][action]=Q[curr_state][observation][action]+learning_rate*(reward+discount_factor*next_max-Q[curr_state][observation][action])
        print("reward=%d,next_max=%f,old q_value=%f, q value updated to %f,automata_state=%s" %(reward,next_max,old_q,Q[curr_state][observation][action],ldba.current_state))
        observation=new_observation
        curr_state=new_state
        if done:
            if success:
                print("Episode finished successfully after {} timesteps".format(t))
            else:
                print("Episode failed after {} timesteps".format(t))
            total_steps+=t
            ans.append(t)
            ans2.append(success)
            break
env.close()
print(ans)
print(ans2)
plt.plot(ans)
plt.xlabel('Episode Number')
plt.ylabel('Number of steps taken to reach goal')
plt.show()
# print(list)