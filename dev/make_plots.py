from collections import defaultdict
from enum import Enum, auto
from itertools import product
from math import log2, log10
from typing import Callable, Dict, List, Optional, Tuple, cast

from matplotlib import colormaps as cm
from matplotlib import pyplot as plt
from numpy import linspace


class ComplexityEnum(Enum):
    CONST           = auto()
    LOG             = auto()
    LOG_SQUARE      = auto()
    LOG2_LOGLOG     = auto()
    LINEAR          = auto()
    LIN_LOG         = auto()
    LIN_LOG_LOGLOG  = auto()
    LIN_LOG2        = auto()
    LIN_LOG2_LOGLOG = auto()
    LIN_TO_LOG3_LOG = auto()
    LIN2            = auto()
    LIN2_LOG        = auto()
    LIN2_LOG_LOGLOG = auto()
    UNKNOWN         = auto()


CE = ComplexityEnum
enum_map: Dict[ComplexityEnum, str] = {
    CE.CONST           : r'1',
    CE.LOG             : r'\log(n)',
    CE.LOG_SQUARE      : r'\log(n)^2',
    CE.LOG2_LOGLOG     : r'\log(n)^2 \cdot \log(\log(n))',
    CE.LINEAR          : r'n',
    CE.LIN_LOG         : r'n \cdot \log(n)',
    CE.LIN_LOG_LOGLOG  : r'n \cdot \log(n) \cdot \log(\log(n))',
    CE.LIN_LOG2        : r'n \cdot \log(n)^2',
    CE.LIN_LOG2_LOGLOG : r'n \cdot \log(n)^2 \cdot \log(\log(n))',
    CE.LIN_TO_LOG3_LOG : r'n^{\log_2(3)} \cdot \log(n)',
    CE.LIN2            : r'n^2',
    CE.LIN2_LOG        : r'n^2 \cdot \log(n)',
    CE.LIN2_LOG_LOGLOG : r'n^2 \cdot \log(n) \cdot \log(\log(n))',
}

get_comp_name = enum_map.get

time_map: Dict[str, float] = {
    enum_map[CE.CONST]:           1,
    enum_map[CE.LOG]:             2,
    enum_map[CE.LOG_SQUARE]:      2 * 2,
    enum_map[CE.LOG2_LOGLOG]:     4 * (1 + log10(2)),
    enum_map[CE.LINEAR]:          100,
    enum_map[CE.LIN_LOG]:         200,
    enum_map[CE.LIN_LOG_LOGLOG]:  200 * (1 + log10(2)),
    enum_map[CE.LIN_LOG2]:        400,
    enum_map[CE.LIN_LOG2_LOGLOG]: 400 * (1 + log10(2)),
    enum_map[CE.LIN_TO_LOG3_LOG]: 100**log2(3) * 2,
    enum_map[CE.LIN2]:            100 * 100,
    enum_map[CE.LIN2_LOG]:        100 * 100 * 2,
    enum_map[CE.LIN2_LOG_LOGLOG]: 100 * 100 * 2 * (1 + log10(2)),
}

space_map: Dict[str, float] = {
    enum_map[CE.CONST]:      1,
    enum_map[CE.LOG]:        2,
    enum_map[CE.LINEAR]:     100,
    enum_map[CE.LIN_LOG]:    200,
    enum_map[CE.LIN2]:       100 * 100,
    enum_map[CE.LIN2_LOG]:   100 * 100 * 2,
    enum_map[CE.LIN_LOG2]:   100 * 4,
}

reverse_time_map = {v: k for k, v in time_map.items()}
reverse_space_map = {v: k for k, v in space_map.items()}

get_time_value = cast(Callable[[Optional[str]], Optional[float]], time_map.get)
get_space_value = cast(Callable[[Optional[str]], Optional[float]], space_map.get)
get_time_complexity = reverse_time_map.get
get_space_complexity = reverse_space_map.get

# name, times, spaces
# fixed+single, fixed+total, flex+single, flex+total
complexities: List[Tuple[
    str,
    Tuple[ComplexityEnum, ComplexityEnum, ComplexityEnum, ComplexityEnum],
    Tuple[ComplexityEnum, ComplexityEnum, ComplexityEnum, ComplexityEnum]]] = [
    ('$T_{2,1}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LOG2_LOGLOG,    CE.LIN_LOG2_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,2}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LOG2_LOGLOG,    CE.LIN_LOG2_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,3}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,4}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LOG_SQUARE,     CE.LIN2_LOG_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,5r}$',
     (CE.LINEAR,          CE.LIN2,            CE.LIN_LOG_LOGLOG, CE.LIN2_LOG_LOGLOG),
     (CE.LOG,             CE.LIN_LOG,         CE.LOG_SQUARE,     CE.LIN_LOG2)),
    ('$T_{2,5d}$',
     (CE.LINEAR,          CE.LIN2,            CE.LIN_LOG_LOGLOG, CE.LIN2_LOG_LOGLOG),
     (CE.LINEAR,          CE.LIN2,            CE.LIN_LOG,        CE.LIN2_LOG)),
    ('$T_{2,6}$',
     (CE.LIN_LOG,         CE.LIN_LOG,         CE.LIN_LOG2,       CE.LIN_LOG2),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,7}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LOG2_LOGLOG,    CE.LIN_LOG2_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,8}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,9}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,10}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,11}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,12}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,13}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,14}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,15s}$',
     (CE.LINEAR,          CE.LIN2,            CE.LINEAR,         CE.LIN2),
     (CE.LINEAR,          CE.LIN2,            CE.LIN_LOG,        CE.LIN2_LOG)),
    ('$T_{2,15p}$',
     (CE.LINEAR,          CE.LIN2,            CE.LIN_LOG_LOGLOG, CE.LIN_LOG_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{2,16}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,17}$',
     (CE.LIN_TO_LOG3_LOG, CE.LIN_TO_LOG3_LOG, CE.UNKNOWN,        CE.UNKNOWN),
     (CE.LINEAR,          CE.LINEAR,          CE.LIN_LOG,        CE.LIN_LOG)),
    ('$T_{2,18}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,19}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{2,20}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,1}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LOG2_LOGLOG,    CE.LIN_LOG2_LOGLOG),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{n,2}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,3}$',
     (CE.LOG,             CE.LIN_LOG,         CE.LIN_LOG,        CE.LIN_LOG2),
     (CE.CONST,           CE.LINEAR,          CE.LOG,            CE.LIN_LOG)),
    ('$T_{n,4}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,5}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,6}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,7}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,8}$',
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN),
     (CE.UNKNOWN,         CE.UNKNOWN,         CE.UNKNOWN,        CE.UNKNOWN)),
    ('$T_{n,9}$',
     (CE.LOG,             CE.LOG,             CE.UNKNOWN,        CE.UNKNOWN),
     (CE.LINEAR,          CE.LINEAR,          CE.LIN_LOG,        CE.LIN_LOG)),
]


for is_arb, is_total in product(range(2), range(2)):
    groups = defaultdict(list)
    index = is_arb * 2 + is_total

    for name, times, spaces in complexities:
        time_value = get_time_value(get_comp_name(times[index]))
        space_value = get_space_value(get_comp_name(spaces[index]))
        if time_value is not None and space_value is not None:
            groups[(time_value, space_value)].append(name)
        # else:
        #     raise ValueError()

    num_entries = sum(len(names) for names in groups.values())
    if num_entries <= 10:
        map_name = 'tab10'
    elif num_entries <= 20:
        map_name = 'tab20'
    else:
        map_name = 'hsv'
    colors = cm[map_name](linspace(0, 1, num_entries))
    markers = ['o', '^', 's', 'p', 'P', '*', 'X', 'D', 'v', 'h', '<', '>', 'H']

    plt.figure(figsize=(8, 6))

    for idx, ((time_value, space_value), names) in enumerate(groups.items()):
        color = colors[idx]
        marker = markers[idx % len(markers)]
        plt.scatter(time_value, space_value, marker=marker, color=color)
        tc = get_time_complexity(time_value)
        sc = get_space_complexity(space_value)
        group_label = ', '.join(names) + f": ($O({tc})$, $O({sc})$)"
        plt.plot([], [], marker, color=color, label=group_label)

    plt.xscale('log')
    plt.yscale('log')

    time_ticks = sorted(set(time_map.values()))
    space_ticks = sorted(set(space_map.values()))

    time_labels = ['$' + cast(str, get_time_complexity(tick)) + '$' for tick in time_ticks]
    space_labels = ['$' + cast(str, get_space_complexity(tick)) + '$' for tick in space_ticks]

    plt.xlim(min(time_ticks) * 0.88, max(time_ticks) * 1.18)
    plt.ylim(min(space_ticks) * 0.88, max(space_ticks) * 1.18)

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
    plt.savefig(
        f'src/figures/complexity/complexity_comparison_{is_total}_{is_arb}.svg',
        format='svg',
        bbox_inches='tight'
    )
