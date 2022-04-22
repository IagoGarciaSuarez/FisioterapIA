;-------- Reglas crisp ---------
(defrule regla_crisp_esguince_1
	(inflamacion)
	(hematoma)
	(alt_tono_musc_adyacente)
	(inseg_apoyo)
	(bloqueo_pie)
	(sensibilidad)
=>
	(assert (esguince_lateral_tobillo)))

(defrule regla_crisp_esguince_2
	(esguince_lateral_tobillo)
	(sens_leve)
	(infl_leve)
	(hematoma) 
=>
	(assert (esg_lat_tob_g1)))

(defrule regla_crisp_esguince_3
	(esguince_lateral_tobillo)
	(sens_media)
	(infl_media)
	(hematoma_medio)
	(func_anormal)
=>
	(assert (esg_lat_tob_g2)))
	
(defrule regla_crisp_esguince_4
	(fract_maleolo)
=>
	(assert (esg_lat_tob_g3)))

(defrule regla_crisp_esguince_5
	(esguince_lateral_tobillo)
	(sens_sust)
	(infl_sust)
	(hematoma_sust)
	(fract_jones)
=>
	(assert (esg_lat_tob_g3)))

(defrule regla_crisp_esguince_6
	(tiene_diagnostico)
	(esg_lat_tob_g3)
=>
	(assert (rice_3))
	(assert (escayolar)))

(defrule regla_crisp_esguince_7
	(esg_lat_tob_g3)
	(tiene_diagnostico)
	(fract_jones)
=>
	(assert (terapia_mov_pie_apoyo)))

(defrule regla_crisp_esguince_8
	(esg_lat_tob_g3)
	(tiene_diagnostico)
	(fract_maleolo)
=>
	(assert (terapia_mov_articulacion)))

(defrule regla_crisp_esguince_9
	(or (and (not (tiene_diagnostico))
			(or (infl_media)
				(infl_sust)
				(hematoma_medio)
				(hematoma_sust))))
		(and (tiene_diagnostico)
			(or (infl_anormal)
				(hematoma_anormal)))
=>
	(assert (derivar_medico)))

(defrule regla_crisp_esguince_10
	(temp_alta)
	(infl_sust)
	(not (tiene_diagnostico))
=>
	(assert (pedir_radiografia))
	(assert (posible_fractura)))

(defrule regla_crisp_esguince_11
	(not (inflamacion))
	(not (tiene_diagnostico))
	(hematoma_normal)
=>
	(assert (reducir_hematoma))
	(assert (mitigar_dolor)))

(defrule regla_crisp_esguince_12
	(tratamiento_g1)
=>
	(assert (rice_1))
	(assert (terapia_mov_articulacion))
	(assert (terapia_manual)))

(defrule regla_crisp_esguince_13
	(tratamiento_g2)
=>	
	(assert (rice_2))
	(assert (terapia_mov_articulacion))
	(assert (terapia_manual)))

(defrule regla_crisp_esguince_14
	(tiene_diagnostico)
	(infl_normal)
=>
	(assert (crioterapia)))

(defrule regla_crisp_esguince_15
	(not (inflamacion))
	(not (hematoma))
	(not (temp_alta))
=>
	(assert (terapia_manual)))

(defrule regla_crisp_esguince_16
	(or (infl_leve)
		(infl_media)
		(infl_sust)
		(infl_anormal)
		(infl_normal))
=>
	(assert (inflamacion)))

(defrule regla_crisp_esguince_16
	(or (hematoma_leve)
		(hematoma_medio)
		(hematoma_sust)
		(hematoma_normal)
		(hematoma_anormal))
=>
	(assert (hematoma)))

(defrule regla_crisp_esguince_17
	(or (sens_leve)
		(sens_media)
		(sens_sust))
=>
	(assert (sensibilidad)))

(defrule regla_crisp_esguince_18
	(esg_lat_tob_g1)
=>
	(assert (esguince_lateral_tobillo))
	(assert (tratamiento_g1))
	(assert (desg_lig_leve)))

(defrule regla_crisp_esguince_19
	(esg_lat_tob_g2)
=>
	(assert (esguince_lateral_tobillo))
	(assert (tratamiento_g2))
	(assert (desg_lig_medio)))

(defrule regla_crisp_esguince_20
	(esg_lat_tob_g2)
=>
	(assert (esguince_lateral_tobillo))
	(assert (desg_lig_sust)))

;-----------Reglas con FC---------
; Esguince

(defrule regla_fc_esguince_1
	(declare (CF 0.9))
	(or (infl_sust)
		(hematoma_sust))
=>
	(assert (esguince_lateral_tobillo)))

(defrule regla_fc_esguince_2
	(declare (CF 0.75))
	(or (infl_media)
		(hematoma_medio))
=>
	(assert (esguince_lateral_tobillo)))

(defrule regla_fc_esguince_3
	(declare (CF 0.6))
	(hematoma_leve)
=>
	(assert  (esguince_lateral_tobillo)))

(defrule regla_fc_esguince_4
	(declare (CF 0.5))
	(infl_leve)
=>
	(assert (esguince_lateral_tobillo)))

; Esguince g1

(defrule regla_fc_esguince_5
	(declare (CF 0.7))
	(infl_leve)
=>
	(assert (esg_lat_tob_g1)))

(defrule regla_fc_esguince_6
	(declare (CF 0.6))
	(hematoma_leve)
=>
	(assert (esg_lat_tob_g1)))

(defrule regla_fc_esguince_7
	(declare (CF 0.3))
	(sens_leve)
=>
	(assert (esg_lat_tob_g1)))

; Esguince g2

(defrule regla_fc_esguince_8
	(declare (CF 0.6))
	(esguince_lateral_tobillo)
	(or (infl_media)
		(hematoma_medio))
=>
	(assert (esg_lat_tob_g2)))

(defrule regla_fc_esguince_9
	(declare (CF 0.5))
	(esguince_lateral_tobillo)
	(sens_media)
=>
	(assert (esg_lat_tob_g2)))

; Esguince g3

(defrule regla_fc_esguince_10
	(declare (CF 0.8))
	(esguince_lateral_tobillo)
	(or (infl_sust)
		(fract_jones))
=>
	(assert (esg_lat_tob_g3)))

(defrule regla_fc_esguince_11
	(declare (CF 0.9))
	(esguince_lateral_tobillo)
	(hematoma_sust)
=>
	(assert (esg_lat_tob_g3)))

(defrule regla_fc_esguince_12
	(declare (CF 0.7))
	(esguince_lateral_tobillo)
	(bloqueo_pie)
=>
	(assert (esg_lat_tob_g3)))


