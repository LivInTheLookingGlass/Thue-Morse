proof-trail(assumption(mp(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))),
                                    quant-intro(proof-bind(Lambda(n,
                                        trans(monotonicity(rewrite(And(n >=
                                        0,
                                        n < s) ==
                                        And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)) ==
                                        Implies(And(n >= 0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))),
                                        rewrite(Implies(And(n >=
                                        0,
                                        Not(s + -1*n <= 0)),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))),
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)) ==
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))))),
                                        (ForAll(n,
                                        Implies(And(n >= 0,
                                        n < s),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))) ==
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))))),
                                    ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))),
                                 nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(And(n >=
                                        0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))))),
                                        ~(ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))),
                                        ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n))))),
                                 ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))),
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
                                        Tn_01(n) == n) ==
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n)))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)) ==
                                        Or(Or(Not(n >= 0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))),
                                        rewrite(Or(Or(Not(n >=
                                        0),
                                        s + -1*n <= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n)))) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))),
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))))),
                                        (ForAll(n,
                                        Or(Not(And(n >= 0,
                                        Not(s + -1*n <= 0))),
                                        And(T2_02(n) == n,
                                        Tn_01(n) == n)))) ==
                                        (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))))),
                             ForAll(n,
                                    Or(s + -1*n <= 0,
                                       Not(n >= 0),
                                       Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n)))))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(s + -1*n <=
                                        0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n)))) ==
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))))),
                                      (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n)))))) ==
                                      (ForAll(n,
                                        Or(s + -1*n <= 0,
                                        Not(n >= 0),
                                        Not(Or(Not(T2_02(n) ==
                                        n),
                                        Not(Tn_01(n) == n))))))),
                          ForAll(n,
                                 Or(s + -1*n <= 0,
                                    Not(n >= 0),
                                    Not(Or(Not(T2_02(n) == n),
                                        Not(Tn_01(n) == n)))))),
                       ForAll(n,
                              Or(s + -1*n <= 0,
                                 Not(n >= 0),
                                 Not(Or(Not(T2_02(n) == n),
                                        Not(Tn_01(n) == n)))))),
            assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_02(n) == Tn_01(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_02(n) == Tn_01(n)) ==
                                        Or(Not(n >= 0),
                                        T2_02(n) == Tn_01(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_02(n) == Tn_01(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_02(n) == Tn_01(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_02(n) == Tn_01(n)))),
...