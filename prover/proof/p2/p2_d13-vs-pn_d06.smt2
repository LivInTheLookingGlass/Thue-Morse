proof-trail(assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_13(n) == Tn_06(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_13(n) == Tn_06(n)) ==
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_13(n) == Tn_06(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                              nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)),
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))))),
                                      ~(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))),
                                        ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))))),
                              ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)) ==
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))))),
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))) ==
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n))))),
                          ForAll(n,
                                 Or(Not(n >= 0),
                                    T2_13(n) == Tn_06(n)))),
                       ForAll(n,
                              Or(Not(n >= 0),
                                 T2_13(n) == Tn_06(n)))),
            assumption(asserted(recfun-num-rounds),
                       recfun-num-rounds),
            assumption(asserted(seq.max_unfolding),
                       seq.max_unfolding),
            assumption(mp(quant-inst(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                                        Or(Not(0 >= 0),
                                        T2_13(0) == Tn_06(0)))),
                          rewrite(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                                     Or(Not(0 >= 0),
                                        T2_13(0) == Tn_06(0))) ==
                                  Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                                     Not(0 >= 0),
                                     T2_13(0) == Tn_06(0))),
                          Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                             Not(0 >= 0),
                             T2_13(0) == Tn_06(0))),
                       Or(Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))),
                          Not(0 >= 0),
                          T2_13(0) == Tn_06(0))),
            assumption(assumption,
                       Or(Not(0 >= 0),
                          T2_13(0) == Tn_06(0),
                          Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_13(n) == Tn_06(n)))))),
            clause-trail-end)