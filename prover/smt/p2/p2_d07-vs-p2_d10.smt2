; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_10 ((x!1 Int)) Int)
                   ( e2_10 ((x!1 Int)) Int)
                   ( f2_10 ((x!1 Int)) Int)
                   ( p2_10 ((x!1 Int)) Int)
                   ( T2_07 ((x!1 Int)) Int)
                   ( p2_07 ((x!1 Int)) Int)
                   ( ilog2_2_07 ((x!1 Int)) Int)
                   ( xor_2_07 ((x!1 Int) (x!2 Int)) Int))
                 ( (mod (+ ((_ e2_10 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_10 0) (+ ((_ e2_10 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_10 0) x!1) 2) 0)
                        x!1
                        ((_ f2_10 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_10 0) (div x!1 2)) x!1))
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
 (forall ((n Int) )(let ((?x210 ((_ T2_10 0) n)))
(let ((?x256 ((_ T2_07 0) n)))
(let (($x259 (= ?x256 ?x210)))
(let (($x224 (>= n 0)))
(=> $x224 $x259))))))
)
(check-sat)
