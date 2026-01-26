# 🍎 Health Nutrition Tracker - User Guide

## 📱 Interface Layout

```
┌─────────────────────────────────────────────────────────────┐
│                  🍎 Health Nutrition Tracker                │
│         Track your daily meals and monitor macronutrient intake
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐  ┌────────────────────────────────────────┐
│  SIDEBAR         │  │  MAIN DASHBOARD                        │
│  ⚙️ TARGETS      │  │                                        │
│                  │  │  📊 Daily Progress                     │
│ 🔥 Calories:     │  │  ┌──────┬──────┬──────┬──────┐        │
│    2000 kcal     │  │  │ 🔥   │ 🥚   │ 🍞   │ 🧈   │        │
│                  │  │  │ 450  │ 35g  │ 42g  │ 8g   │        │
│ 🥚 Protein:      │  │  │kcal  │ g    │ g    │ g    │        │
│    150 g         │  │  └──────┴──────┴──────┴──────┘        │
│                  │  │  [Progress Bars for each]             │
│ 🍞 Carbs:        │  │                                        │
│    250 g         │  │  🍽️ Log a Meal                       │
│                  │  │  ┌──────────────────────────────┐     │
│ 🧈 Fat:          │  │  │ What did you eat? [........] │     │
│    65 g          │  │  │                              │     │
│                  │  │  │         📤 Submit            │     │
│ [🔄 Reset]       │  │  └──────────────────────────────┘     │
│ [📊 View Stats]  │  │                                        │
│                  │  │  📋 Meal History                       │
└──────────────────┘  │  ┌───────────────────────────────────┐ │
                      │  │ # │ Food │ Cal │ Prot│ Carb│ Fat │ │
                      │  │ 1 │Eggs  │234  │ 16  │ 15  │ 12  │ │
                      │  │ 2 │Apple │ 95  │  0  │ 25  │  0  │ │
                      │  │ 3 │Salad │150  │  8  │ 20  │  5  │ │
                      │  │ └───────────────────────────────────┘ │
                      │  │ [🗑️ Remove] [📥 Export] [🔄 Clear]   │
                      └────────────────────────────────────────┘
```

---

## 🎯 Step-by-Step Tutorial

### Step 1: Set Your Daily Goals (First Time)
1. Look at the **SIDEBAR** on the left
2. Set your nutrition targets:
   - 🔥 **Calories**: Your daily calorie goal (e.g., 2000)
   - 🥚 **Protein**: Daily protein goal (e.g., 150g)
   - 🍞 **Carbs**: Daily carb goal (e.g., 250g)
   - 🧈 **Fat**: Daily fat goal (e.g., 65g)

**Why these defaults?**
- 2000 calories: Average adult
- 150g protein: ~0.8g per pound bodyweight
- 250g carbs: ~1.25g per calorie
- 65g fat: ~30% of calories

---

### Step 2: Log Your First Meal
1. In the **main area**, find "🍽️ Log a Meal"
2. Click the text input box
3. Type what you ate naturally:
   ```
   2 boiled eggs and brown toast with orange juice
   ```
4. Click **📤 Submit**

---

### Step 3: See Your Success!
The app shows a success message:
```
✅ Boiled Eggs and Brown Toast with Orange Juice

🔥 Calories: 280 kcal | 🥚 Protein: 18g | 🍞 Carbs: 28g | 🧈 Fat: 12g
```

Your dashboard **automatically updates** showing:
- 🔥 Calories: 280 (remaining: 1720)
- 🥚 Protein: 18g (remaining: 132g)
- 🍞 Carbs: 28g (remaining: 222g)
- 🧈 Fat: 12g (remaining: 53g)

---

### Step 4: Continue Logging Throughout Day
```
Breakfast:  2 eggs + toast       → 280 cal, 18g prot, 28g carb, 12g fat
Lunch:      Chicken + rice       → 450 cal, 35g prot, 42g carb, 8g fat
Snack:      Apple + yogurt       → 195 cal, 10g prot, 52g carb, 0g fat
Dinner:     Salmon + asparagus   → 380 cal, 35g prot, 8g carb, 20g fat
                                    ────────────────────────────────
Total:                               1305 cal, 98g prot, 130g carb, 40g fat
Remaining:                           695 cal, 52g prot, 120g carb, 25g fat
```

---

### Step 5: Use the Meal History
Your **📋 Meal History** table shows everything:

| # | Food | Calories | Protein | Carbs | Fat |
|---|------|----------|---------|-------|-----|
| 1 | Eggs and Toast | 280 | 18g | 28g | 12g |
| 2 | Chicken with Rice | 450 | 35g | 42g | 8g |
| 3 | Apple & Yogurt | 195 | 10g | 52g | 0g |
| 4 | Salmon & Asparagus | 380 | 35g | 8g | 20g |

---

## 🎨 Understanding the Dashboard

### Metric Cards (4 Columns)

#### 1️⃣ 🔥 Calories
```
┌─────────────────┐
│  🔥 Calories    │
│      1305       │
│ Remaining: 695  │
│  ████░░░░░ 65% │
└─────────────────┘
```
- Shows total calories consumed (1305)
- Shows remaining for the day (695)
- Progress bar fills as you eat more

#### 2️⃣ 🥚 Protein
```
┌─────────────────┐
│  🥚 Protein     │
│      98g        │
│ Target: 150g    │
│  ████░░░░░ 65% │
└─────────────────┘
```
- Total protein consumed (98g)
- Daily target (150g)
- Progress toward goal

#### 3️⃣ 🍞 Carbs
```
┌─────────────────┐
│  🍞 Carbs       │
│      130g       │
│ Target: 250g    │
│  ██░░░░░░░ 52% │
└─────────────────┘
```
- Total carbs consumed (130g)
- Daily target (250g)
- Visual progress

#### 4️⃣ 🧈 Fat
```
┌─────────────────┐
│  🧈 Fat         │
│      40g        │
│ Target: 65g     │
│  ███░░░░░░ 62% │
└─────────────────┘
```
- Total fat consumed (40g)
- Daily target (65g)
- Progress indication

---

## ⌨️ How to Enter Meals Correctly

### ✅ GOOD Examples
```
✅ 2 boiled eggs with brown toast and orange juice
✅ Grilled chicken breast with brown rice and steamed broccoli
✅ 1 slice of pizza with small caesar salad
✅ Greek yogurt with granola and fresh berries
✅ Salmon fillet with asparagus and sweet potato
✅ Turkey sandwich on whole wheat with lettuce and tomato
✅ Pasta with marinara sauce and ground beef
```

### ❌ NOT IDEAL
```
❌ Breakfast (too vague)
❌ Lunch (no details)
❌ Food (not specific)
❌ Some stuff I made (unclear)
```

### 💡 Why Detail Matters
The AI understands:
- **Portion sizes**: "2 eggs" vs "eggs"
- **Cooking methods**: "fried" vs "boiled" vs "grilled"
- **Toppings**: "with butter" vs "plain"
- **Side dishes**: "with rice and broccoli"

More detail = More accurate nutrition! 🎯

---

## 📥 Using the Meal History

### Three Action Buttons

#### 1️⃣ 🗑️ Remove Last Entry
- Deletes the most recent meal from your log
- Use if you made a mistake
- Totals update instantly

#### 2️⃣ 📥 Download CSV
- Exports your entire meal history
- Perfect for keeping records
- Use for analysis or backup
- Opens in Excel, Google Sheets, etc.

**CSV Contents:**
```
#,Food,Calories (kcal),Protein (g),Carbs (g),Fat (g)
1,Eggs and Toast,280,18,28,12
2,Chicken with Rice,450,35,42,8
3,Apple & Yogurt,195,10,52,0
```

#### 3️⃣ 🔄 Clear All
- Deletes entire meal history
- Resets all totals to zero
- Use daily for new tracking

---

## 🔄 Reset Your Log

### Two Ways to Reset

**Option 1: Clear All Button**
- In meal history section
- Deletes all meals
- Dashboard resets to 0/0

**Option 2: Reset Log (Sidebar)**
- Top of sidebar
- [🔄 Reset Log] button
- Same effect as Clear All

**Best Practice:** Clear daily at midnight to track each day separately

---

## 🎯 Daily Workflow

### Morning Setup
1. Sidebar: Check/adjust nutrition targets
2. Input: First meal (breakfast)
3. Success! Dashboard shows first meal

### Throughout Day
1. Log each meal as you eat
2. Watch the progress bars fill
3. Check remaining allowance
4. Decide what to eat next

### Evening Review
1. Check final totals
2. Download CSV if desired
3. Clear log for next day
4. Optional: Email yourself the export

---

## 💪 Nutrition Tips

### Daily Targets Explained

**🔥 Calories (2000 kcal)**
- This is your energy budget
- More active = higher target
- Less active = lower target

**🥚 Protein (150g)**
- Build muscle & recovery
- Rule: 0.7-1g per pound bodyweight
- Spread throughout day

**🍞 Carbs (250g)**
- Energy for workouts
- Lower if less active
- Higher if athlete

**🧈 Fat (65g)**
- Essential for hormones
- Usually ~30% of calories
- Don't go too low!

### Meeting Your Goals
```
If you have:
- Remaining calories ↑ = Eat a bit more
- Remaining calories ↓ = Eaten enough
- Remaining protein ↑ = Add protein source (chicken, yogurt, etc)
- Remaining carbs ↑ = Add carbs (rice, bread, fruit, etc)
- Remaining fat ↑ = Add fat (olive oil, nuts, avocado)
```

---

## 🔧 Sidebar Functions

### Nutrition Targets
- 🔥 Calorie Goal: Adjust your daily target
- 🥚 Protein Goal: Your protein requirement
- 🍞 Carbs Goal: Your carb target
- 🧈 Fat Goal: Your fat target

**Changes apply immediately!**

### Control Buttons

**[🔄 Reset Log]**
- Clears all meals
- Resets totals to 0
- Fresh start

**[📊 View Stats]**
- Shows daily summary
- Optional feature

---

## 🚨 Common Issues & Solutions

### "Success message only showed calories"
**Old app behavior - FIXED!** ✅
- Now shows all 4 macros
- Protein, carbs, fat included

### "Some numbers seem wrong"
- Be more specific when entering meals
- "2 eggs" = More accurate than "eggs"
- "fried" vs "boiled" = Different nutrition

### "Can't see Fat column"
- Scroll right in table if on mobile
- Fat is now tracked (was missing before!)

### "App says no meals logged yet"
- You haven't added any yet!
- Click the text input and describe a meal
- Click Submit button

---

## 📊 Sample Day

```
🌅 BREAKFAST (8:00 AM)
Input: "2 scrambled eggs, whole wheat toast with butter, glass of milk"
Result: 350 cal, 18g protein, 35g carbs, 15g fat
Dashboard: 350/2000 cal, 18/150g protein, 35/250g carbs, 15/65g fat

☀️ SNACK (11:00 AM)  
Input: "Apple with almond butter"
Result: 250 cal, 8g protein, 25g carbs, 14g fat
Running total: 600/2000 cal, 26/150g protein, 60/250g carbs, 29/65g fat

🍽️ LUNCH (1:00 PM)
Input: "Grilled chicken breast with brown rice and broccoli"
Result: 450 cal, 35g protein, 42g carbs, 8g fat
Running total: 1050/2000 cal, 61/150g protein, 102/250g carbs, 37/65g fat

🍪 SNACK (4:00 PM)
Input: "Greek yogurt with berries and granola"
Result: 200 cal, 15g protein, 28g carbs, 5g fat
Running total: 1250/2000 cal, 76/150g protein, 130/250g carbs, 42/65g fat

🌆 DINNER (7:00 PM)
Input: "Salmon fillet with asparagus and sweet potato"
Result: 380 cal, 35g protein, 28g carbs, 18g fat
Daily totals: 1630/2000 cal, 111/150g protein, 158/250g carbs, 60/65g fat

REMAINING FOR DAY:
- 370 calories left
- 39g protein remaining
- 92g carbs remaining
- 5g fat remaining
```

---

## ✅ You're Ready!

Now you have:
- ✅ Beautiful dashboard
- ✅ Full macro tracking
- ✅ AI-powered meal analysis
- ✅ Complete data export
- ✅ Professional UI
- ✅ Detailed meal history

**Start tracking now! 🚀**

---

**Have questions? Check README.md for more info!**
