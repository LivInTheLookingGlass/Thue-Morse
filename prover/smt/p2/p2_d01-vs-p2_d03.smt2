; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
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
 (forall ((n Int) )(let ((?x379 ((_ T2_03 0) n)))
 (let (($x380 (= ?x379 n)))
 (let ((?x381 ((_ T2_01 0) n)))
 (let (($x382 (= ?x381 n)))
 (let (($x416 (and $x382 $x380)))
 (let (($x387 (< n s)))
 (let (($x418 (>= n 0)))
 (let (($x420 (and $x418 $x387)))
 (=> $x420 $x416))))))))))
 )
(assert
 (let ((?x408 ((_ T2_01 0) s)))
 (= ?x408 1)))
(assert
 (let ((?x406 ((_ T2_03 0) s)))
 (= ?x406 1)))
(assert
 (forall ((n Int) )(let ((?x379 ((_ T2_03 0) n)))
(let ((?x381 ((_ T2_01 0) n)))
(let (($x467 (= ?x381 ?x379)))
(let (($x418 (>= n 0)))
(=> $x418 $x467))))))
)
(check-sat)
