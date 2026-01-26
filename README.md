# 🍎 Health Nutrition Tracker

A professional web-based nutrition tracking application powered by Google Gemini AI that intelligently analyzes your meals and calculates complete macronutrient data (calories, protein, carbs, and fat).

## ✨ Key Features

### 📊 Comprehensive Nutrition Tracking
- **Full Macro Tracking**: Calories, Protein, Carbs, AND Fat (not just calories!)
- **Daily Targets**: Set personalized goals for each macronutrient
- **Real-time Progress**: Visual progress bars for all macros
- **Meal History**: Complete log with detailed nutrition breakdown
- **Data Export**: Download meals as CSV file

### 🤖 AI-Powered Analysis
- **Smart Parsing**: Google Gemini AI analyzes natural meal descriptions
- **Accurate Estimates**: Uses typical serving sizes for calculations
- **Fallback Mode**: Works without API (uses food database)
- **All Macros**: Extracts calories, protein, carbs, and fat accurately

### 💻 Professional Interface
- **Beautiful Design**: Modern gradient UI with responsive layout
- **4-Column Dashboard**: See all macros at a glance
- **Easy Management**: Add, remove, or clear meals easily
- **Mobile Friendly**: Works on desktop, tablet, and mobile

## 🚀 Quick Start

### 1. Get Your API Key
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
- Click "Create API Key"
- Create a `.env` file in the project folder with:
```
GEMINI_API_KEY=your_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app.py
```

### 4. Start Tracking!
- Set your daily targets in the sidebar
- Describe your meals naturally
- Watch your macros update automatically

## 📋 How To Use

### Setting Daily Targets
In the sidebar, set your goals:
- 🔥 **Calories**: Default 2000 kcal
- 🥚 **Protein**: Default 150g
- 🍞 **Carbs**: Default 250g
- 🧈 **Fat**: Default 65g

### Logging Meals
Enter natural descriptions:
- ✅ "Grilled chicken breast with brown rice and broccoli"
- ✅ "2 boiled eggs and whole wheat toast"
- ✅ "Small pizza and a coke"
- ✅ "Greek yogurt with granola and berries"

**Why it works better**: The more specific you are with portions and cooking methods, the more accurate the nutrition analysis!

### Viewing Progress
The dashboard shows:
- Total consumed for each macro
- Remaining allowance for the day
- Progress bars (0-100%)
- Detailed meal history table

### Managing Your Log
- 🗑️ **Remove Last Entry**: Delete most recent meal
- 📥 **Download CSV**: Export for records
- 🔄 **Clear All**: Reset the entire log

## 📊 Dashboard Display

### 4-Column Metrics
1. **Calories** - Total kcal consumed vs target
2. **Protein** - Total grams vs target
3. **Carbs** - Total grams vs target  
4. **Fat** - Total grams vs target

Each shows:
- Current consumption
- Remaining allowance
- Visual progress bar

### Meal History Table
| # | Food | Calories | Protein | Carbs | Fat |
|---|------|----------|---------|-------|-----|
| 1 | Chicken with rice | 450 | 35 | 42 | 8 |
| 2 | Apple | 95 | 0 | 25 | 0 |
| 3 | Eggs on toast | 234 | 16 | 15 | 12 |

## 🤖 How AI Nutrition Analysis Works

### With Gemini API (Recommended)
1. Enter meal description: "2 eggs with toast"
2. AI analyzes: food type, portion, cooking method
3. Returns: calories, protein, carbs, fat
4. Meal added to your log automatically

### Fallback Mode (No API Needed)
If API unavailable, the app:
1. Recognizes common foods in your description
2. Uses built-in nutrition database
3. Multiplies by quantity mentioned
4. Provides reasonable estimates

**Supported foods**: eggs, chicken, rice, bread, fruits, dairy, fish, vegetables, nuts, pasta, meat, cheese, and more!

## 🔧 Installation

### Requirements
- Python 3.8 or higher
- Streamlit
- Pandas
- Google Generative AI library

### Full Setup

1. **Clone/Download the project**
```bash
cd "d:\github\health agent"
```

2. **Create virtual environment** (optional)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

3. **Install packages**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```
GEMINI_API_KEY=your_actual_api_key
```

5. **Run application**
```bash
streamlit run app.py
```

Open browser to `http://localhost:8501`

## 📋 File Structure

```
health agent/
├── app.py                 # Main Streamlit interface
├── agent_logic.py        # AI and nutrition logic
├── requirements.txt      # Python dependencies
├── .env                  # Your API key (create this)
└── README.md             # Documentation
```

## 🛠️ Technical Details

### Main Functions

**`HealthAgent.parse_meal(meal_text)`**
- Input: Natural meal description
- Output: Dict with name, cal, prot, carb, fat
- Uses: Gemini AI or fallback parser

**`HealthAgent.get_totals()`**
- Returns: Total macros consumed today

**`HealthAgent.get_remaining()`**
- Returns: Remaining allowance for each macro

## 🚨 Troubleshooting

### "Error: Make sure your API key is set"
**Solution:**
1. Create `.env` file in project root
2. Add: `GEMINI_API_KEY=your_key_here`
3. Get key: https://aistudio.google.com/app/apikey

### App won't start
**Check:**
- Python 3.8+: `python --version`
- Dependencies: `pip install -r requirements.txt`
- No syntax errors: `python -m py_compile app.py`

### Nutrition seems inaccurate
**Tips:**
- Be specific: "2 grilled chicken breasts" not "chicken"
- Include sides: "chicken, rice, and broccoli"
- Mention portions: "1 slice pizza" vs "pizza"
- Be detailed: "fried eggs" vs "scrambled eggs"

## 💾 Data Management

### Storage
- Meals stored in browser session (temporary)
- Persists while browsing, clears on close
- Use CSV export for permanent backup

### CSV Export
- Download anytime from meal history
- Import to Excel, Google Sheets, or other tools
- Perfect for tracking long-term trends

## 🔐 Privacy

- ✅ Your data stays local (in browser)
- ✅ Meal text sent to Gemini for analysis only
- ✅ No permanent server storage
- ✅ Clear anytime with "Clear All" button

## 📈 Tips for Success

1. **Be Consistent**: Log meals as you eat them
2. **Be Specific**: Details = Accuracy
3. **Check Progress**: Review daily targets regularly
4. **Export Data**: Keep monthly backups via CSV
5. **Adjust Goals**: Set realistic targets for your lifestyle

## 🏆 What Makes This Better

- ✅ **All Macros**: Not just calories - protein, carbs, fat too!
- ✅ **AI-Powered**: Gemini understands natural language
- ✅ **Always Works**: Fallback parser if API unavailable
- ✅ **Professional UI**: Beautiful, modern design
- ✅ **Easy Export**: Download your data anytime
- ✅ **No Signup**: Works locally in your browser

## 📝 License

Open source nutrition tracking project.

## 🤝 Support

If you have issues:
1. Check Troubleshooting section
2. Verify `.env` file has correct API key
3. Ensure dependencies installed: `pip install -r requirements.txt`
4. Try fallback mode (works without API)

---

**Start tracking your nutrition today! 🚀💪**
