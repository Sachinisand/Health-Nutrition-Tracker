import os
from dotenv import load_dotenv

load_dotenv()

 # Try to import the Gemini/Generative AI SDK. If it's unavailable, set a
 # fallback so the project can still run for local testing without the
 # external dependency or API key.
try:
    import google.generativeai as genai
except Exception:
    genai = None

# Only configure the SDK if we have an API key; otherwise prefer the fallback
_GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if genai is not None and _GEMINI_KEY:
    try:
        genai.configure(api_key=_GEMINI_KEY)
    except Exception:
        genai = None
else:
    genai = None

class HealthAgent:
    def __init__(self, target_cal=2000, target_protein=150, target_carbs=250, target_fat=65):
        self.target_cal = target_cal
        self.target_protein = target_protein
        self.target_carbs = target_carbs
        self.target_fat = target_fat
        self.logs = []

    def parse_meal(self, meal_text):
        """Extract nutrition info from meal description using AI"""
        # If the SDK isn't available, provide a fallback parser
        if genai is None:
            return self._fallback_parse(meal_text)

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"""Analyze this meal: "{meal_text}"

Return ONLY a comma-separated line with exactly 5 values (no labels, no explanation):
food_name, calories, protein_grams, carbs_grams, fat_grams

Example: Grilled Chicken with Rice, 450, 35, 42, 8

Be as accurate as possible based on typical serving sizes.
If unclear, make reasonable estimates."""
            
            response = model.generate_content(prompt)
            text = response.text.strip()
            
            # Handle potential extra whitespace or formatting
            parts = [p.strip() for p in text.split(',')]
            
            if len(parts) >= 5:
                meal_data = {
                    "name": parts[0],
                    "cal": int(float(parts[1])),
                    "prot": int(float(parts[2])),
                    "carb": int(float(parts[3])),
                    "fat": int(float(parts[4]))
                }
            else:
                # Fallback if parsing fails
                return self._fallback_parse(meal_text)
            
            self.logs.append(meal_data)
            return meal_data
        except Exception as e:
            # If API call fails, use fallback parser
            return self._fallback_parse(meal_text)
    
    def _fallback_parse(self, meal_text):
        """Fallback parser with reasonable nutritional estimates"""
        import re
        
        # Dictionary of common foods and their approximate nutrition (per typical serving)
        common_foods = {
            "egg": {"cal": 155, "prot": 13, "carb": 1, "fat": 11},
            "chicken": {"cal": 165, "prot": 31, "carb": 0, "fat": 3},
            "rice": {"cal": 206, "prot": 4, "carb": 45, "fat": 0},
            "bread": {"cal": 79, "prot": 3, "carb": 14, "fat": 1},
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
            "olive": {"cal": 115, "prot": 0, "carb": 6, "fat": 10},
            "nuts": {"cal": 185, "prot": 7, "carb": 7, "fat": 17},
            "butter": {"cal": 100, "prot": 0, "carb": 0, "fat": 11},
            "sweet potato": {"cal": 103, "prot": 2, "carb": 24, "fat": 0},
            "spinach": {"cal": 23, "prot": 3, "carb": 4, "fat": 0},
            "tomato": {"cal": 27, "prot": 1, "carb": 6, "fat": 0},
            "pizza": {"cal": 285, "prot": 12, "carb": 36, "fat": 10},
            "burger": {"cal": 354, "prot": 17, "carb": 28, "fat": 17},
            "salad": {"cal": 150, "prot": 8, "carb": 20, "fat": 5},
        }
        
        lower_text = meal_text.lower()
        total_cal, total_prot, total_carb, total_fat = 0, 0, 0, 0
        found_items = []
        
        # Count occurrences and estimate portions
        for food, nutrition in common_foods.items():
            count = lower_text.count(food)
            if count > 0:
                found_items.append(food)
                total_cal += nutrition['cal'] * count
                total_prot += nutrition['prot'] * count
                total_carb += nutrition['carb'] * count
                total_fat += nutrition['fat'] * count
        
        # If no common foods found, use default estimate
        if not found_items:
            total_cal, total_prot, total_carb, total_fat = 450, 20, 50, 15
        
        meal_data = {
            "name": meal_text.strip(),
            "cal": total_cal,
            "prot": total_prot,
            "carb": total_carb,
            "fat": total_fat
        }
        
        self.logs.append(meal_data)
        return meal_data

    def get_remaining(self):
        """Calculate remaining macros for the day"""
        total_cal = sum(m['cal'] for m in self.logs)
        total_prot = sum(m['prot'] for m in self.logs)
        total_carb = sum(m['carb'] for m in self.logs)
        total_fat = sum(m.get('fat', 0) for m in self.logs)
        
        return {
            "cal": self.target_cal - total_cal,
            "prot": self.target_protein - total_prot,
            "carb": self.target_carbs - total_carb,
            "fat": self.target_fat - total_fat
        }
    
    def get_totals(self):
        """Get total macros consumed"""
        total_cal = sum(m['cal'] for m in self.logs)
        total_prot = sum(m['prot'] for m in self.logs)
        total_carb = sum(m['carb'] for m in self.logs)
        total_fat = sum(m.get('fat', 0) for m in self.logs)
        
        return {
            "cal": total_cal,
            "prot": total_prot,
            "carb": total_carb,
            "fat": total_fat
        }
