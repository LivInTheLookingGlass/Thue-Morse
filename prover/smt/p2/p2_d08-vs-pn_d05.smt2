; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_05 ((x!1 Int)) Int)
                   ( undigitn_05 ((x!1 String)) Int)
                   ( indexn_05 ((x!1 String) (x!2 String)) Int)
                   ( ilog10_n_05 ((x!1 Int)) Int)
                   ( tn_05 ((x!1 Int)) String)
                   ( rotn_05 ((x!1 String) (x!2 Int)) String)
                   ( t1n_05 ((x!1 Int)) String)
                   ( digitn_05 ((x!1 Int)) String)
                   ( zerosn_05 ((x!1 Int)) String)
                   ( ilogn_n_05 ((x!1 Int)) Int)
                   ( T2_08 ((x!1 Int)) Int)
                   ( b2_08 ((x!1 Int)) Int))
                 ( (let ((a!1 (str.substr ((_ tn_05 0)
                                            (+ ((_ ilogn_n_05 0) x!1) 1))
                                          (* x!1 ((_ ilog10_n_05 0) s))
                                          ((_ ilog10_n_05 0) s))))
                     ((_ undigitn_05 0) a!1))
                   (let ((a!1 ((_ undigitn_05 0)
                                (str.substr x!1 1 (- (str.len x!1) 1)))))
                   (let ((a!2 (+ (* 10
                                    ((_ indexn_05 0)
                                      (str.substr x!1 0 1)
                                      "0123456789"))
                                 a!1)))
                     (ite (= (str.len x!1) 1)
                          ((_ indexn_05 0) x!1 "0123456789")
                          a!2)))
                   (let ((a!1 ((_ indexn_05 0)
                                x!1
                                (str.substr x!2
                                            (str.len x!1)
                                            (- (str.len x!2) (str.len x!1))))))
                     (ite (= x!1 (str.substr x!2 0 (str.len x!1))) 0 (+ 1 a!1)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog10_n_05 0) (div x!1 10))))
                   (let ((a!1 (div (str.len ((_ tn_05 0) (- x!1 1))) 2)))
                   (let ((a!2 (str.++ ((_ tn_05 0) (- x!1 1))
                                      ((_ rotn_05 0)
                                        ((_ tn_05 0) (- x!1 1))
                                        a!1))))
                     (ite (= x!1 0)
                          ((_ digitn_05 0) 0)
                          (ite (= x!1 1) ((_ t1n_05 0) 0) a!2))))
                   (str.++ (str.substr x!1 x!2 (- (str.len x!1) x!2))
                           (str.substr x!1 0 x!2))
                   (ite (= x!1 s)
                        ""
                        (str.++ ((_ digitn_05 0) x!1) ((_ t1n_05 0) (+ x!1 1))))
                   (let ((a!1 (str.++ ((_ zerosn_05 0)
                                        (- ((_ ilog10_n_05 0) s) 1))
                                      (str.substr "0123456789" (mod x!1 10) 1)))
                         (a!2 (str.++ (str.substr ((_ digitn_05 0) (div x!1 10))
                                                  1
                                                  (- ((_ ilog10_n_05 0) s) 1))
                                      (str.substr ((_ digitn_05 0) (mod x!1 10))
                                                  (- ((_ ilog10_n_05 0) s) 1)
                                                  1))))
                     (ite (< x!1 10) a!1 a!2))
                   (ite (= x!1 0) "" (str.++ "0" ((_ zerosn_05 0) (- x!1 1))))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilogn_n_05 0) (div x!1 s))))
                   (mod ((_ b2_08 0) x!1) 2)
                   (let ((a!1 (- ((_ b2_08 0) (+ (div x!1 2) (mod x!1 2)))
                                 ((_ b2_08 0) (div x!1 2)))))
                     (ite (< x!1 2) x!1 a!1))))
(assert
 (forall ((n Int) )(let ((?x383 ((_ Tn_05 0) n)))
(let ((?x382 ((_ T2_08 0) n)))
(let (($x406 (= ?x382 ?x383)))
(let (($x381 (>= n 0)))
(=> $x381 $x406))))))
)
(check-sat)
