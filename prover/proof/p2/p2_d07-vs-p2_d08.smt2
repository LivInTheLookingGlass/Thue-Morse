proof-trail(assumption(mp(mp~(mp(asserted(ForAll(n,
                                        Implies(n >= 0,
                                        T2_07(n) == T2_08(n)))),
                                 quant-intro(proof-bind(Lambda(n,
                                        rewrite(Implies(n >=
                                        0,
                                        T2_07(n) == T2_08(n)) ==
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))))),
                                        (ForAll(n,
                                        Implies(n >= 0,
                                        T2_07(n) == T2_08(n)))) ==
                                        (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))))),
                                 ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                              nnf-pos(proof-bind(Lambda(n,
                                        refl(~(Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)),
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))))),
                                      ~(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))),
                                        ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))))),
                              ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                          quant-intro(proof-bind(Lambda(n,
                                        refl(Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)) ==
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))))),
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))) ==
                                      (ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n))))),
                          ForAll(n,
                                 Or(Not(n >= 0),
                                    T2_07(n) == T2_08(n)))),
                       ForAll(n,
                              Or(Not(n >= 0),
                                 T2_07(n) == T2_08(n)))),
            assumption(asserted(recfun-num-rounds),
                       recfun-num-rounds),
            assumption(asserted(seq.max_unfolding),
                       seq.max_unfolding),
            assumption(mp(quant-inst(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                                        Or(Not(1 >= 0),
                                        T2_07(1) == T2_08(1)))),
                          rewrite(Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                                     Or(Not(1 >= 0),
                                        T2_07(1) == T2_08(1))) ==
                                  Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                                     Not(1 >= 0),
                                     T2_07(1) == T2_08(1))),
                          Or(Not(ForAll(n,
                                        Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                             Not(1 >= 0),
                             T2_07(1) == T2_08(1))),
                       Or(Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))),
                          Not(1 >= 0),
                          T2_07(1) == T2_08(1))),
            assumption(assumption,
                       Or(Not(1 >= 0),
                          T2_07(1) == T2_08(1),
                          Not(ForAll(n,
                                     Or(Not(n >= 0),
                                        T2_07(n) == T2_08(n)))))),
            clause-trail-end)