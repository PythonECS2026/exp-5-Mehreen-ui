# AIM: Task List Manager
# Coder: mehreen ansari
# Date: 20/02/2026

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

tasks.append(input())
print(f"Tasks after Adding: {tasks}")
edit_index = int(input())
tasks[edit_index] = input()
print(f"Tasks after Editing: {tasks}")
tasks.pop(0)
print(f"Tasks after Removing: {tasks}")
tasks.sort()
print(f"Tasks after Sorting: {tasks}") 


