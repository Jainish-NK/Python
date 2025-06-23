events = [{"Ahme_Event":["ram","amit","shyam","ram"]},{"Udaipur_Event":["ram","amit","kunal"]},{"mumbai_Event":["ram","parth","amit","ajay","jay"]}]
#find who have attended all city event
#find all unique persons
#find who have attended udaipur event but not mumbai's

events = [
    {"Ahme_Event": ["ram", "amit", "shyam", "ram"]},
    {"Udaipur_Event": ["ram", "amit", "kunal"]},
    {"mumbai_Event": ["ram", "parth", "amit", "ajay", "jay"]}
]

# Extract attendee lists
ahmedabad = set(events[0]["Ahme_Event"])
udaipur = set(events[1]["Udaipur_Event"])
mumbai = set(events[2]["mumbai_Event"])

# 1. Who have attended all city events
attended_all = ahmedabad & udaipur & mumbai

# 2. All unique persons
all_unique = ahmedabad | udaipur | mumbai

# 3. Attended Udaipur but not Mumbai
udaipur_not_mumbai = udaipur - mumbai

# Print results
print("Attended all city events:", attended_all)
print("All unique persons:", all_unique)
print("Attended Udaipur but not Mumbai:", udaipur_not_mumbai)
