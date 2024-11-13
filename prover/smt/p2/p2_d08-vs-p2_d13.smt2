; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_13 ((x!1 Int)) Int)
                   ( gould2_13 ((x!1 Int)) Int)
                   ( partial_sum2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( binomial_coeff2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int))
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
                   (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))))
(assert
 (forall ((n Int) )(let ((?x381 ((_ T2_13 0) n)))
(let ((?x406 ((_ T2_08 0) n)))
(let (($x407 (= ?x406 ?x381)))
(let (($x382 (>= n 0)))
(=> $x382 $x407))))))
)
(check-sat)
