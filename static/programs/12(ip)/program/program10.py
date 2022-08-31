import matplotlib.pyplot as pl
#list of the five consecutive year
year = ['2015','2016','2017','2018','2019']
#list of pass percentage
pass_per=[85.50,95.6,90.5,97.5,98.9]
#color code of bar charts
col=['b','g','r','m','c']
pl.bar(year,pass_per,width=0.2,color=col)
#label for x-axis and y-axis
pl.xlabel("year")
pl.ylabel("Pass%")
#function to display bar chart
pl.show()
