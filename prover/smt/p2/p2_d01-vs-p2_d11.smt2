; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_11 ((x!1 Int)) Int)
                   ( p2_11 ((x!1 Int)) Int)
                   ( ilog2_2_11 ((x!1 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (+ (- 1 ((_ p2_11 0) (+ x!1 1))) ((_ p2_11 0) x!1))
                   (let ((a!1 (* (mod ((_ ilog2_2_11 0) (+ x!1 1)) 2)
                                 (mod x!1 2))))
                     (+ (div x!1 2) a!1))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_11 0) (div x!1 2))))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x257 ((_ T2_11 0) n)))
(let ((?x282 ((_ T2_01 0) n)))
(let (($x283 (= ?x282 ?x257)))
(let (($x258 (>= n 0)))
(=> $x258 $x283))))))
)
(check-sat)
