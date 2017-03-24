(define (how-many-dots s)
  (cond
  	((null? s) 0)
  	((and (number? (car s)) (number? (cdr s))) 1)
  	((and (pair? (car s)) (number? (cdr s))) (+ 1 (how-many-dots (car s))))
   	((pair? (car s)) (+ (how-many-dots (car s)) (how-many-dots (cdr s))))
   	(else (how-many-dots (cdr s)))
  )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7)))))))
; expect 0