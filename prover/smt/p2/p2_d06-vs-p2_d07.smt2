; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_07 ((x!1 Int)) Int)
                   ( p2_07 ((x!1 Int)) Int)
                   ( ilog2_2_07 ((x!1 Int)) Int)
                   ( xor_2_07 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_06 ((x!1 Int)) Int)
                   ( p2_06 ((x!1 Int)) Int))
                 ( (let ((a!1 (ite (= (mod ((_ p2_07 0) x!1) 2) 0)
                                   (- 1 ((_ T2_07 0) (- x!1 1)))
                                   ((_ T2_07 0) (- x!1 1)))))
                     (ite (= x!1 0) 0 a!1))
                   (+ ((_ ilog2_2_07 0) ((_ xor_2_07 0) x!1 (- x!1 1))) 1)
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_07 0) (div x!1 2))))
                   (let ((a!1 (+ (mod (+ (mod x!1 2) (mod x!2 2)) 2)
                                 (* 2 ((_ xor_2_07 0) (div x!1 2) (div x!2 2))))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   ((_ p2_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ p2_06 0) (div x!1 2))) 2)))
                     (ite (= x!1 0) 0 a!1))))
(assert
 (forall ((n Int) )(let ((?x250 ((_ T2_07 0) n)))
(let ((?x215 ((_ T2_06 0) n)))
(let (($x251 (= ?x215 ?x250)))
(let (($x296 (>= n 0)))
(=> $x296 $x251))))))
)
(check-sat)
