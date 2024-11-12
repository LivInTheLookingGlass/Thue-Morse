; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_13 ((x!1 Int)) Int)
                   ( gould2_13 ((x!1 Int)) Int)
                   ( partial_sum2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( binomial_coeff2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_05 ((x!1 Int)) Int)
                   ( t2_05 ((x!1 Int)) String)
                   ( rot2_05 ((x!1 String) (x!2 Int)) String)
                   ( ilog2_2_05 ((x!1 Int)) Int))
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
                   (let ((a!1 (str.substr ((_ t2_05 0)
                                            (+ ((_ ilog2_2_05 0) x!1) 1))
                                          x!1
                                          1)))
                     (ite (= a!1 "0") 0 1))
                   (let ((a!1 (div (str.len ((_ t2_05 0) (- x!1 1))) 2)))
                   (let ((a!2 (str.++ ((_ t2_05 0) (- x!1 1))
                                      ((_ rot2_05 0)
                                        ((_ t2_05 0) (- x!1 1))
                                        a!1))))
                     (ite (= x!1 0) "0" a!2)))
                   (str.++ (str.substr x!1 x!2 (- (str.len x!1) x!2))
                           (str.substr x!1 0 x!2))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_05 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x215 ((_ T2_13 0) n)))
(let ((?x265 ((_ T2_05 0) n)))
(let (($x297 (= ?x265 ?x215)))
(let (($x251 (>= n 0)))
(=> $x251 $x297))))))
)
(check-sat)
