; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_03 ((x!1 Int)) Int)
                   ( t2_03 ((x!1 Int)) String)
                   ( invert2_03 ((x!1 String)) String)
                   ( ilog2_2_03 ((x!1 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (let ((a!1 (str.substr ((_ t2_03 0)
                                            (+ ((_ ilog2_2_03 0) x!1) 1))
                                          x!1
                                          1)))
                     (ite (= a!1 "0") 0 1))
                   (let ((a!1 (str.++ ((_ t2_03 0) (- x!1 1))
                                      ((_ invert2_03 0) ((_ t2_03 0) (- x!1 1))))))
                     (ite (= x!1 0) "0" a!1))
                   (let ((a!1 ((_ invert2_03 0)
                                (str.substr x!1 1 (- (str.len x!1) 1)))))
                   (let ((a!2 (ite (= x!1 "0")
                                   "1"
                                   (str.++ ((_ invert2_03 0)
                                             (str.substr x!1 0 1))
                                           a!1))))
                     (ite (= x!1 "") "" (ite (= x!1 "1") "0" a!2))))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_03 0) (div x!1 2))))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x283 ((_ T2_03 0) n)))
(let ((?x255 ((_ T2_01 0) n)))
(let (($x174 (= ?x255 ?x283)))
(let (($x209 (>= n 0)))
(=> $x209 $x174))))))
)
(check-sat)
