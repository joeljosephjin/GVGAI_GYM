import gym
import gym_gvgai
from stable_baselines3 import PPO as ALGO # DQN, PPO, A2C
from stable_baselines3.common.monitor import Monitor
import wandb

log_dir = './logs/'

game, level = 'gvgai-bravekeeper', 'lvl0-v0'

env = gym_gvgai.make(game + '-' + level)
env = Monitor(env, log_dir)

## DQN
# policy='MlpPolicy', env=env, learning_rate=0.0001, buffer_size=1000000, learning_starts=50000, batch_size=32, tau=1.0, gamma=0.99, train_freq=4, gradient_steps=1,
#                         n_episodes_rollout=- 1, optimize_memory_usage=False, target_update_interval=10000, exploration_fraction=0.1, 
#                         exploration_initial_eps=1.0, exploration_final_eps=0.05, max_grad_norm=10, tensorboard_log=log_dir,
#                         create_eval_env=False, policy_kwargs=None, verbose=1, seed=None, device='auto'

## PPO
# policy, env, learning_rate=0.0003, n_steps=2048, batch_size=64, n_epochs=10, gamma=0.99, gae_lambda=0.95, 
# clip_range=0.2, clip_range_vf=None, ent_coef=0.0, vf_coef=0.5, max_grad_norm=0.5, use_sde=False, sde_sample_freq=- 1, 
# target_kl=None, tensorboard_log=log_dir, create_eval_env=False, policy_kwargs=None, verbose=1, seed=None, device='auto', _init_setup_model=True

# for seed in range(3):
#     for i in range(2, 9):
hyper_params = dict(policy='MlpPolicy', env=env, learning_rate=0.0003, n_steps=2048, batch_size=64, n_epochs=10, gamma=0.99, gae_lambda=0.95, 
clip_range=0.2, clip_range_vf=None, ent_coef=0.0, vf_coef=0.5, max_grad_norm=0.5, use_sde=False, sde_sample_freq=- 1, 
target_kl=None, tensorboard_log=log_dir, create_eval_env=False, policy_kwargs=None, verbose=1, seed=None, device='auto', _init_setup_model=True)

wandb.init(project="gvgai-rl", entity="joeljosephjin", sync_tensorboard=True, config=hyper_params, reinit=True)

model = ALGO(**hyper_params) # tensorboard --logdir ./logs/

model.learn(total_timesteps=int(1e3))
