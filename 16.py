import input
from functools import reduce

data = input.get_data("16")

rules = data[:data.index("")]
data = data[data.index("") + 1:]
ticket = data[:data.index("")]
data = data[data.index("") + 1:]

def extract_rules(ruleset):
    rules = {}
    for rule in ruleset:
        key = rule.split(":")[0]
        ranges = rule[rule.index(":"):].split(" ")
        range1 = ranges[1].split("-")
        range2 = ranges[3].split("-")
        rules[key] = [range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1)]

    return rules


def count_of_invalid_fields(tickets, rules):
    invalid_numbers = []
    count = 0
    for ticket in ",".join(tickets[1:]).split(","):
        for key, rule in rules.items():
            if int(ticket) in rule[0] or int(ticket) in rule[1]:
                break
        else:
            invalid_numbers.append(int(ticket))
            count += 1
    print(count)
    return reduce(lambda x, y: x + y, invalid_numbers), invalid_numbers

def extract_tickets(tickets, filter_numbers):
    new_tickets = []
    for ticket in tickets[1:]:
        for field in ticket.split(","):
            if int(field) in filter_numbers:
                break
        else:
            new_tickets.append(ticket)

    return new_tickets

def recursive_condition(x, y, tickets, ranges):
    if y >= len(tickets):
        return True
    ticket = int(tickets[y].split(",")[x])
    if ticket in ranges[0] or ticket in ranges[1]:
        return recursive_condition(x, y + 1, tickets, ranges)
    else:
        return False 

def get_field_order(tickets, rules):
    order = {}
    for x in range(len(tickets[0].split(","))):
        for key, rule in rules.items():
            result = recursive_condition(x, 0, tickets, rule)
            if result:
                if key in order:
                    order[key].add(x)
                else:
                    order[key] = {x}
    print(len(order))
    return order

def handle_orders(orders):
    new_orders = {}
    for key, order in orders.items():
        for x, y in orders.items():
            if key == x:
                continue
            diff = order - y
            if(len(diff) == 1):
                new_orders[key] = diff
    return new_orders

def product_of_departure(ticket, orders):
    ticket = [int(x) for x in ticket[1].split(",")]
    product = 1
    for key, order in orders.items():
        if "departure" in key:
            product *= ticket[list(order)[0]]

    return product

part1 = count_of_invalid_fields(data, extract_rules(rules))
print(part1[0])
data = extract_tickets(data, part1[1])
orders = handle_orders((get_field_order(data, extract_rules(rules))))
print(product_of_departure(ticket, orders))