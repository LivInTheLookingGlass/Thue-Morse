; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_12 ((x!1 Int)) Int)
                   ( e2_12 ((x!1 Int)) Int)
                   ( fe2_12 ((x!1 Int)) Int)
                   ( p2_12 ((x!1 Int)) Int)
                   ( T2_11 ((x!1 Int)) Int)
                   ( p2_11 ((x!1 Int)) Int)
                   ( ilog2_2_11 ((x!1 Int)) Int))
                 ( (mod (+ ((_ e2_12 0) x!1) 1) 2)
                   (let ((a!1 ((_ fe2_12 0) (+ ((_ e2_12 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_12 0) x!1) 2) 0)
                        x!1
                        ((_ fe2_12 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_12 0) (div x!1 2)) x!1))
                   (+ (- 1 ((_ p2_11 0) (+ x!1 1))) ((_ p2_11 0) x!1))
                   (let ((a!1 (* (mod ((_ ilog2_2_11 0) (+ x!1 1)) 2)
                                 (mod x!1 2))))
                     (+ (div x!1 2) a!1))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_11 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x215 ((_ T2_12 0) n)))
(let ((?x265 ((_ T2_11 0) n)))
(let (($x297 (= ?x265 ?x215)))
(let (($x251 (>= n 0)))
(=> $x251 $x297))))))
)
(check-sat)
