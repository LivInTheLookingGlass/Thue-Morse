; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
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
 (forall ((n Int) )(let ((?x481 ((_ T2_09 0) n)))
 (let (($x380 (= ?x481 n)))
 (let ((?x480 ((_ T2_01 0) n)))
 (let (($x503 (= ?x480 n)))
 (let (($x408 (and $x503 $x380)))
 (let (($x387 (< n s)))
 (let (($x409 (>= n 0)))
 (let (($x358 (and $x409 $x387)))
 (=> $x358 $x408))))))))))
 )
(assert
 (let ((?x454 ((_ T2_01 0) s)))
 (= ?x454 1)))
(assert
 (let ((?x455 ((_ T2_09 0) s)))
 (= ?x455 1)))
(assert
 (forall ((n Int) )(let ((?x481 ((_ T2_09 0) n)))
(let ((?x480 ((_ T2_01 0) n)))
(let (($x468 (= ?x480 ?x481)))
(let (($x409 (>= n 0)))
(=> $x409 $x468))))))
)
(check-sat)
