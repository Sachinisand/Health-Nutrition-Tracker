# 🚀 SETUP INSTRUCTIONS - Health Nutrition Tracker

## Quick Setup Guide (5 Minutes)

---

## ✅ Step 1: Install Python Packages

Open PowerShell in your project folder and run:

```powershell
pip install -r requirements.txt
```

**Expected output:** "Successfully installed streamlit, google-generativeai, python-dotenv, pandas"

---

## ✅ Step 2: Get Your Gemini API Key

1. Go to: https://aistudio.google.com/app/apikey
2. Click "Create API Key" (in Google AI Studio)
3. Copy your API key

---

## ✅ Step 3: Create .env File

In the project folder (`d:\github\health agent`), create a new file called `.env`

**Add this line:**
```
GEMINI_API_KEY=paste_your_key_here
```

Replace `paste_your_key_here` with your actual API key

**Example:**
```
GEMINI_API_KEY=AIzaSyDxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
```

---

## ✅ Step 4: Run the App

In PowerShell, run:

```powershell
streamlit run app.py
```

**Expected output:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## 📱 Step 5: Start Using!

1. Browser opens automatically at `http://localhost:8501`
2. You see the app with:
   - 🍎 Title at top
   - ⚙️ Sidebar with daily targets
   - 📊 Dashboard with metrics
   - 🍽️ Meal input form
   - 📋 Meal history section

3. Set your daily targets in the sidebar
4. Enter a meal: "2 eggs and toast"
5. Click Submit
6. See all 4 macros appear!

---

## 🎯 You're Done! Start Tracking!

Set targets → Log meals → Watch macros update

---

## ❓ If Something Doesn't Work

### "Command not found: streamlit"
```powershell
# Make sure you're in the right folder:
cd "d:\github\health agent"

# Install again:
pip install -r requirements.txt

# Try again:
streamlit run app.py
```

### "ModuleNotFoundError: No module named 'google'"
```powershell
# Install the package:
pip install google-generativeai

# Try again:
streamlit run app.py
```

### "Error: Can't find .env file"
```
The .env file is optional. The app works without it!
It will use the fallback parser (food database)
For AI features, create .env with your API key
```

### "App won't open in browser"
```
Manually visit: http://localhost:8501
Or check PowerShell for the Network URL
```

---

## 🆘 Need Help?

1. Check **README.md** for setup help
2. Check **USER_GUIDE.md** for usage help
3. Check **QUICKSTART.md** for common questions
4. Review **TROUBLESHOOTING** section below

---

## 🔧 Troubleshooting

### Issue: "Python command not found"
**Solution:** Add Python to PATH or use full path

### Issue: "API key not working"
**Solution:** 
- Check .env file exists
- Check API key is correct
- App will use fallback (no API needed)

### Issue: "App loads but no macro data"
**Solution:**
- Restart app: Press Ctrl+C, run again
- Try example meal: "2 boiled eggs and toast"
- Check fallback mode is working

### Issue: "CSV download not working"
**Solution:**
- Check browser download settings
- Try clearing browser cache
- Restart app

### Issue: "Progress bars not updating"
**Solution:**
- Refresh browser page (F5)
- Restart app (Ctrl+C then streamlit run app.py)

---

## 📋 Files Checklist

Before running, make sure you have:

- ✅ app.py (in folder)
- ✅ agent_logic.py (in folder)
- ✅ requirements.txt (in folder)
- ✅ .env (create this with your API key)
- ✅ Python 3.8+ installed
- ✅ Internet connection (for AI features)

---

## 🎯 Success Checklist

After running `streamlit run app.py`:

- ✅ Browser opens to http://localhost:8501
- ✅ App title shows "🍎 Health Nutrition Tracker"
- ✅ Sidebar shows daily targets
- ✅ Dashboard shows 4 metric cards
- ✅ You can enter a meal
- ✅ Success message shows all 4 macros
- ✅ Progress bars update
- ✅ Meal appears in history table

---

## 🚀 Common First Meal

Try this to test:

**Enter:** "2 boiled eggs, slice of brown bread, glass of milk"

**Expected Result:**
```
✅ Boiled Eggs, Brown Bread, and Milk

🔥 Calories: 350 kcal | 🥚 Protein: 18g | 🍞 Carbs: 28g | 🧈 Fat: 12g
```

**Dashboard updates to:**
- 🔥 350/2000 calories (17%)
- 🥚 18/150g protein (12%)
- 🍞 28/250g carbs (11%)
- 🧈 12/65g fat (18%)

If you see this, **everything is working!** 🎉

---

## 📱 Mobile Setup

1. Find your computer's IP: `ipconfig` in PowerShell
2. Look for "IPv4 Address" (e.g., 192.168.1.100)
3. On phone: visit `http://192.168.1.100:8501`
4. Works on mobile!

---

## ⏸️ To Stop the App

Press `Ctrl+C` in PowerShell

To restart: Run `streamlit run app.py` again

---

## 🔑 API Key Tips

- Keys are free to create at aistudio.google.com
- App works WITHOUT a key (uses fallback parser)
- Key makes results more accurate
- Keep your key SECRET
- Don't share .env file

---

## 📚 More Help

- **README.md** - Complete documentation
- **USER_GUIDE.md** - How to use
- **QUICKSTART.md** - Quick reference
- **VISUAL_GUIDE.md** - See interface
- **TROUBLESHOOTING** - More help

---

## ✨ You're Ready!

Now run: `streamlit run app.py`

Then start logging your meals and tracking macros!

**Enjoy your professional nutrition tracker! 🍎💪**

---

**Questions? Check README.md or USER_GUIDE.md!**
