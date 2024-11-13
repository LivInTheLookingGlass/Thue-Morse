unit-resolution(unit-resolution(th-lemma(Or(1 ==
                                        binomial_coeff2_13(s,
                                        1)%
                                        2,
                                        Not(binomial_coeff2_13(s,
                                        1)%
                                        2 <=
                                        1),
                                        Not(binomial_coeff2_13(s,
                                        1)%
                                        2 >=
                                        1))),
                                unit-resolution(th-lemma(Or(Not(binomial_coeff2_13(s,
                                        1)%
                                        2 +
                                        -1*(s%2) >=
                                        0),
                                        Not((1 + s)%2 >= 0),
                                        Not((1 + s)/2 >= 1),
                                        Not(1 +
                                        s +
                                        -1*
                                        (2*((1 + s)/2) +
                                        (1 + s)%2) >=
                                        0),
                                        Not(s/2 <= 0),
                                        Not(s +
                                        -1*(2*(s/2) + s%2) <=
                                        0),
                                        binomial_coeff2_13(s,
                                        1)%
                                        2 >=
                                        1)),
                                        unit-resolution(th-lemma(Or(Not(case-def(s,
                                        1)),
                                        (1 + s)/2 >= 1)),
                                        unit-resolution(lemma(unit-resolution(unit-resolution(th-lemma(Or(Not(0 ==
                                        (s/2)/2),
                                        (s/2)/2 >= 0)),
                                        unit-resolution(lemma(mp(trans*(symm(trans*(symm(th-lemma(T2_01(s) ==
                                        p2_01(s)%2),
                                        p2_01(s)%2 ==
                                        T2_01(s)),
                                        asserted(T2_01(s) ==
                                        1),
                                        p2_01(s)%2 == 1),
                                        1 == p2_01(s)%2),
                                        monotonicity(trans*(symm(unit-resolution(lemma(unit-resolution(hypothesis(Not(... ==
                                        ...)),
                                        mp(trans*(unit-resolution(...,
                                        ...,
                                        ...),
                                        symm(..., ...),
                                        ... == ...),
                                        symm(monotonicity(...,
                                        ...),
                                        (...) == (...)),
                                        ... + ... ==
                                        p2_01(...)),
                                        False),
                                        Or(Not(0 == ...%...),
                                        s + p2_01(...) ==
                                        p2_01(s),
                                        Not(.../... == 0))),
                                        hypothesis(0 == s%2),
                                        mp(unit-resolution(th-lemma(Or(... ==
                                        ...,
                                        Not(...),
                                        Not(...))),
                                        hypothesis(.../... <=
                                        0),
                                        unit-resolution(th-lemma(Or(...,
                                        ...,
                                        ...,
                                        ...)),
                                        hypothesis(... >=
                                        ...),
                                        unit-resolution(th-lemma(...),
                                        true-axiom(...),
                                        ... >= ...),
                                        unit-resolution(th-lemma(...),
                                        unit-resolution(...,
                                        ...,
                                        ...),
                                        ... >= ...),
                                        .../... >= 0),
                                        0 == s/2),
                                        commutativity((0 ==
                                        .../...) ==
                                        (.../... == 0)),
                                        s/2 == 0),
                                        s + p2_01(s/2) ==
                                        p2_01(s)),
                                        p2_01(s) ==
                                        s + p2_01(s/2)),
                                        th-lemma(unit-resolution(th-lemma(Or(Not(0 ==
                                        p2_01(...)),
                                        p2_01(.../...) >= 0)),
                                        unit-resolution(th-lemma(Or(Not(... ==
                                        ...),
                                        0 == p2_01(...))),
                                        mp(unit-resolution(th-lemma(Or(...,
                                        ...,
                                        ...)),
                                        hypothesis(... <=
                                        ...),
                                        unit-resolution(th-lemma(...),
                                        hypothesis(...),
                                        unit-resolution(...,
                                        ...,
                                        ...),
                                        unit-resolution(...,
                                        ...,
                                        ...),
                                        ... >= ...),
                                        0 == .../...),
                                        commutativity((... ==
                                        ...) ==
                                        (... == ...)),
                                        s/2 == 0),
                                        0 == p2_01(s/2)),
                                        p2_01(s/2) >= 0),
                                        hypothesis(s/2 <= 0),
                                        unit-resolution(th-lemma(Or(Not(s ==
                                        ... + ...),
                                        s + ...*(...) <= 0)),
                                        unit-resolution(th-lemma(Or(False,
                                        s == ... + ...)),
                                        true-axiom(True),
                                        s ==
                                        2*(.../...) + s%2),
                                        s +
                                        -1*
                                        (...*(...) + ...%...) <=
                                        0),
                                        unit-resolution(th-lemma(Or(Not(s ==
                                        ... + ...),
                                        s + ...*(...) >= 0)),
                                        unit-resolution(th-lemma(Or(False,
                                        s == ... + ...)),
                                        true-axiom(True),
                                        s ==
                                        2*(.../...) + s%2),
                                        s +
                                        -1*
                                        (...*(...) + ...%...) >=
                                        0),
                                        unit-resolution(th-lemma(Or(Not(1 ==
                                        binomial_coeff2_13(...,
                                        ...)),
                                        binomial_coeff2_13(s,
                                        0) <=
                                        1)),
                                        th-lemma(1 ==
                                        binomial_coeff2_13(s,
                                        0)),
                                        binomial_coeff2_13(s,
                                        0) <=
                                        1),
                                        unit-resolution(th-lemma(Or(Not(... +
                                        ... ==
                                        binomial_coeff2_13(...,
                                        ...)),
                                        ...*(...) +
                                        ...%... +
                                        ...*... <=
                                        0)),
                                        unit-resolution(th-lemma(Or(False,
                                        ... + ... ==
                                        binomial_coeff2_13(...,
                                        ...))),
                                        true-axiom(True),
                                        2*(.../...) +
                                        binomial_coeff2_13(...,
                                        ...)%
                                        2 ==
                                        binomial_coeff2_13(s,
                                        1)),
                                        2*
                                        (binomial_coeff2_13(...,
                                        ...)/
                                        2) +
                                        binomial_coeff2_13(s,
                                        1)%
                                        2 +
                                        -1*
                                        binomial_coeff2_13(s,
                                        1) <=
                                        0),
                                        unit-resolution(th-lemma(Or(Not(1 ==
                                        binomial_coeff2_13(...,
                                        ...)),
                                        binomial_coeff2_13(s,
                                        0) >=
                                        1)),
                                        th-lemma(1 ==
                                        binomial_coeff2_13(s,
                                        0)),
                                        binomial_coeff2_13(s,
                                        0) >=
...