; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_01 ((x!1 Int)) Int)
                   ( pn_01 ((x!1 Int)) Int)
                   ( T2_06 ((x!1 Int)) Int)
                   ( p2_06 ((x!1 Int)) Int))
                 ( (mod ((_ pn_01 0) x!1) s)
                   (ite (= x!1 0) 0 (+ ((_ pn_01 0) (div x!1 s)) x!1))
                   ((_ p2_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ p2_06 0) (div x!1 2))) 2)))
                     (ite (= x!1 0) 0 a!1))))
(assert
 (forall ((n Int) )(let ((?x215 ((_ Tn_01 0) n)))
(let ((?x265 ((_ T2_06 0) n)))
(let (($x297 (= ?x265 ?x215)))
(let (($x251 (>= n 0)))
(=> $x251 $x297))))))
)
(check-sat)
