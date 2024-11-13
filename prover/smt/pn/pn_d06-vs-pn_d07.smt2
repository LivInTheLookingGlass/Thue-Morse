; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Int)
(define-funs-rec ( ( Tn_07 ((x!1 Int)) Int)
                   ( ilog2 ((x!1 Int) (x!2 Int)) Int)
                   ( xorn ((x!1 Int) (x!2 Int) (x!3 Int)) Int)
                   ( Tn_06 ((x!1 Int)) Int)
                   ( pn_06 ((x!1 Int)) Int))
                 ( (let ((a!1 (+ ((_ ilog2 0) ((_ xorn 0) x!1 (- x!1 1) s) s)
                                 ((_ Tn_07 0) (- x!1 1))
                                 1)))
                     (ite (< x!1 s) x!1 (mod a!1 s)))
                   (ite (<= x!1 1) 0 (+ 1 ((_ ilog2 0) (div x!1 x!2) x!2)))
                   (let ((a!1 (+ (mod (+ (mod x!1 x!3) (mod x!2 x!3)) x!3)
                                 (* x!3
                                    ((_ xorn 0) (div x!1 x!3) (div x!2 x!3) x!3)))))
                     (ite (= x!1 0) x!2 (ite (= x!2 0) x!1 a!1)))
                   ((_ pn_06 0) x!1)
                   (let ((a!1 (mod (- x!1 ((_ pn_06 0) (div x!1 s))) s)))
                     (ite (= x!1 0) 0 a!1))))
(assert
 (>= s 2))
(assert
 (forall ((n Int) )(let ((?x10622 ((_ Tn_07 0) n)))
(let ((?x62295 ((_ Tn_06 0) n)))
(let (($x11201 (= ?x62295 ?x10622)))
(let (($x15059 (>= n 0)))
(=> $x15059 $x11201))))))
)
(check-sat)
