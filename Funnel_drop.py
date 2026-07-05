#This is a funnel data, i have to calculate the step by step drop percantage, calculate the drop percentage between each stage and
#print the results. Formulae: Drop percantage = (Current stage users/ Previous stage users) * 100



funnel_stages = [
    {"stage": "1_visited_site", "users": 10000},
    {"stage": "2_added_to_cart", "users": 4500},
    {"stage": "3_entered_shipping", "users": 2100},
    {"stage": "4_completed_purchase", "users": 850}
]

for i in range(1, len(funnel_stages)):
    prev = funnel_stages[i-1]
    curr = funnel_stages[i]
    
    # Calculation based on your formula (Retention/Conversion)
    conversion_pct = (curr["users"] / prev["users"]) * 100
    # Actual drop-off
    drop_pct = 100 - conversion_pct
    
    print(f"{prev['stage']} -> {curr['stage']}:")
    print(f"  Conversion: {conversion_pct:.1f}%")
    print(f"  Drop-off:   {drop_pct:.1f}%\n")
