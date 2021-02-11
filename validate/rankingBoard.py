#!/usr/bin/env python
import gym
import gym_gvgai

import json
import time

# 1. the random agent
import randomAgent as Agent


games = ['gvgai-bravekeeper', 'gvgai-greedymouse', 'gvgai-trappedhero']
# games = ['gvgai-treasurekeeper', 'gvgai-waterpuzzle', 'gvgai-golddigger']

# validateLevels = ['lvl1-v0', 'lvl2-v0', 'lvl3-v0']
validateLevels = ['lvl0-v0', 'lvl1-v0']

totalTimes = 20 # 20
numSteps = 2000 # 2000

# variables for recording the results
results = {}

for game in games:
    levelRecord = {}
    for level in validateLevels:
        timeRecord = {}
        for t in range(totalTimes):
            env = gym_gvgai.make(game + '-' + level)
            agent = Agent.Agent()
            print('Starting ' + env.env.game + " with Level " + str(env.env.lvl))
            stateObs = env.reset()
            actions = env.unwrapped.get_action_meanings()
            totalScore = 0
            startTime = time.time()

            for tick in range(numSteps): # 2000
                action_id = agent.act(stateObs, actions)
                stateObs, diffScore, done, debug = env.step(action_id)
                totalScore += diffScore
                # print("Action " + str(action_id) + " tick " + str(tick+1) + " reward " + str(diffScore) + " win " + debug["winner"])
                if done:
                    break

            print('Runtime:', round(time.time() - startTime,1), 'seconds', '\n')

            timeRecord[t] = [tick, totalScore, debug["winner"]]
        levelRecord[level] = timeRecord
    results[game] = levelRecord


filename = agent.name + "_result.txt"
with open(filename, 'w') as outfile:
    json.dump(results, outfile)



# VISUALIZE
print('----------------VISUALIZE--------------------')
print("{:<35} {:<20} {:<10}".format('Game-Level', 'Average Reward', 'No. of wins'), '\n')
for game, levels_info in results.items():
    for levelName, level_info in levels_info.items():
        reward = 0
        no_of_wins = 0
        for run_no, run_info in level_info.items():
            # print(run_info)
            reward += run_info[1]
            if run_info[2] == 'PLAYER_WINS': no_of_wins += 1
        print("{:<35} {:<20} {:<10}".format(game[6:]+'-'+levelName[3:-3], round(reward/len(level_info), 1), no_of_wins))
    print()
print('No of runs:', len(level_info), ', Episode Length:', run_info[0]+1)
