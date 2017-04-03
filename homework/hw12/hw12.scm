(define (find s predicate)
	(if (null? s)
		#f
		(if (predicate (car s))
			(car s)
			(find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
	(if (null? s) 
		nil
		(cons-stream (* k (car s)) 
			(scale-stream 
				(cdr-stream s) 
				k)))
)

(define (a-in-stream s a)
	(if (null? s)
		#f
		(if (eq? (car s) a)
			#t
			(a-in-stream (cdr-stream s) a))))

(define (has-cycle s)
	(define (helper s prev)
		(if (null? s)
			#f
			(if (a-in-stream prev (car s))
				#t
				(helper 
					(cdr-stream s) 
					(cons-stream 
						(car s) 
						prev))))
	)

	(helper s nil)
)


(define (has-cycle-constant s)
	(define (helper fast slow)
		(cond 
			((or (null? fast) 
				 (null? (cdr-stream fast))) 
					#f)
			((or (eq? fast slow) 
				 (eq? (cdr-stream fast) slow)) 
					#t)
			(helper (cdr-stream (cdr-stream fast)) 
					(cdr-stream slow))
		)
	)
	(helper (cdr-stream s) s)
)
