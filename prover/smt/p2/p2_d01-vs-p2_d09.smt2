; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_09 ((x!1 Int)) Int)
                   ( o2_09 ((x!1 Int)) Int)
                   ( f2_09 ((x!1 Int)) Int)
                   ( p2_09 ((x!1 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (mod (+ ((_ o2_09 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_09 0) (+ ((_ o2_09 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 1 a!1))
                   (ite (= (mod ((_ p2_09 0) x!1) 2) 1)
                        x!1
                        ((_ f2_09 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_09 0) (div x!1 2)) x!1))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x298 ((_ T2_09 0) n)))
(let ((?x323 ((_ T2_01 0) n)))
(let (($x324 (= ?x323 ?x298)))
(let (($x299 (>= n 0)))
(=> $x299 $x324))))))
)
(check-sat)
