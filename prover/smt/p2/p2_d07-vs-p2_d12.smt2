; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_12 ((x!1 Int)) Int)
                   ( e2_12 ((x!1 Int)) Int)
                   ( fe2_12 ((x!1 Int)) Int)
                   ( p2_12 ((x!1 Int)) Int)
                   ( T2_07 ((x!1 Int)) Int)
                   ( p2_07 ((x!1 Int)) Int)
                   ( ilog2_2_07 ((x!1 Int)) Int)
                   ( xor_2_07 ((x!1 Int) (x!2 Int)) Int))
                 ( (mod (+ ((_ e2_12 0) x!1) 1) 2)
                   (let ((a!1 ((_ fe2_12 0) (+ ((_ e2_12 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_12 0) x!1) 2) 0)
                        x!1
                        ((_ fe2_12 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_12 0) (div x!1 2)) x!1))
                   (let ((a!1 (ite (= (mod ((_ p2_07 0) x!1) 2) 0)
                                   (- 1 ((_ T2_07 0) (- x!1 1)))
                                   ((_ T2_07 0) (- x!1 1)))))
                     (ite (= x!1 0) 0 a!1))
                   (+ ((_ ilog2_2_07 0) ((_ xor_2_07 0) x!1 (- x!1 1))) 1)
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_07 0) (div x!1 2))))
                   (let ((a!1 (+ (mod (+ (mod x!1 2) (mod x!2 2)) 2)
                                 (* 2 ((_ xor_2_07 0) (div x!1 2) (div x!2 2))))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))))
(assert
 (forall ((n Int) )(let ((?x406 ((_ T2_12 0) n)))
 (let (($x407 (= ?x406 n)))
 (let ((?x408 ((_ T2_07 0) n)))
 (let (($x409 (= ?x408 n)))
 (let (($x410 (and $x409 $x407)))
 (let (($x387 (< n s)))
 (let (($x411 (>= n 0)))
 (let (($x412 (and $x411 $x387)))
 (=> $x412 $x410))))))))))
 )
(assert
 (forall ((n Int) )(let ((?x406 ((_ T2_12 0) n)))
(let ((?x408 ((_ T2_07 0) n)))
(let (($x383 (= ?x408 ?x406)))
(let (($x411 (>= n 0)))
(=> $x411 $x383))))))
)
(check-sat)