(deftemplate inflamacion
	0 10
	(
		(leve (0 1) (1 1) (4 0))
		(media (2 0) (6 1) (8 0))
		(sust (7 0) (10 1))
	)
)
(deftemplate hematoma
	0 10
	(
		(leve (0 1) (1 1) (4 0))
		(medio (2 0) (6 1) (8 0))
		(sust (7 0) (10 1))
	)
)

(deftemplate importancia
	0 10
	(
		(muy_poca (0 1) (1 1) (3 0))
		(leve (1 0) (3 1) (5 0))
		(media (3 0) (5 1) (7 0))
		(importante (5 0) (7 1) (9 0))
		(urgente (7 0) (9 1) (10 1))
	)
)

(defrule r1
	(inflamacion leve)
	(hematoma leve)
=>
	(assert (importancia muy_poca)))

(defrule r2
	(inflamacion media)
	(hematoma leve)
=>
	(assert (importancia leve)))

(defrule r3
	(inflamacion sust)
	(hematoma leve)
=>
	(assert (importancia media)))

(defrule r4
	(inflamacion leve)
	(hematoma medio)
=>
	(assert (importancia leve)))

(defrule r5
	(inflamacion media)
	(hematoma medio)
=>
	(assert (importancia media)))

(defrule r6
	(inflamacion sust)
	(hematoma medio)
=>
	(assert (importancia importante)))

(defrule r7
	(inflamacion leve)
	(hematoma sust)
=>
	(assert (importancia media)))
	
(defrule r8
	(inflamacion media)
	(hematoma sust)
=>
	(assert (importancia importante)))
	
(defrule r9
	(inflamacion sust)
	(hematoma sust)
=>
	(assert (importancia urgente)))
