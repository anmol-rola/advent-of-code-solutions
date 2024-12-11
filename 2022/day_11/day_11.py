from os import path

input = open(f"{path.dirname(__file__)}/input.txt", "r").read()


def perform_operation(operation, curr_value):
    if operation["type"] == "+":
        return curr_value + (
            curr_value if operation["arg"] == "old" else int(operation["arg"])
        )
    else:
        return curr_value * (
            curr_value if operation["arg"] == "old" else int(operation["arg"])
        )


def parse_operation(operation):
    statement = operation.split("new = ")[-1]
    parsed_operation = {}
    parsed_operation["type"] = statement.split(" ")[1]
    parsed_operation["arg"] = statement.split(" ")[2]
    return parsed_operation


def create_input():
    monkeys = {}
    input_lines = input.split("\n")
    for start in range(0, len(input_lines), 7):
        stats_text = input_lines[start : start + 7]
        monkey_index = stats_text[0].replace(":", "").replace("Monkey ", "")
        stats_parsed = {}
        stats_parsed["items"] = [
            int(item)
            for item in stats_text[1]
            .strip()
            .replace("Starting items: ", "")
            .split(", ")
        ]
        stats_parsed["operation"] = parse_operation(stats_text[2])
        stats_parsed["test"] = {
            "divisor": int(stats_text[3].split(" ")[-1]),
            "true": stats_text[4].split(" ")[-1],
            "false": stats_text[5].split(" ")[-1],
        }
        stats_parsed["inspect_count"] = 0
        monkeys[monkey_index] = stats_parsed
    return monkeys


parsed_input = create_input()

for index in range(0, 20):
    for monkey in parsed_input.keys():
        stats = parsed_input[monkey]
        for item in stats["items"]:
            worry_level = perform_operation(stats["operation"], item)
            worry_level = worry_level // 3

            if worry_level % stats["test"]["divisor"]:
                next_monkey = stats["test"]["false"]
                worry_level = worry_level % parsed_input[next_monkey]["test"]["divisor"]
                parsed_input[next_monkey]["items"].append(worry_level)
            else:
                next_monkey = stats["test"]["true"]
                worry_level = worry_level % parsed_input[next_monkey]["test"]["divisor"]
                parsed_input[next_monkey]["items"].append(worry_level)
            stats["inspect_count"] += 1
        stats["items"] = []

inspect_counts = [value['inspect_count'] for value in parsed_input.values()]
print(inspect_counts)
inspect_counts = sorted(inspect_counts)
print(inspect_counts[-1] * inspect_counts[-2])
