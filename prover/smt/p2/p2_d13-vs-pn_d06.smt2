; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_06 ((x!1 Int)) Int)
                   ( pn_06 ((x!1 Int)) Int)
                   ( T2_13 ((x!1 Int)) Int)
                   ( gould2_13 ((x!1 Int)) Int)
                   ( partial_sum2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( binomial_coeff2_13 ((x!1 Int) (x!2 Int)) Int))
                 ( ((_ pn_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ pn_06 0) (div x!1 s))) s)))
                     (ite (= x!1 0) 0 a!1))
                   (mod (- ((_ gould2_13 0) x!1) 1) 3)
                   (let ((a!1 (+ (* ((_ partial_sum2_13 0) x!1 0) 2)
                                 (mod ((_ binomial_coeff2_13 0) x!1 (div x!1 2))
                                      2))))
                     (ite (= (mod x!1 2) 0)
                          a!1
                          (* ((_ partial_sum2_13 0) x!1 0) 2)))
                   (let ((a!1 (ite (= (mod ((_ binomial_coeff2_13 0) x!1 x!2) 2)
                                      1)
                                   (+ 1 ((_ partial_sum2_13 0) x!1 (+ x!2 1)))
                                   ((_ partial_sum2_13 0) x!1 (+ x!2 1)))))
                     (ite (> x!2 (div (+ x!1 1) 2)) 0 a!1))
                   (let ((a!1 (div (* ((_ binomial_coeff2_13 0) x!1 (- x!2 1))
                                      (- x!1 (- x!2 1)))
                                   x!2)))
                     (ite (= x!2 0) 1 a!1))))
(assert
 (forall ((n Int) )(let ((?x259 ((_ Tn_06 0) n)))
(let ((?x258 ((_ T2_13 0) n)))
(let (($x282 (= ?x258 ?x259)))
(let (($x257 (>= n 0)))
(=> $x257 $x282))))))
)
(check-sat)
