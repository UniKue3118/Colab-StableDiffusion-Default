from unittest.mock import patch

from dynamicprompts.generators.magicprompt import MagicPromptGenerator
from dynamicprompts.wildcardmanager import WildcardManager

from sd_dynamic_prompts.generator_builder import GeneratorBuilder


def test_magic_blocklist_regexp(tmp_path):
    gb = GeneratorBuilder(
        wildcard_manager=WildcardManager(tmp_path),
    )
    gb.set_seed(42)  # TODO: not setting a seed makes the test fail
    popular_artist = "grug retkawsky"
    gb.set_is_magic_prompt(magic_blocklist_regex=popular_artist)
    with patch("dynamicprompts.generators.magicprompt.MagicPromptGenerator.set_model"):
        gen = gb.create_generator()
        assert isinstance(gen, MagicPromptGenerator)
        assert gen._blocklist_regex.pattern == popular_artist
