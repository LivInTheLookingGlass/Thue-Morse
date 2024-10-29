from itertools import combinations
from multiprocessing import AsyncResult, Event, Pool
from os import path
from subprocess import PIPE, CalledProcessError, Popen
from subprocess import Result as SResult
from tempfile import TemporaryDirectory
from time import sleep
from typing import Dict, Tuple

FORMULAS = {
    'p2_d01': '...',  # Replace with Prover9 representation
    'p2_d02': '...',
    'p2_d03': '...',
    'p2_d04': '...',
    'p2_d05': '...',
    'p2_d06': '...',
    'p2_d07': '...',
    'p2_d08': '...',
    'p2_d09': '...',
    'p2_d10': '...',
    'pn_d01': '...',  # make sure these are template strings, so you can define s
    'pn_d02': '...',
    'pn_d03': '...',
    'pn_d04': '...',
    'pn_d05': '...',
}

# Groupings
P2_GROUP = [f'p2_d{str(i).zfill(2)}' for i in range(1, 11)]
PN_GROUP = [f'pn_d{str(i).zfill(2)}' for i in range(1, 6)]


def run_prover9(formula1: str, formula2: str, stop_event: Event) -> Tuple[bool, int, str, str]:
    with TemporaryDirectory() as tempdir:
        input1_path = path.join(tempdir, 'input1.m')
        input2_path = path.join(tempdir, 'input2.m')

        with open(input1_path, 'w') as f:
            f.write(formula1)

        with open(input2_path, 'w') as f:
            f.write(formula2)

        process = Popen([
            'nice', '-n', '19',  # lowest priority
            'ionice', '-c', '2', '-n', '7',  # lowest non-idle priority
            'prover9', '-f', input1_path, input2_path
        ], stdout=PIPE, stderr=PIPE, text=True)
        
        # Polling for the process and checking the stop event
        while True:
            if stop_event.is_set():
                process.terminate()  # Terminate the process if the stop event is set
                return False, process.returncode, '', ''

            retcode = process.poll()
            if retcode is not None:
                stdout, stderr = process.communicate()
                return retcode == 0, retcode, stdout, stderr

            sleep(0.1)  # Small sleep to avoid busy-waiting


def main():
    equiv = {
        f: {f} for f in P2_GROUP + PN_GROUP
    }
    equiv['p2_d01'].add('p2_d04')
    equiv['p2_d01'].add('pn_d01')
    equiv['p2_d04'].add('p2_d01')
    equiv['pn_d01'].add('p2_d01')
    with Pool() as pool:
        comparisons: Dict[Tuple[str, str], Tuple[Event, AsyncResult]] = {}
        # Proving all p2_dX are equivalent
        for a, b in combinations(P2_GROUP, 2):
            if a in equiv[b]: continue
            stop = Event()
            comparisons[a, b] = (stop, pool.apply_async(run_prover9, (FORMULAS[a], FORMULAS[b], stop)))
        # Proving p2_dX and pn_dX are equivalent for given X
        for a, b in zip(P2_GROUP, PN_GROUP):
            if a in equiv[b]: continue
            stop = Event()
            comparisons[a, b] = (stop, pool.apply_async(run_prover9, (FORMULAS[a], FORMULAS[b].format('2'), stop)))
        # Proving all pn_dX are equivalent
        for a, b in combinations(PN_GROUP, 2):
            if a in equiv[b]: continue
            stop = Event()
            comparisons[a, b] = (stop, pool.apply_async(run_prover9, (FORMULAS[a].format('s'), FORMULAS[b].format('s'), stop)))

        # collect results while eliminating obviated comparisons
        while comparisons:
            for f1, f2 in tuple(comparisons.keys()):
                e, p = comparisons[f1, f2]
                if p.ready():
                    try:
                        terminated, retcode, stdout, stderr = p.get()
                    except CalledProcessError as e:
                        print(f'Comparison for {f1} & {f2} failed!')
                        print(e)
                    if not terminated and retcode == 0:
                        print(f'{f1} == {f2}!')
                        print('--------- stdout ---------')
                        print(stdout)
                        print('--------- stderr ---------')
                        print(stderr)
                        print('---------  done  ---------')
                        equiv_set = {f1, f2}
                        cur_len = 0
                        while cur_len != len(equiv_set):
                            equiv_set = {f for f in P2_GROUP + PN_GROUP if any(f in equiv[g] for g in equiv_set)}
                        for f in equiv_set:
                            equiv[f].update(equiv_set)
                        for g1, g2 in combinations(equiv_set, 2):
                            if (g1, g2) in comparisons:
                                comparisons[g1, g2][0].set()
                                del comparisons[g1, g2]
                    elif terminated:
                        contained = 'in' if f1 in equiv[f2] else 'not in'
                        print(f'Comparison between {f1} and {f2} terminated. They are {contained} the equiv set')
                    elif retcode:
                        print(f'Comparison between {f1} and {f2} failed!')
                        print('--------- stdout ---------')
                        print(stdout)
                        print('--------- stderr ---------')
                        print(stderr)
                        print('---------  done  ---------')
            sleep(0.1)  # Avoid busy-wait


if __name__ == "__main__":
    main()
