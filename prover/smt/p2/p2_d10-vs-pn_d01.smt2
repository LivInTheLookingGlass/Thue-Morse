; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_01 ((x!1 Int)) Int)
                   ( pn_01 ((x!1 Int)) Int)
                   ( T2_10 ((x!1 Int)) Int)
                   ( e2_10 ((x!1 Int)) Int)
                   ( f2_10 ((x!1 Int)) Int)
                   ( p2_10 ((x!1 Int)) Int))
                 ( (mod ((_ pn_01 0) x!1) s)
                   (ite (= x!1 0) 0 (+ ((_ pn_01 0) (div x!1 s)) x!1))
                   (mod (+ ((_ e2_10 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_10 0) (+ ((_ e2_10 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_10 0) x!1) 2) 0)
                        x!1
                        ((_ f2_10 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_10 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x257 ((_ Tn_01 0) n)))
(let ((?x282 ((_ T2_10 0) n)))
(let (($x283 (= ?x282 ?x257)))
(let (($x258 (>= n 0)))
(=> $x258 $x283))))))
)
(check-sat)
