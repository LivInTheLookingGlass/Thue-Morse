; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_07 ((x!1 Int)) Int)
                   ( ilog2 ((x!1 Int) (x!2 Int)) Int)
                   ( xorn ((x!1 Int) (x!2 Int) (x!3 Int)) Int)
                   ( T2_01 ((x!1 Int)) Int)
                   ( p2_01 ((x!1 Int)) Int))
                 ( (let ((a!1 (+ ((_ ilog2 0) ((_ xorn 0) x!1 (- x!1 1) s) s)
                                 ((_ Tn_07 0) (- x!1 1))
                                 1)))
                     (ite (< x!1 s) x!1 (mod a!1 s)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2 0) (div x!1 x!2) x!2)))
                   (let ((a!1 (+ (mod (+ (mod x!1 x!3) (mod x!2 x!3)) x!3)
                                 (* x!3
                                    ((_ xorn 0) (div x!1 x!3) (div x!2 x!3) x!3)))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   (mod ((_ p2_01 0) x!1) 2)
                   (ite (= x!1 0) 0 (+ ((_ p2_01 0) (div x!1 2)) x!1))))
(assert
 (forall ((n Int) )(let ((?x5310 ((_ Tn_07 0) n)))
 (let (($x2488 (= ?x5310 n)))
 (let ((?x5370 ((_ T2_01 0) n)))
 (let (($x3107 (= ?x5370 n)))
 (let (($x1401 (and $x3107 $x2488)))
 (let (($x387 (< n s)))
 (let (($x1929 (>= n 0)))
 (let (($x1618 (and $x1929 $x387)))
 (=> $x1618 $x1401))))))))))
 )
(assert
 (let ((?x5396 ((_ T2_01 0) s)))
 (= ?x5396 1)))
(assert
 (let ((?x810 ((_ Tn_07 0) s)))
 (= ?x810 1)))
(assert
 (forall ((n Int) )(let ((?x5310 ((_ Tn_07 0) n)))
(let ((?x5370 ((_ T2_01 0) n)))
(let (($x711 (= ?x5370 ?x5310)))
(let (($x1929 (>= n 0)))
(=> $x1929 $x711))))))
)
(check-sat)