; benchmark generated from python API
(set-info :status unknown)
(define-funs-rec ( ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int)
                   ( T2_05 ((x!1 Int)) Int)
                   ( t2_05 ((x!1 Int)) String)
                   ( rot2_05 ((x!1 String) (x!2 Int)) String)
                   ( ilog2_2_05 ((x!1 Int)) Int))
                 ( (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))
                   (let ((a!1 (str.substr ((_ t2_05 0)
                                            (+ ((_ ilog2_2_05 0) x!1) 1))
                                          x!1
                                          1)))
                     (ite (= a!1 "0") 0 1))
                   (let ((a!1 (div (str.len ((_ t2_05 0) (- x!1 1))) 2)))
                   (let ((a!2 (str.++ ((_ t2_05 0) (- x!1 1))
                                      ((_ rot2_05 0)
                                        ((_ t2_05 0) (- x!1 1))
                                        a!1))))
                     (ite (= x!1 0) "0" (ite (= x!1 1) "01" a!2))))
                   (str.++ (str.substr x!1 x!2 (- (str.len x!1) x!2))
                           (str.substr x!1 0 x!2))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_05 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x382 ((_ T2_08 0) n)))
(let ((?x407 ((_ T2_05 0) n)))
(let (($x370 (= ?x407 ?x382)))
(let (($x406 (>= n 0)))
(=> $x406 $x370))))))
)
(check-sat)
