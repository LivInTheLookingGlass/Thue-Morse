; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_09 ((x!1 Int)) Int)
                   ( o2_09 ((x!1 Int)) Int)
                   ( f2_09 ((x!1 Int)) Int)
                   ( p2_09 ((x!1 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (mod (+ ((_ o2_09 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_09 0) (+ ((_ o2_09 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 1 a!1))
                   (ite (= (mod ((_ p2_09 0) x!1) 2) 1)
                        x!1
                        ((_ f2_09 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_09 0) (div x!1 2)) x!1))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x418 ((_ T2_09 0) n)))
 (let (($x380 (= ?x418 n)))
 (let ((?x416 ((_ T2_02 0) n)))
 (let (($x422 (= ?x416 n)))
 (let (($x433 (and $x422 $x380)))
 (let (($x387 (< n s)))
 (let (($x434 (>= n 0)))
 (let (($x358 (and $x434 $x387)))
 (=> $x358 $x433))))))))))
 )
(assert
 (forall ((n Int) )(let ((?x418 ((_ T2_09 0) n)))
(let ((?x416 ((_ T2_02 0) n)))
(let (($x429 (= ?x416 ?x418)))
(let (($x434 (>= n 0)))
(=> $x434 $x429))))))
)
(check-sat)