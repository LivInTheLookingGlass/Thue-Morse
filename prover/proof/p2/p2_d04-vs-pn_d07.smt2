th-lemma(th-lemma(Length(str.substr(t2_04(-863 +
                                        ilog2_2_04(s)),
                                    1,
                                    -1 +
                                    Length(t2_04(-863 +
                                        ilog2_2_04(s))))) >=
                  0),
         unit-resolution(th-lemma(Or(Not(seq.length_limit),
                                     Length(t2_04(-862 +
                                        ilog2_2_04(s))) <=
                                     1)),
                         unit-resolution(th-lemma(Or(Not(seq.max_unfolding),
                                        seq.length_limit)),
                                        asserted(seq.max_unfolding),
                                        seq.length_limit),
                         Length(t2_04(-862 + ilog2_2_04(s))) <=
                         1),
         unit-resolution(th-lemma(Or(Not(Length(t2_04(-862 +
                                        ilog2_2_04(s))) ==
                                        2 +
                                        Length(str.substr(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        1,
                                        -1 +
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))))),
                                     Length(t2_04(-862 +
                                        ilog2_2_04(s))) +
                                     -1*
                                     (2 +
                                      Length(str.substr(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        1,
                                        -1 +
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))))) >=
                                     0)),
                         trans*(symm(monotonicity(symm(th-lemma(mp(trans*(commutativity((Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        0) ==
                                        (0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))))),
                                        iff-false(unit-resolution(th-lemma(Or(Not(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0)),
                                        unit-resolution(th-lemma(Or(Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1),
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0))),
                                        unit-resolution(th-lemma(Or(Not(1 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(...)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1)),
                                        trans*(th-lemma(1 ==
                                        Length(Unit(48))),
                                        symm(monotonicity(symm(unit-resolution(th-lemma(Or(Not(...),
                                        ... == ...)),
                                        unit-resolution(th-lemma(Or(...,
                                        ...)),
                                        unit-resolution(lemma(...,
                                        ...),
                                        unit-resolution(...,
                                        ...,
                                        ...),
                                        case-def(...)),
                                        ilog2_2_04(...) ==
                                        863),
                                        Unit(48) ==
                                        t2_04(... + ...)),
                                        t2_04(-863 +
                                        ilog2_2_04(...)) ==
                                        Unit(48)),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(...))) ==
                                        Length(Unit(48))),
                                        Length(Unit(48)) ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        1 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1),
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0)),
                                        Not(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))))),
                                        (0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))) ==
                                        False),
                                        (Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        0) ==
                                        False),
                                        rewrite(((Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        0) ==
                                        False) ==
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        0)),
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        0)),
                                        trans*(unit-resolution(th-lemma(Or(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))),
                                        At(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        0) ==
                                        Unit(seq.nth_i(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        0)))),
                                        unit-resolution(th-lemma(Or(Not(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0)),
                                        unit-resolution(th-lemma(Or(Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1),
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0))),
                                        unit-resolution(th-lemma(Or(Not(1 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1)),
                                        trans*(th-lemma(1 ==
                                        Length(Unit(48))),
                                        symm(monotonicity(symm(unit-resolution(th-lemma(Or(Not(... ==
                                        ...),
                                        Unit(...) ==
                                        t2_04(...))),
                                        unit-resolution(th-lemma(Or(Not(...),
                                        ... == ...)),
                                        unit-resolution(lemma(unit-resolution(...,
                                        ...,
                                        ...,
                                        ...),
                                        Or(..., ...)),
                                        unit-resolution(lemma(...,
                                        ...),
                                        asserted(...),
                                        Not(...)),
                                        case-def(... + ...)),
                                        ilog2_2_04(s) == 863),
                                        Unit(48) ==
                                        t2_04(-863 +
                                        ilog2_2_04(...))),
                                        t2_04(-863 +
                                        ilog2_2_04(s)) ==
                                        Unit(48)),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) ==
                                        Length(Unit(48))),
                                        Length(Unit(48)) ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        1 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s)))),
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))) >=
                                        1),
                                        Not(Length(t2_04(-863 +
                                        ilog2_2_04(s))) <=
                                        0)),
                                        Not(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))))),
                                        At(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        0) ==
                                        Unit(seq.nth_i(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        0))),
                                        monotonicity(symm(th-lemma(unit-resolution(th-lemma(Or(0 ==
                                        Length(t2_04(-863 +
                                        ilog2_2_04(s))),
                                        seq.eq(t2_04(-863 +
                                        ilog2_2_04(s)),
                                        Concat(Unit(seq.nth_i(t2_04(-863 +
                                        ilog2_2_04(...)),
                                        0)),
...