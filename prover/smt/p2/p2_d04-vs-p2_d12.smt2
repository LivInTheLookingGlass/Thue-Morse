; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_12 ((x!1 Int)) Int)
                   ( e2_12 ((x!1 Int)) Int)
                   ( fe2_12 ((x!1 Int)) Int)
                   ( p2_12 ((x!1 Int)) Int)
                   ( T2_04 ((x!1 Int)) Int)
                   ( t2_04 ((x!1 Int)) String)
                   ( sub2_04 ((x!1 String) (x!2 String)) String)
                   ( ilog2_2_04 ((x!1 Int)) Int))
                 ( (mod (+ ((_ e2_12 0) x!1) 1) 2)
                   (let ((a!1 ((_ fe2_12 0) (+ ((_ e2_12 0) (- x!1 1)) 1))))
                     (ite (= x!1 0) 0 a!1))
                   (ite (= (mod ((_ p2_12 0) x!1) 2) 0)
                        x!1
                        ((_ fe2_12 0) (+ x!1 1)))
                   (ite (= x!1 0) 0 (+ ((_ p2_12 0) (div x!1 2)) x!1))
                   (let ((a!1 (str.substr ((_ t2_04 0)
                                            (+ ((_ ilog2_2_04 0) x!1) 1))
                                          x!1
                                          1)))
                     (ite (= a!1 "0") 0 1))
                   (ite (= x!1 0)
                        "0"
                        ((_ sub2_04 0) "" ((_ t2_04 0) (- x!1 1))))
                   (let ((a!1 (str.++ x!1
                                      (ite (= (str.substr x!2 0 1) "0")
                                           "01"
                                           "10")
                                      (str.substr x!2 1 (- (str.len x!2) 1)))))
                     (ite (= (str.len x!2) 0) x!1 a!1))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_04 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x379 ((_ T2_12 0) n)))
(let ((?x356 ((_ T2_04 0) n)))
(let (($x322 (= ?x356 ?x379)))
(let (($x358 (>= n 0)))
(=> $x358 $x322))))))
)
(check-sat)
