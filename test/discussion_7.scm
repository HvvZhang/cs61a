; the discussions are getting quite challenging
; so I'll be posting all solutions from now onwards
; I still haven't figured out a good way to format 
; my scheme code so sorry about the mess

; discussion # 7 - fall '16

(define factorial
  (lambda (x) 
    (if (= 0 x)
        1
        (* x (factorial (- x 1))))))

(define (fib n)
  (if (< n 2)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

(define (concat a b)
	(cond
    	((null? a) b)
		((null? b) a)
    	(else 
        	(cons (car a) (concat (cdr a) b)))))

(define (replicate x n)
	(cond
    	((= n 0) ())
     	(else 
        	(cons x (replicate x (- n 1))))))

(define (uncompress s)
	(cond 
   		((null? s) ())
     	(else 
        	(concat 
            	(replicate (car (car s)) (car (cdr (car s)))) 
               	(uncompress (cdr s))))))


(define (map fn lst)
	(if (null? lst)
		nil
		(cons (fn (car lst)) (map fn (cdr lst)))))

(define (deep-apply fn nested-list)
  (cond 
  	((null? nested-list) ())
   	((number? nested-list) (fn nested-list))
   	((pair? (car nested-list)) 
    	(cons (deep-apply fn (car nested-list)) 
              (deep-apply fn (cdr nested-list))))
   	(else 
    	(cons (fn (car nested-list)) 
              (deep-apply fn (cdr nested-list))))))

(define (make-tree root branches) (cons root branches))
(define (root tree) (car tree))
(define (branches tree) (cdr tree))

(define (reduce fn lst initial)
	(cond 
     ((null? lst) initial)
     (else (reduce fn (cdr lst) (fn initial (car lst))))))

(define (tree-sum tree)
  	(if (null? (branches tree))
        (root tree)
        (+ (root tree) 
           (reduce + (map tree-sum (branches tree)) 0))))

; a simple tree to test my solutions on
(define x (make-tree 2 (list (make-tree 5 (list 
                                          (make-tree 6 ()))) 
                             (make-tree 3 ()))))

(define (path-product-tree t)
	(define (helper t previous-root)
      (if (null? (branches t))
          (make-tree (* (root t) previous-root) ())
          (make-tree (* previous-root (root t))
                     (map 
                     	(lambda (b) (helper b (* previous-root (root t)))) 
                      	(branches t)))))
  

 








