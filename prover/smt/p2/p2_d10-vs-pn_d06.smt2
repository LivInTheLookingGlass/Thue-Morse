; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_06 ((x!1 Int)) Int)
                   ( pn_06 ((x!1 Int)) Int)
                   ( T2_10 ((x!1 Int)) Int)
                   ( e2_10 ((x!1 Int)) Int)
                   ( f2_10 ((x!1 Int)) Int)
                   ( p2_10 ((x!1 Int)) Int))
                 ( ((_ pn_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ pn_06 0) (div x!1 s))) s)))
                     (ite (= x!1 0) 0 a!1))
                   (mod (+ ((_ e2_10 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_10 0) (+ ((_ e2_10 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_10 0) x!1) 2) 0)
                        x!1
                        ((_ f2_10 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_10 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let (($x379 (= ((_ T2_10 0) n) ((_ Tn_06 0) n))))
(let (($x407 (>= n 0)))
(=> $x407 $x379))))
)
(check-sat)
