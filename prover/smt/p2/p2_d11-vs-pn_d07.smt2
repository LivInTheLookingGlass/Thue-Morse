; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_07 ((x!1 Int)) Int)
                   ( ilog2 ((x!1 Int) (x!2 Int)) Int)
                   ( xorn ((x!1 Int) (x!2 Int) (x!3 Int)) Int)
                   ( T2_11 ((x!1 Int)) Int)
                   ( p2_11 ((x!1 Int)) Int)
                   ( ilog2_2_11 ((x!1 Int)) Int))
                 ( (let ((a!1 (+ ((_ ilog2 0) ((_ xorn 0) x!1 (- x!1 1) s) s)
                                 ((_ Tn_07 0) (- x!1 1))
                                 1)))
                     (ite (< x!1 s) x!1 (mod a!1 s)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2 0) (div x!1 x!2) x!2)))
                   (let ((a!1 (+ (mod (+ (mod x!1 x!3) (mod x!2 x!3)) x!3)
                                 (* x!3
                                    ((_ xorn 0) (div x!1 x!3) (div x!2 x!3) x!3)))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   (+ (- 1 ((_ p2_11 0) (+ x!1 1))) ((_ p2_11 0) x!1))
                   (let ((a!1 (* (mod ((_ ilog2_2_11 0) (+ x!1 1)) 2)
                                 (mod x!1 2))))
                     (+ (div x!1 2) a!1))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2_2_11 0) (div x!1 2))))))
(assert
 (forall ((n Int) )(let ((?x426 ((_ Tn_07 0) n)))
(let ((?x418 ((_ T2_11 0) n)))
(let (($x419 (= ?x418 ?x426)))
(let (($x417 (>= n 0)))
(=> $x417 $x419))))))
)
(check-sat)
