; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( T2_11 ((x!1 Int)) Int)
                   ( p2_11 ((x!1 Int)) Int)
                   ( ilog2_2_11 ((x!1 Int)) Int)
                   ( T2_03 ((x!1 Int)) Int)
                   ( t2_03 ((x!1 Int)) String)
                   ( invert2_03 ((x!1 String)) String)
                   ( ilog2_2_03 ((x!1 Int)) Int))
                 ( (+ (- 1 ((_ p2_11 0) (+ x!1 1))) ((_ p2_11 0) x!1))
                   (let ((a!1 (* (mod ((_ ilog2_2_11 0) (+ x!1 1)) 2)
                                 (mod x!1 2))))
                     (+ (div x!1 2) a!1))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_11 0) (div x!1 2))))
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
 (forall ((n Int) )(let ((?x406 ((_ T2_11 0) n)))
 (let (($x407 (= ?x406 n)))
 (let ((?x408 ((_ T2_03 0) n)))
 (let (($x409 (= ?x408 n)))
 (let (($x410 (and $x409 $x407)))
 (let (($x387 (< n s)))
 (let (($x411 (>= n 0)))
 (let (($x412 (and $x411 $x387)))
 (=> $x412 $x410))))))))))
 )
(assert
 (forall ((n Int) )(let ((?x406 ((_ T2_11 0) n)))
(let ((?x408 ((_ T2_03 0) n)))
(let (($x383 (= ?x408 ?x406)))
(let (($x411 (>= n 0)))
(=> $x411 $x383))))))
)
(check-sat)