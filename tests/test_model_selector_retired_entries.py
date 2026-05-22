"""Regression coverage for stale/dead model rows in the WebUI selector."""

import api.config as config


def test_retired_selector_model_matcher_handles_provider_prefixes_and_alias_shapes():
    assert config._is_retired_selector_model("gpt-5.5")
    assert config._is_retired_selector_model("@openai-codex:gpt-5.5")
    assert config._is_retired_selector_model("@nous:google/gemini-3.1-pro-preview")
    assert config._is_retired_selector_model("anthropic/claude-opus-4-7")

    assert not config._is_retired_selector_model("gpt-5.3-codex")
    assert not config._is_retired_selector_model("gemini-2.5-flash")
    assert not config._is_retired_selector_model("glm-5.1")


def test_retired_selector_model_filter_preserves_live_supported_rows():
    models = [
        {"id": "gpt-5.5", "label": "GPT 5.5"},
        {"id": "gpt-5.3-codex", "label": "GPT 5.3 Codex"},
        {"id": "@gemini:gemini-3.1-pro-preview", "label": "Gemini 3.1 Pro Preview"},
        {"id": "gemini-2.5-flash", "label": "Gemini 2.5 Flash"},
    ]

    assert config._filter_retired_selector_models(models) == [
        {"id": "gpt-5.3-codex", "label": "GPT 5.3 Codex"},
        {"id": "gemini-2.5-flash", "label": "Gemini 2.5 Flash"},
    ]
