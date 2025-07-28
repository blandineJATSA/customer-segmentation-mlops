"""Configuration utilities for the project."""

import os
import yaml
from pathlib import Path
from typing import Dict, Any
import logging

class Config:
    """Configuration manager for the project."""
    
    def __init__(self, config_dir: str = "config"):
        """Initialize configuration manager.
        
        Args:
            config_dir: Directory containing configuration files
        """
        self.config_dir = Path(config_dir)
        self.config = {}
        self._load_all_configs()
    
    def _load_all_configs(self):
        """Load all YAML configuration files."""
        config_files = [
            "config.yaml",
            "model_config.yaml", 
            "data_config.yaml"
        ]
        
        for config_file in config_files:
            config_path = self.config_dir / config_file
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    file_config = yaml.safe_load(f)
                    self.config.update(file_config)
                    
        logging.info(f"Loaded configuration from {len(config_files)} files")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key.
        
        Args:
            key: Configuration key (supports dot notation like 'mlflow.tracking_uri')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
                
        return value
    
    def get_mlflow_config(self) -> Dict[str, Any]:
        """Get MLflow specific configuration."""
        return self.config.get('mlflow', {})
    
    def get_data_config(self) -> Dict[str, Any]:
        """Get data specific configuration.""" 
        return self.config.get('data', {})
    
    def get_model_config(self) -> Dict[str, Any]:
        """Get model specific configuration."""
        return self.config.get('model', {})

# Global configuration instance
config = Config()
