; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_12 ((x!1 Int)) Int)
                   ( e2_12 ((x!1 Int)) Int)
                   ( fe2_12 ((x!1 Int)) Int)
                   ( p2_12 ((x!1 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (mod (+ ((_ e2_12 0) x!1) 1) 2)
                   (let ((a!1 ((_ fe2_12 0) (+ ((_ e2_12 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_12 0) x!1) 2) 0)
                        x!1
                        ((_ fe2_12 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_12 0) (div x!1 2)) x!1))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x449 ((_ T2_12 0) n)))
 (let (($x407 (= ?x449 n)))
 (let ((?x448 ((_ T2_02 0) n)))
 (let (($x465 (= ?x448 n)))
 (let (($x488 (and $x465 $x407)))
 (let (($x387 (< n s)))
 (let (($x492 (>= n 0)))
 (let (($x428 (and $x492 $x387)))
 (=> $x428 $x488))))))))))
 )
(assert
 (forall ((n Int) )(let ((?x449 ((_ T2_12 0) n)))
(let ((?x448 ((_ T2_02 0) n)))
(let (($x485 (= ?x448 ?x449)))
(let (($x492 (>= n 0)))
(=> $x492 $x485))))))
)
(check-sat)