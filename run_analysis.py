import pandas as pd
import matplotlib.pyplot as plt
import os

# File paths
files = {
    "Home Page": "data/home_page_table.csv",
    "Search Page": "data/search_page_table.csv",
    "Payment Page": "data/payment_page_table.csv",
    "Confirmation Page": "data/payment_confirmation_table.csv",
    "User Data": "data/user_table.csv"
}

# Load datasets
home_df = pd.read_csv(files['Home Page'])
search_df = pd.read_csv(files['Search Page'])
payment_df = pd.read_csv(files['Payment Page'])
confirmation_df = pd.read_csv(files['Confirmation Page'])
users_df = pd.read_csv(files['User Data'])

# Ensure user_id is present and int
for df_name, df in [('home', home_df), ('search', search_df), ('payment', payment_df), ('confirm', confirmation_df), ('users', users_df)]:
    if 'user_id' not in df.columns:
        raise KeyError(f"'user_id' not found in {df_name} dataframe columns: {df.columns}")

# Count unique users at each stage
home_users = set(home_df['user_id'].unique())
search_users = set(search_df['user_id'].unique())
payment_users = set(payment_df['user_id'].unique())
confirm_users = set(confirmation_df['user_id'].unique())

funnel_counts = {
    'Home Page': len(home_users),
    'Search Page': len(search_users),
    'Payment Page': len(payment_users),
    'Confirmation Page': len(confirm_users)
}

# Convert to DataFrame
funnel_df = pd.DataFrame.from_dict(funnel_counts, orient='index', columns=['Users'])

# Compute drop-off relative to previous stage
funnel_df['Drop-off Rate (%)'] = funnel_df['Users'].pct_change().abs() * 100

print('Sales Funnel Summary:')
print(funnel_df)

# Report missing values for each dataset
print('\nMissing values summary:')
for name, df in [('Home Page', home_df), ('Search Page', search_df), ('Payment Page', payment_df), ('Confirmation Page', confirmation_df), ('User Data', users_df)]:
    missing = df.isnull().sum().sum()
    print(f"{name}: {missing} missing values")

# Visualization
stages = funnel_df.index[::-1]
values = funnel_df['Users'][::-1]
plt.figure(figsize=(8, 5))
plt.barh(stages, values, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Number of Users')
plt.ylabel('Stages')
plt.title('Sales Funnel Drop-off Analysis')
plt.tight_layout()
output_chart = os.path.join(os.getcwd(), 'sales_funnel_chart.png')
plt.savefig(output_chart)
plt.show()
print(f"Chart saved to: {output_chart}")
