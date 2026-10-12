# Health Nutrition Tracker

A Streamlit app that turns a plain-text meal description ("2 eggs and toast") into calories, protein, carbs and fat, and tracks the day against personal targets.

[![tests](https://github.com/Sachinisand/Health-Nutrition-Tracker/actions/workflows/tests.yml/badge.svg)](https://github.com/Sachinisand/Health-Nutrition-Tracker/actions/workflows/tests.yml)

## How it works

```
meal text ──► Gemini (structured JSON, validated with pydantic) ──► meal log ──► totals vs. targets
                 │ no API key / API error / invalid answer
                 └──► built-in food table (rough estimate, clearly labelled)
```

- **With a Gemini API key**, the model must answer in a fixed JSON schema (`name`, `calories`, `protein_g`, `carbs_g`, `fat_g`). The answer is validated before it is logged, so a malformed or out-of-range reply never reaches the totals.
- **Without a key**, or if the request fails, the app uses a small table of common foods. It reads quantities ("2 eggs", "three bananas") and matches whole words only ("pineapple" is not an apple). The app shows that the number is a rough estimate and which foods it recognised.
- The daily log can be corrected (remove last entry), cleared, and downloaded as CSV.

## Design decisions

| Decision | Why |
|---|---|
| Structured JSON output instead of parsing free text | Meal names contain commas ("chicken, rice and salad"), which broke a comma-split approach |
| Validation with ranges (e.g. calories 0–10,000) | An LLM can return nonsense; invalid answers fall back instead of corrupting the log |
| Visible fallback instead of a silent one | Users should know when a number is a guess |
| Model name in `.env` (`GEMINI_MODEL`) | Gemini models are retired regularly; changing the model needs no code change |
| Gemini injected into `HealthAgent` | Tests replace it with a fake client, so they run without a key or network |

## Run it

```bash
pip install -r requirements.txt
cp .env.example .env        # add your GEMINI_API_KEY (optional)
streamlit run app.py
```

A key is free from [Google AI Studio](https://aistudio.google.com/apikey). The default model is `gemini-3.5-flash`.

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

11 tests cover quantity parsing, whole-word matching, the Gemini path with a fake client, fallback on invalid answers and API errors, and the daily totals. They run automatically on every push (GitHub Actions).

## Project structure

```
├── app.py               ← Streamlit interface
├── agent_logic.py       ← Gemini estimator, built-in food table, daily log
├── tests/test_agent.py  ← pytest suite (no API key needed)
├── .env.example         ← configuration template
└── .github/workflows/   ← runs the tests on every push
```

## Limitations

- Nutrition values are estimates: neither the model nor the food table knows the exact portion or recipe.
- The log lives in the browser session; it is not saved between visits (download the CSV to keep it).
- Not medical advice.

---

**Author:** Sachini Hewahattage · [LinkedIn](https://www.linkedin.com/in/sachini-hewahattage) · [GitHub](https://github.com/Sachinisand)
