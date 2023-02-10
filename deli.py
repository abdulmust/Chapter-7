sandwich_orders = ['chicken', 'tuna', 'egg', 'ham', 'beef']
finished_sandwiches = []
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich} sandwich.")
    finished_sandwiches.append(made_sandwich)
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())