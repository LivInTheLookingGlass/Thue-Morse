proof-trail(assumption(mp(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))),
                                    quant-intro(proof-bind(Lambda(n,
                                        trans(monotonicity(rewrite(And(n >=
                                        0,
                                        n < s) ==
                                        And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)) ==
                                        Implies(And(n >= 0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))),
                                        rewrite(Implies(And(n >=
                                        0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))))),
                                        (ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))) ==
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))))),
                                    ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))),
                                 nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(And(n >=
                                        0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))))),
                                        ~(ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))),
                                        ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n))))),
                                 ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))),
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
                                        rewrite(And(T2_02(n) ==
                                        n,
                                        T2_07(n) == n) ==
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n)))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)) ==
                                        Or(Or(Not(n >= 0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))),
                                        rewrite(Or(Or(Not(n >=
                                        0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n)))) ==
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)) ==
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))))),
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        T2_07(n) == n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))))),
                             ForAll(n,
                                    Or(Not(n >= 0),
                                       s + -1*n <= 0,
                                       Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n)))))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n)))) ==
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))))),
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n)))))) ==
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        s + -1*n <= 0,
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(T2_07(n) == n))))))),
                          ForAll(n,
                                 Or(Not(n >= 0),
                                    s + -1*n <= 0,
                                    Not(Or(Not(T2_02(n) == n),
                                        Not(T2_07(n) == n)))))),
                       ForAll(n,
                              Or(Not(n >= 0),
                                 s + -1*n <= 0,
                                 Not(Or(Not(T2_02(n) == n),
                                        Not(T2_07(n) == n)))))),
            assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_02(n) == T2_07(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_02(n) == T2_07(n)) ==
                                        Or(Not(n >= 0),
                                        T2_02(n) == T2_07(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_02(n) == T2_07(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_02(n) == T2_07(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_02(n) == T2_07(n)))),
                              nnf-pos(proof-bind(Lambda(n,
...