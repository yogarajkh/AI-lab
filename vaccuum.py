
goal_state = {"A": "0", "B": "0"}
cost = 0


room_state = {"A": "0", "B": "0"}
location = input("Enter the location of vacuum cleaner (A or B): ")

for room in room_state:
room_state[room] = input(f"Enter state of room {room} (0=Clean, 1=Dirty): ")

print("\nGoal state is:", goal_state)
print("Initial Room state is:", room_state)


if location == "A":
if room_state["A"] == "1":
room_state["A"] = "0"
cost += 1
print("Room A was dirty → Cleaned. Cost for cleaning A = 1")

if room_state == goal_state:
print("\nGoal Reached! ")
print("Total Maintenance Cost:", cost)
else:
print("Room A is clean → Moving from A to B. Cost = 1")
cost += 1
if room_state["B"] == "1":
room_state["B"] = "0"
cost += 1
print("Room B was dirty → Cleaned. Cost for cleaning B = 1")


elif location == "B":
if room_state["B"] == "1":
room_state["B"] = "0"
cost += 1
print("Room B was dirty → Cleaned. Cost for cleaning B = 1")

if room_state == goal_state:
print("\nGoal Reached! ")
print("Total Maintenance Cost:", cost)
else:
print("Room B is clean → Moving from B to A. Cost = 1")
cost += 1
if room_state["A"] == "1":
room_state["A"] = "0"
cost += 1
print("Room A was dirty → Cleaned. Cost for cleaning A = 1")


if room_state == goal_state:
print("\nGoal Reached! ")
else:
print("\nSome rooms are still dirty ")

print("Final Room State:", room_state)
print("Total Maintenance Cost:", cost)
