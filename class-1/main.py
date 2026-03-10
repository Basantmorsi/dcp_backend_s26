import pandas as pd

df = pd.read_csv('input.csv')

df['calories'] = pd.to_numeric(df['calories'], errors='coerce')
df['protein_g'] = pd.to_numeric(df['protein_g'], errors='coerce')
df['carbs_g'] = pd.to_numeric(df['carbs_g'], errors='coerce')
df['fat_g']= pd.to_numeric(df['fat_g'], errors='coerce')


grouped_by_date = df.groupby('date')
#total_calories =grouped_by_date['calories'].sum()
nutri_facts = grouped_by_date[['calories','protein_g','carbs_g','fat_g']].sum()
print("Welcome to Your Nutri tracker: ")
for date, fact in nutri_facts.iterrows():
    print(f"On {date} you consumed {fact['calories']} calories ")
    print(f"Your food contained {fact['carbs_g']}g carbs,{fact['protein_g']}g of protein and {fact['fat_g']}g of fats.")

print('--------------------------------------------------------------')
max_calories_row = df.loc[df['calories'].idxmax()]
max_protein_row = df.loc[df['protein_g'].idxmax()]
print(f"On {nutri_facts['calories'].idxmax()} you had the most calories ({nutri_facts['calories'].max()} kcal)")
print(f"Try to avoid {max_calories_row['food']} as it contains the highest calorie intake ")
print(f"The highest protein intake was in {max_protein_row['food']} ")

#print(nutri_facts)
#print ("max : ", nutri_facts.max())


#print(total_calories)

#calories_per_date = {}
#total_calories = 0

#for date, group in grouped_by_date:
   # if group['calories'].isdigit():
       # total_calories += int(group['calories'])
        #calories_per_date[date] = total_calories

#print(calories_per_date)