; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x380 ((_ T2_02 0) n)))
(let ((?x381 ((_ T2_01 0) n)))
(let (($x382 (= ?x381 ?x380)))
(let (($x383 (>= n 0)))
(=> $x383 $x382))))))
)
(check-sat)
