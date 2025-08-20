# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Data Generation ---
# Create realistic synthetic data for support efficiency analysis.
# We'll simulate response times for different support channels.
np.random.seed(42) # for reproducibility
channels = ['Email', 'Phone', 'Chat', 'Social Media']
data = []

# Generate different distributions for each channel
# Email: Slower, wider distribution
email_times = np.random.normal(loc=120, scale=40, size=200)
# Phone: Medium speed, medium distribution
phone_times = np.random.normal(loc=30, scale=15, size=300)
# Chat: Fastest, tightest distribution
chat_times = np.random.normal(loc=5, scale=2.5, size=500)
# Social Media: Fast, but with more outliers
social_media_times = np.random.normal(loc=15, scale=8, size=250)

# Combine into a list of dictionaries
for time in email_times: data.append({'Channel': 'Email', 'Response Time (Minutes)': time})
for time in phone_times: data.append({'Channel': 'Phone', 'Response Time (Minutes)': time})
for time in chat_times: data.append({'Channel': 'Chat', 'Response Time (Minutes)': time})
for time in social_media_times: data.append({'Channel': 'Social Media', 'Response Time (Minutes)': time})

# Create a pandas DataFrame
df = pd.DataFrame(data)
# Ensure no negative response times
df['Response Time (Minutes)'] = df['Response Time (Minutes)'].clip(lower=1)


# --- Visualization ---
# Apply professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8) # Use 'talk' context for presentation-ready text

# Set figure size to produce a 512x512 image (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8))

# Create the violinplot
ax = sns.violinplot(
    x='Channel',
    y='Response Time (Minutes)',
    data=df,
    palette='viridis', # Use a professional and accessible color palette
    inner='quartile', # Show quartiles inside the violins
    linewidth=1.5
)

# Add meaningful titles and axis labels
plt.title('Support Response Time Distribution by Channel', fontsize=18, weight='bold')
plt.xlabel('Support Channel', fontsize=12, weight='bold')
plt.ylabel('Response Time (Minutes)', fontsize=12, weight='bold')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0) # Keep x-axis labels horizontal

# --- Export ---
# Save the chart as a PNG with exactly 512x512 pixel dimensions
# bbox_inches='tight' ensures all elements fit within the saved image
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Successfully generated and saved 'chart.png'.")