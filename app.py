import streamlit as st
import pandas as pd
from agent_logic import HealthAgent

# Page config
st.set_page_config(
    page_title="Health Nutrition Tracker", 
    page_icon="🍎", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .stProgress > div > div > div > div {
        background-color: #667eea;
    }
    .nutrition-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize the agent in session state
if 'my_agent' not in st.session_state:
    st.session_state.my_agent = HealthAgent()

# Header
st.markdown("""<h1 style='text-align: center; color: white;'>🍎 Health Nutrition Tracker</h1>""", unsafe_allow_html=True)
st.markdown("""<p style='text-align: center; color: white; font-size: 16px;'>Track your daily meals and monitor macronutrient intake</p>""", unsafe_allow_html=True)

# Sidebar for Goals
with st.sidebar:
    st.markdown("<h2 style='color: #667eea;'>⚙️ Daily Nutrition Targets</h2>", unsafe_allow_html=True)
    
    st.session_state.my_agent.target_cal = st.number_input(
        "🔥 Calorie Goal (kcal)", 
        value=st.session_state.my_agent.target_cal,
        min_value=1000,
        max_value=5000,
        step=100
    )
    st.session_state.my_agent.target_protein = st.number_input(
        "🥚 Protein Goal (g)", 
        value=st.session_state.my_agent.target_protein,
        min_value=50,
        max_value=300,
        step=5
    )
    st.session_state.my_agent.target_carbs = st.number_input(
        "🍞 Carbs Goal (g)", 
        value=st.session_state.my_agent.target_carbs,
        min_value=100,
        max_value=500,
        step=10
    )
    st.session_state.my_agent.target_fat = st.number_input(
        "🧈 Fat Goal (g)", 
        value=st.session_state.my_agent.target_fat,
        min_value=30,
        max_value=200,
        step=5
    )
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Reset Log", use_container_width=True):
            st.session_state.my_agent.logs = []
            st.rerun()
    with col2:
        if st.button("📊 View Stats", use_container_width=True):
            st.session_state.show_stats = True

# Main dashboard - Stats
st.markdown("""<h2 style='color: white;'>📊 Daily Progress</h2>""", unsafe_allow_html=True)
rem = st.session_state.my_agent.get_remaining()
tot = st.session_state.my_agent.get_totals()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="background-color: #FFE5E5; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #FF6B6B;">
        <h3 style="color: #FF6B6B; margin: 0; font-size: 18px;">🔥 Calories</h3>
        <p style="font-size: 32px; font-weight: bold; color: #333; margin: 10px 0;">{tot['cal']}/{st.session_state.my_agent.target_cal}</p>
        <p style="font-size: 22px; color: #FF6B6B; font-weight: bold; margin: 0;">📉 {max(rem['cal'], 0)} left</p>
    </div>
    """, unsafe_allow_html=True)
    cal_percent = min((tot['cal'] / st.session_state.my_agent.target_cal) * 100, 100)
    st.progress(cal_percent / 100)

with col2:
    st.markdown(f"""
    <div style="background-color: #E5F5FF; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #4A90E2;">
        <h3 style="color: #4A90E2; margin: 0; font-size: 18px;">🥚 Protein</h3>
        <p style="font-size: 32px; font-weight: bold; color: #333; margin: 10px 0;">{tot['prot']}g/{st.session_state.my_agent.target_protein}g</p>
        <p style="font-size: 22px; color: #4A90E2; font-weight: bold; margin: 0;">📉 {max(rem['prot'], 0)}g left</p>
    </div>
    """, unsafe_allow_html=True)
    prot_percent = min((tot['prot'] / st.session_state.my_agent.target_protein) * 100, 100)
    st.progress(prot_percent / 100)

with col3:
    st.markdown(f"""
    <div style="background-color: #FFF5E5; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #FFA500;">
        <h3 style="color: #FFA500; margin: 0; font-size: 18px;">🍞 Carbs</h3>
        <p style="font-size: 32px; font-weight: bold; color: #333; margin: 10px 0;">{tot['carb']}g/{st.session_state.my_agent.target_carbs}g</p>
        <p style="font-size: 22px; color: #FFA500; font-weight: bold; margin: 0;">📉 {max(rem['carb'], 0)}g left</p>
    </div>
    """, unsafe_allow_html=True)
    carb_percent = min((tot['carb'] / st.session_state.my_agent.target_carbs) * 100, 100)
    st.progress(carb_percent / 100)

with col4:
    st.markdown(f"""
    <div style="background-color: #E5FFE5; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #52C41A;">
        <h3 style="color: #52C41A; margin: 0; font-size: 18px;">🧈 Fat</h3>
        <p style="font-size: 32px; font-weight: bold; color: #333; margin: 10px 0;">{tot['fat']}g/{st.session_state.my_agent.target_fat}g</p>
        <p style="font-size: 22px; color: #52C41A; font-weight: bold; margin: 0;">📉 {max(rem['fat'], 0)}g left</p>
    </div>
    """, unsafe_allow_html=True)
    fat_percent = min((tot['fat'] / st.session_state.my_agent.target_fat) * 100, 100)
    st.progress(fat_percent / 100)

# Input for Meal
st.markdown("""<h2 style='color: white;'>🍽️ Log a Meal</h2>""", unsafe_allow_html=True)
st.markdown("""<p style='color: white;'>Describe what you ate in detail (e.g., '2 boiled eggs, brown toast, and orange juice')</p>""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input(
        "What did you eat?", 
        placeholder="e.g., Grilled chicken breast with rice and broccoli",
        label_visibility="collapsed"
    )
with col2:
    submit_button = st.button("📤 Submit", use_container_width=True, type="primary")

if submit_button:
    if user_input.strip():
        try:
            with st.spinner("🤖 AI is analyzing meal nutrition..."):
                result = st.session_state.my_agent.parse_meal(user_input)
                
                # Create success message with all nutrition details
                success_msg = f"✅ **{result['name']}**\n\n"
                success_msg += f"🔥 Calories: {result['cal']} kcal | "
                success_msg += f"🥚 Protein: {result['prot']}g | "
                success_msg += f"🍞 Carbs: {result['carb']}g | "
                success_msg += f"🧈 Fat: {result['fat']}g"
                
                st.success(success_msg)
                st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {str(e)}. Please ensure your Gemini API key is set in the .env file.")
    else:
        st.warning("⚠️ Please describe what you ate.")

# Display meal history
if st.session_state.my_agent.logs:
    st.markdown("""<h2 style='color: white;'>📋 Meal History</h2>""", unsafe_allow_html=True)
    
    # Prepare dataframe with all nutrition info
    meal_data = []
    for i, meal in enumerate(st.session_state.my_agent.logs, 1):
        meal_data.append({
            "#": i,
            "Food": meal['name'],
            "Calories (kcal)": meal['cal'],
            "Protein (g)": meal['prot'],
            "Carbs (g)": meal['carb'],
            "Fat (g)": meal.get('fat', 0)
        })
    
    df = pd.DataFrame(meal_data)
    
    # Display with custom styling
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Delete and export options
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🗑️ Remove Last Entry", use_container_width=True):
            st.session_state.my_agent.logs.pop()
            st.rerun()
    with col2:
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="meal_log.csv",
            mime="text/csv",
            use_container_width=True
        )
    with col3:
        if st.button("🔄 Clear All", use_container_width=True):
            st.session_state.my_agent.logs = []
            st.rerun()
else:
    st.info("👉 No meals logged yet. Start by entering a meal description!")

# Footer
st.divider()
st.markdown("""<div style='text-align: center; color: white; padding: 20px;'>
<p><strong>Health Nutrition Tracker v1.0</strong></p>
<p style='font-size: 12px;'>Powered by Google Gemini AI | Track your nutrition effortlessly</p>
</div>""", unsafe_allow_html=True)
