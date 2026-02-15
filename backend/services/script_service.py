import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))

from generator.smart_episode_generator import SmartEpisodeGenerator
from generator.first_episode import FirstEpisodeGenerator
from generator.second_episode import SecondEpisodeGenerator
from generator.consistency_validator import ConsistencyValidator
from generator.state_tracker import StateTracker
from utils.config_manager import ConfigManager
from data.data_manager import DataManager
from loguru import logger


class ScriptGenerationService:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.data_manager = DataManager()
        self.state_tracker = StateTracker(self.data_manager)
        self.validator = ConsistencyValidator(self.state_tracker)
        
        logger.info("ScriptGenerationService initialized")

    async def generate_single_script(
        self,
        episode: int,
        creativity_level: float = 0.3,
        enable_validation: bool = True
    ) -> str:
        logger.info(f"Generating script for episode {episode}")
        
        try:
            if episode == 1:
                generator = FirstEpisodeGenerator(self.config_manager, self.data_manager)
            elif episode == 2:
                generator = SecondEpisodeGenerator(self.config_manager, self.data_manager)
            else:
                generator = SmartEpisodeGenerator(self.config_manager, self.data_manager)
            
            outline = self.data_manager.get_outline(episode)
            if not outline:
                raise ValueError(f"Outline for episode {episode} not found")
            
            script_content = generator.generate(episode, outline)
            
            if enable_validation:
                validation_result = self.validator.validate(episode, script_content)
                if not validation_result["is_valid"]:
                    logger.warning(f"Validation issues found for episode {episode}: {validation_result['issues']}")
            
            logger.info(f"Script generated successfully for episode {episode}")
            return script_content
            
        except Exception as e:
            logger.error(f"Error generating script for episode {episode}: {e}")
            raise

    async def validate_script(self, episode: int, content: str) -> dict:
        logger.info(f"Validating script for episode {episode}")
        
        try:
            validation_result = self.validator.validate(episode, content)
            logger.info(f"Validation completed for episode {episode}")
            return validation_result
        except Exception as e:
            logger.error(f"Error validating script for episode {episode}: {e}")
            raise


script_service = ScriptGenerationService()
