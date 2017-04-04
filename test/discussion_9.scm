(define (range-stream start end)
	(if (= start end)
		nil
		(cons-stream start (range-stream (+ 1 start) end)))
)

; it's really hard to format scheme on sublime
(define (slice stream start end)
	(define (slice-helper stream index)
		(cond
			((null? stream) nil)
			((= start index) (cons-stream (car stream) 
										  (slice-helper 
										  		(cdr-stream stream) 
										  		(+ index 1))))
			((= end index) nil)
		)
	)
	(slice-helper stream 0)
)

; note: I couldn't solve these two problems, unfortunately
; But I understand the logic behind them
; The stream needs base cases which are 1 for factorials
; and 0 and 1 for fibonacci
; Now each natural number is just multiplied 
; with whatever the previous factorial was
; to get the new factorial
; the logic behind fib is similar
; the logic is still similar to the recursive definitions

(define factorials (cons-stream 1 (zip-with * (naturals 1) factorials)))
(define fib (cons-stream 0 (cons-stream 1 (zip-with + fib (cdr-stream fib)))))
