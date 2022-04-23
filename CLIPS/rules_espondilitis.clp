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

(defrule rule_crisp_espond_4
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
    (tiene_diagnostico)
=>
    (assert (espondilitis_anquilosante)))

;---------- Reglas con FC ----------
(defrule rule_fc_espond_1
    (declare (CF 0.6))
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
    (hombre)
    (not (tiene_diagnostico))
=>
    (assert (espondilitis_anquilosante))
    (assert (pedir_radiografia)) CF 1)

(defrule rule_fc_espond_2
    (declare (CF 0.2))
    (dolor_dism_act)
    (rigidez_inact)
=>
    (assert (espondilitis_anquilosante)))

(defrule rule_fc_espond_3
    (declare (CF 0.4))
    (rigidez_inact)
    (dolor_dism_act)
    (dismin_curv_columna)
    (hombre)
=>
    (assert (espondilitis_anquilosante))
    (assert (pedir_radiografia)) CF 1)