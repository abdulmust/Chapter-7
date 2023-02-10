sandwich_orders = ['pastrami', 'chicken', 'tuna', 'pastrami', 'egg', 'ham', 'beef', 'pastrami']
finished_sandwiches = []
print("The Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")