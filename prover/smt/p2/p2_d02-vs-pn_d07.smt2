; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_07 ((x!1 Int)) Int)
                   ( ilog2 ((x!1 Int) (x!2 Int)) Int)
                   ( xorn ((x!1 Int) (x!2 Int) (x!3 Int)) Int)
                   ( T2_02 ((x!1 Int)) Int)
                   ( p2_02 ((x!1 Int)) Int))
                 ( (let ((a!1 (+ ((_ ilog2 0) ((_ xorn 0) x!1 (- x!1 1) s) s)
                                 ((_ Tn_07 0) (- x!1 1))
                                 1)))
                     (ite (< x!1 s) x!1 (mod a!1 s)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2 0) (div x!1 x!2) x!2)))
                   (let ((a!1 (+ (mod (+ (mod x!1 x!3) (mod x!2 x!3)) x!3)
                                 (* x!3
                                    ((_ xorn 0) (div x!1 x!3) (div x!2 x!3) x!3)))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   (let ((a!1 (/ (- 1.0 (^ (- 1) ((_ p2_02 0) x!1))) 2.0)))
                     (to_int a!1))
                   (ite (= x!1 0) 0 (+ ((_ p2_02 0) (div x!1 2)) (mod x!1 2)))))
(assert
 (forall ((n Int) )(let ((?x215 ((_ Tn_07 0) n)))
(let ((?x265 ((_ T2_02 0) n)))
(let (($x297 (= ?x265 ?x215)))
(let (($x251 (>= n 0)))
(=> $x251 $x297))))))
)
(check-sat)
