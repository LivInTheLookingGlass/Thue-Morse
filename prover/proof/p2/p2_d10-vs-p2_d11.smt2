proof-trail(assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_10(n) == T2_11(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_10(n) == T2_11(n)) ==
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_10(n) == T2_11(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                              nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)),
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))))),
                                      ~(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))),
                                        ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))))),
                              ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)) ==
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))))),
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))) ==
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n))))),
                          ForAll(n,
                                 Or(Not(n >= 0),
                                    T2_10(n) == T2_11(n)))),
                       ForAll(n,
                              Or(Not(n >= 0),
                                 T2_10(n) == T2_11(n)))),
            assumption(asserted(recfun-num-rounds),
                       recfun-num-rounds),
            assumption(asserted(seq.max_unfolding),
                       seq.max_unfolding),
            assumption(mp(quant-inst(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                                        Or(Not(0 >= 0),
                                        T2_10(0) == T2_11(0)))),
                          rewrite(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                                     Or(Not(0 >= 0),
                                        T2_10(0) == T2_11(0))) ==
                                  Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                                     Not(0 >= 0),
                                     T2_10(0) == T2_11(0))),
                          Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                             Not(0 >= 0),
                             T2_10(0) == T2_11(0))),
                       Or(Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))),
                          Not(0 >= 0),
                          T2_10(0) == T2_11(0))),
            assumption(assumption,
                       Or(Not(0 >= 0),
                          T2_10(0) == T2_11(0),
                          Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_10(n) == T2_11(n)))))),
            clause-trail-end)