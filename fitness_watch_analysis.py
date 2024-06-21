import pandas as pd
import plotly.express as plt
from plotly.offline import plot

data = pd.read_csv('Apple-fitness-Data.csv')
print(data.head())

print(data.isnull().sum())

figure1 = plt.line(data, x="Time", y='Step Count', title='Step Count over time')

plot(figure1)

average_step_count_per_day = data.groupby("Date")["Step Count"].mean().reset_index()

fig2 = plt.bar(average_step_count_per_day, x="Date", y="Step Count", title="Average Step Count per Day")
fig2.update_xaxes(type='category')
plot(fig2)

# Calculate Walking Efficiency
data["Walking Efficiency"] = data["Distance"] / data["Step Count"]

fig6 = plt.line(data, x="Time", y="Walking Efficiency",title="Walking Efficiency Over Time")
plot(fig6)



# create time intervals

time_intervals = pd.cut(pd.to_datetime(data["Time"]).dt.hour, bins = [0,12,18,24], labels=["Mornings", "Afternoon", "Evening"],right=False)
data["Time Interval"] = time_intervals

fig3 = plt.scatter(data, x="Step Count", y="Walking Speed", color="Time Interval", title="Step Count and Walking Speed Variations by Time Interval", trendline='ols')
plot(fig3)

# Reshape data for treemap

daily_avg_metrics = data.groupby("Date").mean().reset_index()

daily_avg_metrics_melted = daily_avg_metrics.melt(id_vars=["Date"], value_vars=[ "Distance", "Energy Burned", "Flights Climbed", "Walking Double Support Percentage", "Walking Speed"])

# TreeMap Of Daily Average for Different Metrics Over Several Weeks

fig4 = plt.treemap(daily_avg_metrics_melted, path=["variable"],values="value", color="variable",hover_data=["value"], title="Daily Average for Different Metrics")

plot(fig4)











































