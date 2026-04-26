import gymnasium as gym

gym.register(
    id="Unitree-G1-29dof-Velocity",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotEnvCfg",
        "play_env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"unitree_rl_lab.tasks.locomotion.agents.rsl_rl_ppo_cfg:BasePPORunnerCfg",
    },
)

gym.register(
    id="Unitree-G1-29dof-Velocity-Flat",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotFlatEnvCfg",
        "play_env_cfg_entry_point": f"{__name__}.velocity_env_cfg:RobotFlatPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"unitree_rl_lab.tasks.locomotion.agents.rsl_rl_ppo_cfg:BasePPORunnerCfg",
    },
)

# ---------------------------------------------------------------------------
# Direct-workflow variants (Phase 2: bypass Reward/Obs/Termination managers).
# Same MDP semantics as the Manager versions above, just no per-term Python
# dispatch on the hot path.  See:
#   source/unitree_rl_lab/unitree_rl_lab/tasks/locomotion/direct/velocity_base_env.py
# for the env class, and ./velocity_direct_env_cfg.py for cfg specifics.
# ---------------------------------------------------------------------------

gym.register(
    id="Unitree-G1-29dof-Velocity-Flat-Direct",
    entry_point="unitree_rl_lab.tasks.locomotion.direct:UnitreeVelocityDirectEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.velocity_direct_env_cfg:G1VelocityDirectEnvCfg",
        "play_env_cfg_entry_point": f"{__name__}.velocity_direct_env_cfg:G1VelocityDirectPlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"unitree_rl_lab.tasks.locomotion.agents.rsl_rl_ppo_cfg:BasePPORunnerCfg",
    },
)
