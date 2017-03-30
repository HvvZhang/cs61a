(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (cond
      ((null? items) nil)
      (else (cons (proc (car items)) 
                    (map proc 
                         (cdr items))))))

(define (cons-all first rests)
  (map (lambda (x) (append (list first) x)) 
         rests))

(define (zip pairs)
  'replace-this-line)

;; Problem 17
;; Returns a list of two-element lists
(define (reverse s)
  (define (helper s reversed)
      (cond
          ((null? s) reversed)
          (else (helper (cdr s) 
                (cons (car s) 
                      reversed)))))
  (helper s nil))

(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (helper s enumerated val)
    (cond
      ((null? s) enumerated)
      (else (helper (cdr s) 
                    (cons (list val (car s)) 
                          enumerated) 
                    (+ 1 val)))))
  (reverse (helper s nil 0)))
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
;; John Denero is a god because a problem like this
;; was OUT of my league before I started this course!
(define (list-change total denoms) 
  (define (helper total denoms current-sum-list)
      (cond 
          ((null? denoms) nil)
          ((zero? total) (list current-sum-list))
          ((> (car denoms) total) (helper total 
                                            (cdr denoms) 
                                            current-sum-list))
          (else (append
                    (helper (- total (car denoms)) 
                            denoms 
                            (cons (car denoms) 
                                  current-sum-list)) 
                    (helper total 
                            (cdr denoms) 
                            current-sum-list)))))
  (map reverse (helper total denoms nil)))
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
