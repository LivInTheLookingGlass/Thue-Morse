; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_10 ((x!1 Int)) Int)
                   ( e2_10 ((x!1 Int)) Int)
                   ( f2_10 ((x!1 Int)) Int)
                   ( p2_10 ((x!1 Int)) Int)
                   ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int))
                 ( (mod (+ ((_ e2_10 0) x!1) 1) 2)
                   (let ((a!1 ((_ f2_10 0) (+ ((_ e2_10 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_10 0) x!1) 2) 0)
                        x!1
                        ((_ f2_10 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_10 0) (div x!1 2)) x!1))
                   (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))))
(assert
 (forall ((n Int) )(let ((?x283 ((_ T2_10 0) n)))
(let ((?x255 ((_ T2_08 0) n)))
(let (($x174 (= ?x255 ?x283)))
(let (($x209 (>= n 0)))
(=> $x209 $x174))))))
)
(check-sat)
