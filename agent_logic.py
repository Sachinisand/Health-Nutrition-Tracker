"""
Meal logging logic for the Health Nutrition Tracker.

parse_meal() turns a free-text meal description into calories and macros:

1. With a Gemini API key, the model is asked for structured JSON that follows
   the MealEstimate schema, so the answer is validated instead of split on commas.
2. Without a key, or if the API call fails, a small built-in food table is used.
   Those results are marked source="estimate" so the app can say they are rough.

Configuration (.env or environment):
    GEMINI_API_KEY   your key from Google AI Studio
    GEMINI_MODEL     optional, defaults to DEFAULT_MODEL
"""

import os
import re

from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError

load_dotenv()

DEFAULT_MODEL = "gemini-3.5-flash"   # stable; see ai.google.dev for newer models

PROMPT = """Estimate the nutrition of this meal: "{meal}"

Use typical serving sizes unless the description gives quantities.
Return the meal name and the totals for the whole meal."""


class MealEstimate(BaseModel):
    """Schema the model must follow (also used to validate its answer)."""
    name: str = Field(description="Short name of the meal")
    calories: int = Field(ge=0, le=10000)
    protein_g: int = Field(ge=0, le=1000)
    carbs_g: int = Field(ge=0, le=2000)
    fat_g: int = Field(ge=0, le=1000)


# Approximate values per typical serving (USDA-style averages, rounded).
COMMON_FOODS = {
    "egg": {"cal": 78, "prot": 6, "carb": 1, "fat": 5},
    "chicken": {"cal": 165, "prot": 31, "carb": 0, "fat": 4},
    "rice": {"cal": 206, "prot": 4, "carb": 45, "fat": 0},
    "bread": {"cal": 79, "prot": 3, "carb": 14, "fat": 1},
    "toast": {"cal": 79, "prot": 3, "carb": 14, "fat": 1},
    "apple": {"cal": 95, "prot": 0, "carb": 25, "fat": 0},
    "banana": {"cal": 105, "prot": 1, "carb": 27, "fat": 0},
    "milk": {"cal": 149, "prot": 8, "carb": 12, "fat": 8},
    "yogurt": {"cal": 100, "prot": 10, "carb": 7, "fat": 0},
    "salmon": {"cal": 280, "prot": 25, "carb": 0, "fat": 20},
    "broccoli": {"cal": 55, "prot": 4, "carb": 11, "fat": 0},
    "oatmeal": {"cal": 150, "prot": 5, "carb": 27, "fat": 3},
    "pasta": {"cal": 220, "prot": 8, "carb": 43, "fat": 1},
    "beef": {"cal": 250, "prot": 26, "carb": 0, "fat": 15},
    "fish": {"cal": 120, "prot": 20, "carb": 0, "fat": 4},
    "cheese": {"cal": 115, "prot": 7, "carb": 0, "fat": 9},
    "nuts": {"cal": 185, "prot": 7, "carb": 7, "fat": 17},
    "butter": {"cal": 100, "prot": 0, "carb": 0, "fat": 11},
    "sweet potato": {"cal": 103, "prot": 2, "carb": 24, "fat": 0},
    "spinach": {"cal": 23, "prot": 3, "carb": 4, "fat": 0},
    "tomato": {"cal": 27, "prot": 1, "carb": 6, "fat": 0},
    "pizza": {"cal": 285, "prot": 12, "carb": 36, "fat": 10},
    "burger": {"cal": 354, "prot": 17, "carb": 28, "fat": 17},
    "salad": {"cal": 150, "prot": 8, "carb": 20, "fat": 5},
}
DEFAULT_MEAL = {"cal": 450, "prot": 20, "carb": 50, "fat": 15}
NUMBER_WORDS = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}


def _food_pattern(food: str) -> re.Pattern:
    """Whole-word match with an optional quantity before and plural after,
    so "2 eggs" counts two eggs and "pineapple" does not count as an apple."""
    words = r"\s+".join(map(re.escape, food.split()))
    quantity = r"(?:(\d+|" + "|".join(NUMBER_WORDS) + r")\s+)?"
    return re.compile(r"\b" + quantity + words + r"(?:e?s)?\b", re.IGNORECASE)


FOOD_PATTERNS = {food: _food_pattern(food) for food in COMMON_FOODS}


def estimate_from_table(meal_text: str) -> dict:
    """Rough estimate from the built-in table (used without an API key)."""
    text = meal_text.lower()
    totals = {"cal": 0, "prot": 0, "carb": 0, "fat": 0}
    matched = []
    for food, pattern in FOOD_PATTERNS.items():
        for match in pattern.finditer(text):
            qty_text = match.group(1)
            qty = 1 if qty_text is None else int(qty_text) if qty_text.isdigit() else NUMBER_WORDS[qty_text]
            for key in totals:
                totals[key] += COMMON_FOODS[food][key] * qty
            matched.append(f"{qty} x {food}")
    if not matched:
        totals = dict(DEFAULT_MEAL)
    return {"name": meal_text.strip(), **totals, "source": "estimate", "matched": matched}


class GeminiEstimator:
    """Asks Gemini for a structured estimate. `client` can be injected for tests."""

    def __init__(self, api_key: str | None = None, model: str | None = None, client=None):
        self.model = model or os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
        self.client = client
        if self.client is None and (api_key or os.getenv("GEMINI_API_KEY")):
            from google import genai                # imported here so tests and offline use need no SDK setup
            self.client = genai.Client(api_key=api_key or os.getenv("GEMINI_API_KEY"))

    @property
    def available(self) -> bool:
        return self.client is not None

    def estimate(self, meal_text: str) -> dict:
        from google.genai import types
        response = self.client.models.generate_content(
            model=self.model,
            contents=PROMPT.format(meal=meal_text),
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=MealEstimate,
                temperature=0,
            ),
        )
        meal = MealEstimate.model_validate_json(response.text)
        return {"name": meal.name, "cal": meal.calories, "prot": meal.protein_g,
                "carb": meal.carbs_g, "fat": meal.fat_g, "source": "gemini", "matched": []}


class HealthAgent:
    def __init__(self, target_cal=2000, target_protein=150, target_carbs=250, target_fat=65, estimator=None):
        self.target_cal = target_cal
        self.target_protein = target_protein
        self.target_carbs = target_carbs
        self.target_fat = target_fat
        self.estimator = estimator if estimator is not None else GeminiEstimator()
        self.logs = []
        self.last_error = None

    def parse_meal(self, meal_text: str) -> dict:
        """Estimate a meal, add it to the log and return it.
        Falls back to the built-in table if Gemini is unavailable or its answer is invalid."""
        self.last_error = None
        meal = None
        if self.estimator.available:
            try:
                meal = self.estimator.estimate(meal_text)
            except (ValidationError, ValueError) as exc:
                self.last_error = f"Gemini returned an invalid answer ({type(exc).__name__}); used a rough estimate."
            except Exception as exc:                # network, quota, wrong model name ...
                self.last_error = f"Gemini request failed ({type(exc).__name__}); used a rough estimate."
        if meal is None:
            meal = estimate_from_table(meal_text)
        self.logs.append(meal)
        return meal

    def get_totals(self) -> dict:
        return {key: sum(m.get(key, 0) for m in self.logs) for key in ("cal", "prot", "carb", "fat")}

    def get_remaining(self) -> dict:
        totals = self.get_totals()
        return {"cal": self.target_cal - totals["cal"], "prot": self.target_protein - totals["prot"],
                "carb": self.target_carbs - totals["carb"], "fat": self.target_fat - totals["fat"]}
