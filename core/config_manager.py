import yaml
from pathlib import Path

class ConfigManager:
    _config = None

    @classmethod
    def load_config(cls, env="dev"):
        if cls._config is None:
            base_path = Path(__file__).parent.parent / "config"

            with open(base_path / "config.yaml") as f:
                global_config = yaml.safe_load(f)

            with open(base_path / f"{env}.yaml") as f:
                env_config = yaml.safe_load(f)

            # Merge configs (env overrides global)
            cls._config = {**global_config, **env_config}

        return cls._config
