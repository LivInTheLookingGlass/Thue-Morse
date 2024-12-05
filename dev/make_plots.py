from collections import defaultdict
from itertools import product
from math import log10, log2

import matplotlib.pyplot as plt
from numpy import linspace


time_map = {
    r'1':                                     1,
    r'\log(n)':                               2,
    r'n':                                     100,
    r'n \cdot \log(n)':                       200,
    r'\log(n)^2 \cdot \log(\log(n))':         4 * (1 + log10(2)),
    r'n \cdot \log(n)^2 \cdot \log(\log(n))': 100 * 4 * (1 + log10(2)),
    r'\log(n)^2':                             2 * 2,
    r'n \cdot \log(n)^2':                     400,
    r'n \cdot \log(n) \cdot \log(\log(n))':   100 * 2 * (1 + log10(2)),
    r'n^2 \cdot \log(n) \cdot \log(\log(n))': 100 * 100 * 2 * (1 + log10(2)),
    r'n^2':                                   100 * 100,
    r'n^2 \cdot \log(n)':                     100 * 100 * 2,
    r'n^{\log_2(3)} \cdot \log(n)':           100**log2(3) * 2,
}

space_map = {
    r'1':                 1,
    r'n':                 100,
    r'\log(n)':           2,
    r'n \cdot \log(n)':   200,
    r'n^2':               100 * 100,
    r'n^2 \cdot \log(n)': 100 * 100 * 2,
    r'n \cdot \log(n)^2': 100 * 4
}

reverse_time_map = {v: k for k, v in time_map.items()}
reverse_space_map = {v: k for k, v in space_map.items()}

get_time_value = time_map.get
get_space_value = space_map.get
get_time_complexity = reverse_time_map.get
get_space_complexity = reverse_space_map.get

# name, times, spaces
# fixed+single, fixed+total, flex+single, flex+total
complexities = [
    ('$T_{2,1}$',
     [r'\log(n)',                     r'n \cdot \log(n)',             r'\log(n)^2 \cdot \log(\log(n))',       r'n \cdot \log(n)^2 \cdot \log(\log(n))'],
     [r'1',                           r'n',                           r'\log(n)',                             r'n \cdot \log(n)']),
    ('$T_{2,4}$',
     [r'\log(n)',                     r'n \cdot \log(n)',             r'\log(n)^2',                           r'n \cdot \log(n)^2 \cdot \log(\log(n))'],
     [r'1',                           r'n',                           r'\log(n)',                             r'n \cdot \log(n)']),
    ('$T_{2,5a}$',
     [r'n',                           r'n^2',                         r'n \cdot \log(n) \cdot \log(\log(n))', r'n^2 \cdot \log(n) \cdot \log(\log(n))'],
     [r'\log(n)',                     r'n \cdot \log(n)',             r'\log(n)^2',                           r'n \cdot \log(n)^2']),
    ('$T_{2,5b}$',
     [r'n',                           r'n^2',                         r'n \cdot \log(n) \cdot \log(\log(n))', r'n^2 \cdot \log(n) \cdot \log(\log(n))'],
     [r'n',                           r'n^2',                         r'n \cdot \log(n)',                     r'n^2 \cdot \log(n)']),
    ('$T_{2,6}$',
     [r'n \cdot \log(n)',             r'n \cdot \log(n)',             r'n \cdot \log(n)^2',                   r'n \cdot \log(n)^2'],
     [r'1',                           r'n',                           r'\log(n)',                             r'n \cdot \log(n)']),
    ('$T_{2,15s}$',
     [r'n',                           r'n^2',                         r'n',                                   r'n^2'],
     [r'n',                           r'n^2',                         r'n \cdot \log(n)',                     r'n^2 \cdot \log(n)']),
    ('$T_{2,15p}$',
     [r'n',                           r'n^2',                         r'n \cdot \log(n) \cdot \log(\log(n))', r'n^2 \cdot \log(n) \cdot \log(\log(n))'],
     [r'1',                           r'n',                           r'\log(n)',                             r'n \cdot \log(n)']),
    ('$T_{2,17}$',
     [r'n^{\log_2(3)} \cdot \log(n)', r'n^{\log_2(3)} \cdot \log(n)', None,                                   None],
     [r'n',                           r'n',                           r'n \cdot \log(n)',                     r'n \cdot \log(n)']),
    ('$T_{n,1}$',
     [r'\log(n)',                     r'n \cdot \log(n)',             r'\log(n)^2 \cdot \log(\log(n))',       r'n \cdot \log(n)^2 \cdot \log(\log(n))'],
     [r'1',                           r'n',                           r'\log(n)',                             r'\n \cdot \log(n)']),
    ('$T_{n,3}$',
     [r'\log(n)',                     r'n \cdot \log(n)',             r'n \cdot \log(n)',                     r'n \cdot \log(n)^2'],
     [r'1',                           r'n',                           r'\log(n)',                             r'n \cdot \log(n)']),
    ('$T_{n,9}$',
     [r'\log(n)',                     r'\log(n)',                     None,                                   None],
     [r'n',                           r'n',                           r'n \cdot \log(n)',                     r'n \cdot \log(n)']),
]


for is_arb, is_total in product(range(2), range(2)):
    groups = defaultdict(list)
    index = is_arb * 2 + is_total

    for name, times, spaces in complexities:
        time_value = get_time_value(times[index])
        space_value = get_space_value(spaces[index])
        if time_value is not None and space_value is not None:
            groups[(time_value, space_value)].append(name)
        # else:
        #     raise ValueError()

    num_entries = sum(len(names) for names in groups.values())
    colors = plt.cm.plasma(linspace(0, 1, num_entries))

    plt.figure(figsize=(8, 6))

    for idx, ((time_value, space_value), names) in enumerate(groups.items()):
        color = colors[idx]
        plt.scatter(time_value, space_value, color=color)
        group_label = ', '.join(names) + f": ($O({get_time_complexity(time_value)})$, $O({get_space_complexity(space_value)})$)"
        plt.plot([], [], 'o', color=color, label=group_label)

    plt.xscale('log')
    plt.yscale('log')

    time_ticks = sorted(set(time_map.values()))
    space_ticks = sorted(set(space_map.values()))

    time_labels = ['$' + get_time_complexity(tick) + '$' for tick in time_ticks]
    space_labels = ['$' + get_space_complexity(tick) + '$' for tick in space_ticks]

    plt.xlim(min(time_ticks) * 0.9, max(time_ticks) * 1.1)
    plt.ylim(min(space_ticks) * 0.9, max(space_ticks) * 1.1)

    plt.xticks(time_ticks, time_labels, rotation=45, ha='right')
    plt.yticks(space_ticks, space_labels)

    plt.xlabel("Time Complexity (Big-O) - Log Scale")
    plt.ylabel("Space Complexity (Big-O) - Log Scale")

    title = "Algorithm Complexity Comparison (Time vs. Space, "

    if is_total:
        title += "Per n Elements, "
    else:
        title += "Per 1 Element, "

    if is_arb:
        title += "Arbitrary Size Integers)"
    else:
        title += "Fixed Size Integers)"
    plt.title(title)

    plt.grid(True, which="both", linestyle='--', linewidth=0.25)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Complexity Groups", fontsize=8)
    plt.savefig(f'src/figures/complexity/complexity_comparison_{is_total}_{is_arb}.svg', format='svg', bbox_inches='tight')
