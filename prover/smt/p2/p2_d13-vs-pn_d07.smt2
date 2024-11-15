; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_07 ((x!1 Int)) Int)
                   ( ilog2 ((x!1 Int) (x!2 Int)) Int)
                   ( xorn ((x!1 Int) (x!2 Int) (x!3 Int)) Int)
                   ( T2_13 ((x!1 Int)) Int)
                   ( gould2_13 ((x!1 Int)) Int)
                   ( partial_sum2_13 ((x!1 Int) (x!2 Int)) Int)
                   ( binomial_coeff2_13 ((x!1 Int) (x!2 Int)) Int))
                 ( (let ((a!1 (+ ((_ ilog2 0) ((_ xorn 0) x!1 (- x!1 1) s) s)
                                 ((_ Tn_07 0) (- x!1 1))
                                 1)))
                     (ite (< x!1 s) x!1 (mod a!1 s)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2 0) (div x!1 x!2) x!2)))
                   (let ((a!1 (+ (mod (+ (mod x!1 x!3) (mod x!2 x!3)) x!3)
                                 (* x!3
                                    ((_ xorn 0) (div x!1 x!3) (div x!2 x!3) x!3)))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
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
 (forall ((n Int) )(let ((?x417 ((_ Tn_07 0) n)))
(let ((?x419 ((_ T2_13 0) n)))
(let (($x16471 (= ?x419 ?x417)))
(let (($x418 (>= n 0)))
(=> $x418 $x16471))))))
)
(check-sat)