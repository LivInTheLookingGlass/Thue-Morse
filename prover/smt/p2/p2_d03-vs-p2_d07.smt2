; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_07 ((x!1 Int)) Int)
                   ( p2_07 ((x!1 Int)) Int)
                   ( ilog2_2_07 ((x!1 Int)) Int)
                   ( xor_2_07 ((x!1 Int) (x!2 Int)) Int)
                   ( T2_03 ((x!1 Int)) Int)
                   ( t2_03 ((x!1 Int)) String)
                   ( invert2_03 ((x!1 String)) String)
                   ( ilog2_2_03 ((x!1 Int)) Int))
                 ( (let ((a!1 (ite (= (mod ((_ p2_07 0) x!1) 2) 0)
                                   (- 1 ((_ T2_07 0) (- x!1 1)))
                                   ((_ T2_07 0) (- x!1 1)))))
                     (ite (= x!1 0) 0 a!1))
                   (+ ((_ ilog2_2_07 0) ((_ xor_2_07 0) x!1 (- x!1 1))) 1)
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_07 0) (div x!1 2))))
                   (let ((a!1 (+ (mod (+ (mod x!1 2) (mod x!2 2)) 2)
                                 (* 2 ((_ xor_2_07 0) (div x!1 2) (div x!2 2))))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   (let ((a!1 (str.substr ((_ t2_03 0)
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
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_03 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x407 ((_ T2_07 0) n)))
(let ((?x379 ((_ T2_03 0) n)))
(let (($x358 (= ?x379 ?x407)))
(let (($x370 (>= n 0)))
(=> $x370 $x358))))))
)
(check-sat)