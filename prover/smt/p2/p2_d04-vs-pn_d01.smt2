; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_01 ((x!1 Int)) Int)
                   ( pn_01 ((x!1 Int)) Int)
                   ( T2_04 ((x!1 Int)) Int)
                   ( t2_04 ((x!1 Int)) String)
                   ( sub2_04 ((x!1 String) (x!2 String)) String)
                   ( ilog2_2_04 ((x!1 Int)) Int))
                 ( (mod ((_ pn_01 0) x!1) s)
                   (ite (= x!1 0) 0 (+ ((_ pn_01 0) (div x!1 s)) x!1))
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
 (forall ((n Int) )(let ((?x370 ((_ Tn_01 0) n)))
(let ((?x358 ((_ T2_04 0) n)))
(let (($x356 (= ?x358 ?x370)))
(let (($x379 (>= n 0)))
(=> $x379 $x356))))))
)
(check-sat)
