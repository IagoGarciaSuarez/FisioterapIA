;--------- Reglas crisp ---------

(defrule rule_crisp_espond_1
    (espalda_muy_recta)
=>
    (assert (dismin_curv_columna)))

(defrule rule_crisp_espond_2
    (espondilitis_anquilosante)
    (dolor_agudo)
    (rigidez_muy_alta)
=>
    (assert (posible_fract_vertebras))
    (assert (pedir_resonancia)))

(defrule rule_crisp_espond_3
    (espondilitis_anquilosante)
=>
    (assert (terapia_manual))
    (assert (estiramiento_musc_post))
    (assert (termoterapia))
    (assert (ejer_terapeutico)))

;---------- Reglas con FC ----------
(defrule rule_fc_espond_1
    (declare (CF 0.9))
    (acort_musc_glutea)
    (acort_musc_isquiotibial)
    (dismin_curv_columna)
    (rigidez_espalda_baja)
    (rigidez_caderas)
    (rigidez_inact)
    (dolor_irrad_piernas)
    (sens_corr_electrica)
    (dolor_lumbar_inesp)
    (dolor_inc_inact)
    (dolor_dism_act)
    (dolor_caderas)
=>
    (assert (espondilitis_anquilosante)))

(defrule rule_fc_espond_2
    (declare (CF 0.4))
    (or (rigidez_inact)
        (rigidez_muy_alta))
=>
    (assert (espondilitis_anquilosante)))


(defrule rule_fc_espond_3
    (declare (CF 0.3))
    (rigidez_espalda_baja)
=>
    (assert (espondilitis_anquilosante)))

