; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x300 ((_ T2_08 0) n)))
(let ((?x299 ((_ T2_02 0) n)))
(let (($x323 (= ?x299 ?x300)))
(let (($x298 (>= n 0)))
(=> $x298 $x323))))))
)
(check-sat)
