This project is used for the **[Generic Video Game Competition (GVGAI)](http://www.gvgai.net/) Learning Competition** since the year 2019. For more about the competition legs, rules and rank, please visite the [AI in Games website](http://www.aingames.cn/), maintained by [Hao Tong](https://github.com/HawkTom) and [Jialin Liu](https://github.com/ljialin). 

# Disclamer

This project is forked from [GVGAI Gym](https://github.com/rubenrtorrado/GVGAI_GYM), which is an [OpenAI Gym](gym.openai.com) environment for games written in the [Video Game Description Language (VGDL)](http://www.gvgai.net/vgdl.php), including the GVGAI framework. 

Please refer to the paper [Deep Reinforcement Learning for General Video Game AI](https://arxiv.org/abs/1806.02448) for more about the GVGAI GYM framework and some initial results of Reinforcement Learning (RL) agents. This paper should be cited if code from this project or the [original GVGAI GYM project](https://github.com/rubenrtorrado/GVGAI_GYM) is used in any way:

```
@inproceedings{torrado2018deep,
  title={Deep Reinforcement Learning for General Video Game AI},
  author={Torrado, Ruben Rodriguez and Bontrager, Philip and Togelius, Julian and Liu, Jialin and Perez-Liebana, Diego},
  booktitle={Computational Intelligence and Games (CIG), 2018 IEEE Conference on},
  year={2018},
  organization={IEEE}
}
```

# GVGAI Learning Competition in 2021

Two competition legs at IEEE CoG2021:
http://aingames.cn/gvgai/cog2021/

## Performance of some baseline planning agents giving a forward model

* Some representive planning agents from the GVGAI Single-player Planning Competition are used as references in this test. Note that those agents have access to the game forward model, thus, the test was performed under planning setting instead of learning setting.
* *Theoretical maximum* refer to the maximum score that one can get if playing optimally.

| Game-level\ Planing agent | RHEA     | MCTS     | OLETS    | Random   | Theoretical maximum |
| -------------------------- | -------- | -------- | -------- | -------- | ------------------- |
| greedymouse-lv0            | 21.4(0)  | 29(0)    | 57.8(4)  | -4.7(0)  | 98                  |
| greedymouse-lv1            | 12.7(0)  | 20(0)    | 26.1(0)  | -2.23(0) | 67                  |
| bravekeeper-lv0            | 38.7(24) | 40.8(30) | 47(28)   | 8.5(0)   | 100                 |
| bravekeeper-lv1            | 36.2(12) | 51.7(26) | 50.8(24) | 5.0(0)   | 90                  |
| trappedhero-lv0            | 1.7(0)   | 2.0(1)   | 13.3(25) | 1.5(1)   | 15                  |
| trappedhero-lv1            | 0(0)     | 0.17(0)  | 10.2(17) | 0(0)     | 15                  |

Table 1: Average score (wins) of different [planning agents](https://github.com/rubenrtorrado/GVGAI_GYM/tree/master/gym_gvgai/envs/gvgai/src/tracks/singlePlayer/advanced) 
on each game level over 30 independent trials.

# Latest Updates 

# Installation

**Way 1: using Docker**

Please refer to the step-by-step [guidelines](https://github.com/SUSTechGameAI/GVGAI_GYM/blob/master/docs/Guidelines-Docker-GVGAI-RLbaselines.md) for setting up the framework and RL baselines with Docker (using GPU or CPU only).

**Way 2: git clone** 

  * Clone this repository to your local machine
  * Run ```pip install -e <package-location>``` to install the package
  * Install a Java compiler(e.g. ```sudo apt install openjdk-9-jdk-headless```)

# Requirements

* **Anaconda:**　The version published after 2019.10 is recomended 
* **Java:**　JDK 9 is recommended
* **Python:**　The version Python3 (3.6 or 3.7 are recomended) is acceptable. (**Python2 can't be used!!!**)

# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/SUSTechGameAI/GVGAI_GYM.

# Resources

[GVGAI website](http://www.gvgai.net)

[original GVGAI-Gym (master branch)](https://github.com/rubenrtorrado/GVGAI_GYM) 

[Demo video on YouTube](https://youtu.be/O84KgRt6AJI)

[AI in Games website for more about competition updates](http://www.aingames.cn/#sources)

[*Deep Reinforcement Learning for General Video Game AI*](https://arxiv.org/abs/1806.02448) published at IEEE CIG2018

# References

1. [G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba, “Openai gym,” 2016.](https://github.com/openai/gym)
2. [A. Hill, A. Raffin, M. Ernestus, A. Gleave, A. Kanervisto, R. Traore, P. Dhariwal, C. Hesse, O. Klimov, A. Nichol, M. Plappert, A. Radford, J. Schulman, S. Sidor, and Y. Wu, “Stable baselines,” https://github.com/hill-a/stable-baselines, 2018.](https://github.com/hill-a/stable-baselines)
3. [R. R. Torrado, P. Bontrager, J. Togelius, J. Liu, and D. Perez-Liebana, “Deep reinforcement learning for general video game AI,” in Computational Intelligence and Games (CIG), 2018 IEEE Conference on. IEEE, 2018.](https://github.com/rubenrtorrado/GVGAI_GYM)
4. [D Perez-Liebana, J Liu, A Khalifa, RD Gaina, J Togelius, SM Lucas, "General video game AI: A multitrack framework for evaluating agents, games, and content generation algorithms," in IEEE Transactions on Games, 11(3), 195-214.](https://arxiv.org/pdf/1802.10363)
