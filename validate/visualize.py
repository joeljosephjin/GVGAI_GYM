import json


filename = 'randomAgent_result.txt'

with open(filename) as fd:
    data = json.load(fd)

print(filename, '\n')

print("{:<35} {:<20} {:<10}".format('Game-Level', 'Average Reward', 'No. of wins'), '\n')
for game, levels_info in data.items():
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