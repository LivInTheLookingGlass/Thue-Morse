; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x455 ((_ T2_08 0) n)))
 (let (($x407 (= ?x455 n)))
 (let ((?x454 ((_ T2_01 0) n)))
 (let (($x477 (= ?x454 n)))
 (let (($x370 (and $x477 $x407)))
 (let (($x387 (< n s)))
 (let (($x356 (>= n 0)))
 (let (($x428 (and $x356 $x387)))
 (=> $x428 $x370))))))))))
 )
(assert
 (let ((?x433 ((_ T2_01 0) s)))
 (= ?x433 1)))
(assert
 (let ((?x434 ((_ T2_08 0) s)))
 (= ?x434 1)))
(assert
 (forall ((n Int) )(let ((?x455 ((_ T2_08 0) n)))
(let ((?x454 ((_ T2_01 0) n)))
(let (($x441 (= ?x454 ?x455)))
(let (($x356 (>= n 0)))
(=> $x356 $x441))))))
)
(check-sat)