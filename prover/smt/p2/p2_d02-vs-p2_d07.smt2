; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_07 ((x!1 Int)) Int)
                   ( p2_07 ((x!1 Int)) Int)
                   ( ilog2_2_07 ((x!1 Int)) Int)
                   ( xor_2_07 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (let ((a!1 (ite (= (mod ((_ p2_07 0) x!1) 2) 0)
                                   (- 1 ((_ T2_07 0) (- x!1 1)))
                                   ((_ T2_07 0) (- x!1 1)))))
                     (ite (= x!1 0) 0 a!1))
                   (+ ((_ ilog2_2_07 0) ((_ xor_2_07 0) x!1 (- x!1 1))) 1)
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_07 0) (div x!1 2))))
                   (let ((a!1 (+ (mod (+ (mod x!1 2) (mod x!2 2)) 2)
                                 (* 2 ((_ xor_2_07 0) (div x!1 2) (div x!2 2))))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x379 ((_ T2_07 0) n)))
 (let (($x380 (= ?x379 n)))
 (let ((?x381 ((_ T2_02 0) n)))
 (let (($x382 (= ?x381 n)))
 (let (($x416 (and $x382 $x380)))
 (let (($x387 (< n s)))
 (let (($x418 (>= n 0)))
 (let (($x420 (and $x418 $x387)))
 (=> $x420 $x416))))))))))
 )
(assert
 (forall ((n Int) )(let ((?x379 ((_ T2_07 0) n)))
(let ((?x381 ((_ T2_02 0) n)))
(let (($x414 (= ?x381 ?x379)))
(let (($x418 (>= n 0)))
(=> $x418 $x414))))))
)
(check-sat)