proof-trail(assumption(asserted(s >= 2), s >= 2),
            assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        Tn_01(n) == Tn_06(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        Tn_01(n) == Tn_06(n)) ==
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        Tn_01(n) == Tn_06(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                              nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)),
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))))),
                                      ~(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))),
                                        ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))))),
                              ForAll(n,
                                     Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)) ==
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))))),
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))) ==
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n))))),
                          ForAll(n,
                                 Or(Not(n >= 0),
                                    Tn_01(n) == Tn_06(n)))),
                       ForAll(n,
                              Or(Not(n >= 0),
                                 Tn_01(n) == Tn_06(n)))),
            assumption(asserted(recfun-num-rounds),
                       recfun-num-rounds),
            assumption(asserted(seq.max_unfolding),
                       seq.max_unfolding),
            th-assumption(th-lemma(Or(0%0 + -1*mod0(0, 0) >=
                                      0,
                                      0%0 + -1*mod0(0, 0) <=
                                      0)),
                          Or(0%0 + -1*mod0(0, 0) >= 0,
                             0%0 + -1*mod0(0, 0) <= 0)),
            th-assumption(th-lemma(Or(0%0 + -1*mod0(0, 0) >=
                                      0,
                                      0%0 + -1*mod0(0, 0) <=
                                      0)),
                          Or(0%0 + -1*mod0(0, 0) <= 0,
                             0%0 + -1*mod0(0, 0) >= 0)),
            th-assumption(th-lemma(Or(Not(0%0 == mod0(0, 0)),
                                      0%0 + -1*mod0(0, 0) <=
                                      0)),
                          Or(Not(0%0 == mod0(0, 0)),
                             0%0 + -1*mod0(0, 0) <= 0)),
            th-assumption(th-lemma(Or(Not(0%0 == mod0(0, 0)),
                                      0%0 + -1*mod0(0, 0) <=
                                      0)),
                          Or(Not(0%0 == mod0(0, 0)),
                             0%0 + -1*mod0(0, 0) <= 0)),
            th-assumption(th-lemma(Or(Not(0%0 == mod0(0, 0)),
                                      0%0 + -1*mod0(0, 0) >=
                                      0)),
                          Or(Not(0%0 == mod0(0, 0)),
                             0%0 + -1*mod0(0, 0) >= 0)),
            th-assumption(th-lemma(Or(Not(0%0 == mod0(0, 0)),
                                      0%0 + -1*mod0(0, 0) >=
                                      0)),
                          Or(Not(0%0 == mod0(0, 0)),
                             0%0 + -1*mod0(0, 0) >= 0)),
            th-assumption(th-lemma(Or(0%0 == mod0(0, 0),
                                      Not(0%0 +
                                        -1*mod0(0, 0) <=
                                        0),
                                      Not(0%0 +
                                        -1*mod0(0, 0) >=
                                        0))),
                          Or(0%0 == mod0(0, 0),
                             Not(0%0 + -1*mod0(0, 0) <= 0),
                             Not(0%0 + -1*mod0(0, 0) >= 0))),
            th-assumption(th-lemma(Or(0%0 == mod0(0, 0),
                                      Not(0%0 +
                                        -1*mod0(0, 0) <=
                                        0),
                                      Not(0%0 +
                                        -1*mod0(0, 0) >=
                                        0))),
                          Or(0%0 == mod0(0, 0),
                             Not(0%0 + -1*mod0(0, 0) <= 0),
                             Not(0%0 + -1*mod0(0, 0) >= 0))),
            th-assumption(th-lemma(Or(0%s >= 0, 0%s <= 0)),
                          Or(0%s >= 0, 0%s <= 0)),
            th-assumption(th-lemma(Or(0%s >= 0, 0%s <= 0)),
                          Or(0%s <= 0, 0%s >= 0)),
            th-assumption(th-lemma(Or(Not(0 == 0%s),
                                      0%s <= 0)),
                          Or(Not(0 == 0%s), 0%s <= 0)),
            th-assumption(th-lemma(Or(Not(0 == 0%s),
                                      0%s <= 0)),
                          Or(Not(0 == 0%s), 0%s <= 0)),
            th-assumption(th-lemma(Or(Not(0 == 0%s),
                                      0%s >= 0)),
                          Or(Not(0 == 0%s), 0%s >= 0)),
            th-assumption(th-lemma(Or(Not(0 == 0%s),
                                      0%s >= 0)),
                          Or(Not(0 == 0%s), 0%s >= 0)),
            th-assumption(th-lemma(Or(0 == 0%s,
                                      Not(0%s <= 0),
                                      Not(0%s >= 0))),
                          Or(0 == 0%s,
                             Not(0%s <= 0),
                             Not(0%s >= 0))),
            th-assumption(th-lemma(Or(0 == 0%s,
                                      Not(0%s <= 0),
                                      Not(0%s >= 0))),
                          Or(0 == 0%s,
                             Not(0%s <= 0),
                             Not(0%s >= 0))),
            assumption(mp(quant-inst(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                        Or(Not(0 >= 0),
                                        Tn_01(0) == Tn_06(0)))),
                          trans(monotonicity(trans(monotonicity(trans(monotonicity(rewrite((0 >=
                                        0) ==
                                        True),
                                        Not(0 >= 0) ==
                                        Not(True)),
                                        rewrite(Not(True) ==
                                        False),
                                        Not(0 >= 0) == False),
                                        rewrite((Tn_01(0) ==
                                        Tn_06(0)) ==
                                        (0%s == 0)),
                                        Or(Not(0 >= 0),
                                        Tn_01(0) == Tn_06(0)) ==
                                        Or(False, 0%s == 0)),
                                        rewrite(Or(False,
                                        0%s == 0) ==
                                        (0%s == 0)),
                                        Or(Not(0 >= 0),
                                        Tn_01(0) == Tn_06(0)) ==
                                        (0%s == 0)),
                                        Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                        Or(Not(0 >= 0),
                                        Tn_01(0) == Tn_06(0))) ==
                                        Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                        0%s == 0)),
                                rewrite(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                        0%s == 0) ==
                                        Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                        0%s == 0)),
                                Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                   Or(Not(0 >= 0),
                                      Tn_01(0) == Tn_06(0))) ==
                                Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                                   0%s == 0)),
                          Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                             0%s == 0)),
                       Or(Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        Tn_01(n) == Tn_06(n)))),
                          0%s == 0)),
            th-assumption(th-lemma(Or(s >= 0, Not(s >= 2))),
                          Or(s >= 0, Not(s >= 2))),
            th-assumption(th-lemma(Or(s <= 0, s >= 0)),
                          Or(s <= 0, s >= 0)),
            th-assumption(th-lemma(Or(0/s + -1*div0(0, s) >=
                                      0,
                                      0/s + -1*div0(0, s) <=
...