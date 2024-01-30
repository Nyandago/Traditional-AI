# Personalized diet plan generator

# Sample data of diet plans
diet_plans = {
    "weight_loss": ["Salad", "Grilled chicken", "Smoothie", 100],
    "muscle_gain": ["Eggs", "Protein shake", "Steak"],
    "balanced": ["Oatmeal", "Chicken salad", "Fish with vegetables"]
}

# Function to generate diet plan
def generate_diet_plan(goal):
    return diet_plans.get(goal, "No plan available for this goal")

# Main function for user interaction
def diet_planner():
    goal = input("Enter your diet goal (weight_loss, muscle_gain, balanced): ")
    plan = generate_diet_plan(goal)
    print("Your diet plan:", plan)

# Running the diet planner
diet_planner()
