(deftemplate inflamacion
	0 10
	(
		(leve (0 1) (1 1) (4 0))
		(media (3.5 0) (6 1) (7.5 0))
		(sust (8 0) (10 1))
	)
)
(deftemplate hematoma
	0 10
	(
		(leve (0 1) (1 1) (4 0))
		(medio (3.5 0) (6 1) (7.5 0))
		(sust (8 0) (10 1))
	)
)

(deftemplate esguince
	0 10
	(
		(g1 (0 1) (1 1) (3 0))
		(g1_2 (1 0) (3 1) (5 0))
		(g2 (3 0) (5 1) (7 0))
		(g2_3 (5 0) (7 1) (9 0))
		(g3 (7 0) (9 1) (10 1))
	)
)

(defrule r1
	(inflamacion leve)
	(hematoma leve)
=>
	(assert (esguince g1)))

(defrule r2
	(or (and (inflamacion leve)
			(hematoma medio))
		(and (inflamacion media)
			(hematoma medio)))
=>
	(assert (esguince g1_2)))

(defrule r3
	(inflamacion media)
	(hematoma medio)
=>
	(assert (esguince g2)))

(defrule r4
	(or (and (inflamacion media)
			(hematoma sust))
		(and (inflamacion sust)
			(hematoma medio)))
=>
	(assert (esguince g2_3)))

(defrule r5
	(inflamacion sust)
	(hematoma sust)
=>
	(assert (esguince g3)))
