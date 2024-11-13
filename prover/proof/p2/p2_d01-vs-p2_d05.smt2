proof-trail(assumption(mp(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))),
                                    quant-intro(proof-bind(Lambda(n,
                                        trans(monotonicity(rewrite(And(n >=
                                        0,
                                        n < s) ==
                                        And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)) ==
                                        Implies(And(n >= 0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))),
                                        rewrite(Implies(And(n >=
                                        0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))))),
                                        (ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))) ==
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))))),
                                    ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))),
                                 nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(And(n >=
                                        0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))))),
                                        ~(ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))),
                                        ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n))))),
                                 ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))),
                             quant-intro(proof-bind(Lambda(n,
                                        trans(monotonicity(trans(monotonicity(rewrite(And(n >=
                                        0,
                                        Not(s + -1*n <= 0)) ==
                                        Not(Or(Not(n >= 0),
                                        s + -1*n <= 0))),
                                        Not(And(n >= 0,
                                        Not(s + -1*n <= 0))) ==
                                        Not(Not(Or(Not(n >=
                                        0),
                                        s + -1*n <= 0)))),
                                        rewrite(Not(Not(Or(Not(n >=
                                        0),
                                        s + -1*n <= 0))) ==
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0)),
                                        Not(And(n >= 0,
                                        Not(s + -1*n <= 0))) ==
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0)),
                                        rewrite(And(T2_01(n) ==
                                        n,
                                        T2_05(n) == n) ==
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n)))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)) ==
                                        Or(Or(Not(n >= 0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))),
                                        rewrite(Or(Or(Not(n >=
                                        0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n)))) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))))),
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_01(n) == n,
                                        T2_05(n) == n)))) ==
                                        (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))))),
                             ForAll(n,
                                    Or(s + -1*n <= 0,
                                       Not(n >= 0),
                                       Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n)))))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(s + -1*n <=
                                        0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n)))) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))))),
                                      (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n)))))) ==
                                      (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_01(n) ==
                                        n),
                                        Not(T2_05(n) == n))))))),
                          ForAll(n,
                                 Or(s + -1*n <= 0,
                                    Not(n >= 0),
                                    Not(Or(Not(T2_01(n) == n),
                                        Not(T2_05(n) == n)))))),
                       ForAll(n,
                              Or(s + -1*n <= 0,
                                 Not(n >= 0),
                                 Not(Or(Not(T2_01(n) == n),
                                        Not(T2_05(n) == n)))))),
            assumption(asserted(T2_01(s) == 1),
                       T2_01(s) == 1),
            assumption(asserted(T2_05(s) == 1),
                       T2_05(s) == 1),
            assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_01(n) == T2_05(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_01(n) == T2_05(n)) ==
                                        Or(Not(n >= 0),
                                        T2_01(n) == T2_05(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_01(n) == T2_05(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
...