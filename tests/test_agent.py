"""Tests for the meal logic. They run without an API key or network:
Gemini is replaced by a fake client that returns a fixed answer."""

from types import SimpleNamespace

import pytest

from agent_logic import GeminiEstimator, HealthAgent, estimate_from_table


class FakeClient:
    """Mimics client.models.generate_content(...) and returns `text`, or raises `error`."""

    def __init__(self, text=None, error=None):
        self.calls = []
        self.models = SimpleNamespace(generate_content=self._generate)
        self._text, self._error = text, error

    def _generate(self, **kwargs):
        self.calls.append(kwargs)
        if self._error:
            raise self._error
        return SimpleNamespace(text=self._text)


def offline_agent():
    return HealthAgent(estimator=GeminiEstimator(client=None, api_key=None))


# ---------- built-in estimate ----------

def test_quantities_are_multiplied():
    meal = estimate_from_table("2 eggs and toast")
    assert meal["cal"] == 2 * 78 + 79
    assert "2 x egg" in meal["matched"]


def test_number_words_and_plurals():
    assert estimate_from_table("three bananas")["cal"] == 3 * 105


def test_no_partial_word_matches():
    # "pineapple" must not count as an apple, "doughnuts" not as nuts
    meal = estimate_from_table("pineapple juice and doughnuts")
    assert meal["matched"] == []
    assert meal["cal"] == 450          # default meal when nothing is recognised


def test_multi_word_food():
    meal = estimate_from_table("sweet potato with spinach")
    assert set(meal["matched"]) == {"1 x sweet potato", "1 x spinach"}


def test_estimate_is_marked():
    assert estimate_from_table("chicken")["source"] == "estimate"


# ---------- Gemini path (fake client) ----------

def test_gemini_answer_is_used_and_validated():
    client = FakeClient('{"name": "Chicken, rice and salad", "calories": 620, "protein_g": 45, "carbs_g": 60, "fat_g": 18}')
    agent = HealthAgent(estimator=GeminiEstimator(client=client, model="test-model"))
    meal = agent.parse_meal("chicken, rice and salad")
    assert meal["name"] == "Chicken, rice and salad"      # commas in names no longer break parsing
    assert (meal["cal"], meal["source"]) == (620, "gemini")
    assert client.calls[0]["model"] == "test-model"
    assert agent.last_error is None


@pytest.mark.parametrize("bad", ['{"name": "x"}', "not json", '{"name": "x", "calories": -5, "protein_g": 1, "carbs_g": 1, "fat_g": 1}'])
def test_invalid_answer_falls_back(bad):
    agent = HealthAgent(estimator=GeminiEstimator(client=FakeClient(bad)))
    meal = agent.parse_meal("2 eggs")
    assert meal["source"] == "estimate" and meal["cal"] == 156
    assert "invalid answer" in agent.last_error


def test_api_error_falls_back():
    agent = HealthAgent(estimator=GeminiEstimator(client=FakeClient(error=RuntimeError("quota"))))
    assert agent.parse_meal("apple")["source"] == "estimate"
    assert "request failed" in agent.last_error


# ---------- totals ----------

def test_totals_and_remaining():
    agent = offline_agent()
    agent.parse_meal("2 eggs")
    agent.parse_meal("banana")
    assert agent.get_totals()["cal"] == 156 + 105
    assert agent.get_remaining()["cal"] == 2000 - 261
