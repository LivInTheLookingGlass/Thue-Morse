; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_04 ((x!1 Int)) Int)
                   ( t2_04 ((x!1 Int)) String)
                   ( sub2_04 ((x!1 String) (x!2 String)) String)
                   ( ilog2_2_04 ((x!1 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (let ((a!1 (str.substr ((_ t2_04 0)
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
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_04 0) (div x!1 2))))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x358 ((_ T2_04 0) n)))
(let ((?x322 ((_ T2_02 0) n)))
(let (($x380 (= ?x322 ?x358)))
(let (($x356 (>= n 0)))
(=> $x356 $x380))))))
)
(check-sat)
