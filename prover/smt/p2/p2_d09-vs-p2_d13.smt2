; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_13 ((x!1 Int)) Int)
                   ( gould2_13 ((x!1 Int)) Int)
                   ( partial_sum2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( binomial_coeff2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_09 ((x!1 Int)) Int)
                   ( o2_09 ((x!1 Int)) Int)
                   ( f2_09 ((x!1 Int)) Int)
                   ( p2_09 ((x!1 Int)) Int))
                 ( (mod (- ((_ gould2_13 0) x!1) 1) 3)
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
                     (ite (= x!2 0) 1 a!1))
                   (mod (+ ((_ o2_09 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_09 0) (+ ((_ o2_09 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 1 a!1))
                   (ite (= (mod ((_ p2_09 0) x!1) 2) 1)
                        x!1
                        ((_ f2_09 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_09 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x256 ((_ T2_13 0) n)))
(let ((?x257 ((_ T2_09 0) n)))
(let (($x258 (= ?x257 ?x256)))
(let (($x259 (>= n 0)))
(=> $x259 $x258))))))
)
(check-sat)
