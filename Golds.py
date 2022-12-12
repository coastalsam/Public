def process_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    word = "Yellow"
    line_number = 0
    last_line_number = 0
    min_gap = float("inf")
    max_gap = 0

    golds = []

    for line in lines:
        line_number += 1
        if word in line:
            if last_line_number != 0:
                gap = line_number - last_line_number
                golds.append("You went on a {} case dry streak to get this gold".format(gap))
                min_gap = min(min_gap, gap)
                max_gap = max(max_gap, gap)

            golds.append("Case number {}: {}".format(line_number, line))
            last_line_number = line_number

    def _count_generator(reader):
        b = reader(1024 * 1024)
        while b:
            yield b
            b = reader(1024 * 1024)

    with open(filename, 'rb') as fp:
        c_generator = _count_generator(fp.raw.read)
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        golds.append('Total Cases: {}'.format(count -1))

    with open(filename, 'r') as fp:
        data = fp.read()
        occurrences = data.count("Yellow")
        golds.append('Number of Golds : {}'.format(occurrences))

    difference = count - last_line_number
    golds.append("Amount of cases since last Gold: {}".format(difference))

    golds.append("Smallest number of cases between Golds: {}".format(min_gap))
    golds.append("Largest number of cases between Golds: {}".format(max_gap))

    with open("Golds.txt", "w") as f:
        f.write("\n".join(golds))

process_file("results.txt")

def process_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    word = "(Red)"
    line_number = 0
    last_line_number = 0
    min_gap = float("inf")
    max_gap = 0

    golds = []

    for line in lines:
        line_number += 1
        if word in line:
            if last_line_number != 0:
                gap = line_number - last_line_number
                golds.append("You went on a {} case dry streak to get this Red".format(gap))
                min_gap = min(min_gap, gap)
                max_gap = max(max_gap, gap)

            golds.append("Case number {}: {}".format(line_number, line))
            last_line_number = line_number

    def _count_generator(reader):
        b = reader(1024 * 1024)
        while b:
            yield b
            b = reader(1024 * 1024)

    with open(filename, 'rb') as fp:
        c_generator = _count_generator(fp.raw.read)
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        golds.append('Total Cases: {}'.format(count -1))

    with open(filename, 'r') as fp:
        data = fp.read()
        occurrences = data.count("(Red)")
        golds.append('Number of Redss : {}'.format(occurrences))

    difference = count - last_line_number
    golds.append("Amount of cases since last Reds: {}".format(difference))

    golds.append("Smallest number of cases between Reds: {}".format(min_gap))
    golds.append("Largest number of cases between Reds: {}".format(max_gap))

    with open("Reds.txt", "w") as f:
        f.write("\n".join(golds))

process_file("results.txt")

import re

results = open('results.txt').read().split('\n')

case_data = {}
for result in results:
  match = re.search(r'(.*)->(.*) \| (.*) \((.*)\) \((.*)\)', result)
  if match:
    case_type = match.group(1)
    float = match.group(4)
    rarity = match.group(5)
    if case_type not in case_data:
      case_data[case_type] = {'Wears': {}, 'Rarities': {}, 'Total': 0}
    if float not in case_data[case_type]['Wears']:
      case_data[case_type]['Wears'][float] = 0
    if rarity not in case_data[case_type]['Rarities']:
      case_data[case_type]['Rarities'][rarity] = 0
    case_data[case_type]['Wears'][float] += 1
    case_data[case_type]['Rarities'][rarity] += 1
    case_data[case_type]['Total'] += 1

f = open('CasesInfo.txt', 'w')
for case_type, data in case_data.items():
  f.write(f'{case_type} ({data["Total"]})\n')
  f.write('Wears\n')
  total = data['Total']
  Wears = ['Battle-Scarred', 'Well-Worn', 'Field-Tested', 'Minimal Wear', 'Factory New']
  for float in Wears:
    if float in data['Wears']:
      f.write(f'  {float}: {data["Wears"][float]} ({data["Wears"][float] / total * 100:.2f}%)\n')
    else:
      f.write(f'  {float}: 0 (0.00%)\n')
  f.write('Rarities\n')
  Rarities = ['Blue', 'Purple', 'Pink', 'Red', 'Yellow']
  for rarity in Rarities:
    if rarity in data['Rarities']:
      f.write(f'  {rarity}: {data["Rarities"][rarity]} ({data["Rarities"][rarity] / total * 100:.2f}%)\n')
    else:
      f.write(f'  {rarity}: 0 (0.00%)\n')
f.close()
