print("Welcome to your weekly time calculator")
#gives the user a welcome message
time = int(input("How many hours a week do you spend in class? "))
#asks the user how many hours a week they spend and class and stores the input
free_time = int(input("How many hours of free time do you have per week? "))
#asks the user how many hours of free time they have a week and stores the input
sleep = int(input("How many hours of sleep do you get per week? "))
#asks the user how many hours of sleep they get per week and stores the input
print(f"You spend {round(time / 168 * 100)}% of your week in class!")
#prints the % of time a week the user spends in class
print(f"{round(free_time / 168 * 100)}% of your week is free time!")
#prints the % of time a week the user has of free time
print(f"{round(sleep / 168 * 100)}% of your week is spent sleeping!"
#prints the % of time a week the user sleeps