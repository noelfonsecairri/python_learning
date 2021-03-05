tasks = ["email Frank", "call Sarah", "meet with Zach"]

latest_task_accomplished = tasks.pop(1)

popped_item = "The popped task is " + '"' +latest_task_accomplished + '"'

print(popped_item)
print(tasks)

# a simple for loop that pops
# for task in tasks:
# 	print(tasks)
# 	tasks.remove(task)
# 	print(tasks)