#importing modules
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random
import csv
import pandas as pd

# reading .csv file and converting in .tolist()
df = pd.read_csv("codeData/data.csv")
data = df["reading score"].tolist()

# finding mean,median,mode,standard deviation of data variable
mean=stats.mean(data)
median=stats.median(data)
mode=stats.mode(data)
std_dev=stats.stdev(data)

# calculating
first_std_deviation_start, first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start, second_std_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_dev), mean+(3*std_dev)


# plotting chart and adding traces to it
fig = ff.create_distplot([data], ["reading score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

# printing
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

#printing results
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))


# python




