; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_06 ((x!1 Int)) Int)
                   ( pn_06 ((x!1 Int)) Int)
                   ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int))
                 ( ((_ pn_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ pn_06 0) (div x!1 s))) s)))
                     (ite (= x!1 0) 0 a!1))
                   (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))))
(assert
 (forall ((n Int) )(let ((?x370 ((_ Tn_06 0) n)))
(let ((?x358 ((_ T2_08 0) n)))
(let (($x356 (= ?x358 ?x370)))
(let (($x379 (>= n 0)))
(=> $x379 $x356))))))
)
(check-sat)
