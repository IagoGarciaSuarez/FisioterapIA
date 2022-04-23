import os

INTRO = '''
  ______ _     _       _                      _____          
 |  ____(_)   (_)     | |                    |_   _|   /\\    
 | |__   _ ___ _  ___ | |_ ___ _ __ __ _ _ __  | |    /  \\   
 |  __| | / __| |/ _ \\| __/ _ \\ '__/ _` | '_ \\ | |   / /\\ \\  
 | |    | \\__ \\ | (_) | ||  __/ | | (_| | |_) || |_ / ____ \\ 
 |_|    |_|___/_|\\___/ \\__\\___|_|  \\__,_| .__/_____/_/    \\_\\
                                        | |                  
                                        |_|                  
'''
RUN_TOBILLO = '''
(deffunction inicio()
    (undeffacts *)
    (undefrule *)
    (load rules_esguince.clp)
    (load facts.clp)
    (printout t "Reglas y hechos cargados. Analizando el caso..." crlf)
    (reset)
    (run)
    (save-facts result.clp))
'''
RUN_ESPALDA = '''
(deffunction inicio()
    (undeffacts *)
    (undefrule *)
    (load rules_espondilitis.clp)
    (load facts.clp)
    (printout t "Reglas y hechos cargados. Analizando el caso..." crlf)
    (reset)
    (run)
    (save-facts result.clp))
'''
FACT_SIGNIF = {
    '(crioterapia)': 'Aplicar crioterapia.',
    '(derivar_medico)': 'Derivar al médico.',
    '(desg_lig_leve)': 'Hay un desgarro leve del ligamento de la articulación.',
    '(desg_lig_medio)': 'Hay un desgarro medio del ligamento de la articulación.',
    '(desg_lig_sust)': 'Hay un desgarro sustancial del ligamento de la articulación.',
    '(ejer_terapeutico)': 'Realizar ejercicios terapéuticos orientados a la zona de la lesión.',
    '(escayolar)': 'Escayolar la zona.',
    '(esg_lat_tob_g1)': 'Esguince lateral de tobillo de grado 1.',
    '(esg_lat_tob_g2)': 'Esguince lateral de tobillo de grado 2.',
    '(esg_lat_tob_g3)': 'Esguince lateral de tobillo de grado 3.',
    '(esguince_lateral_tobillo)': 'Esguince lateral de tobillo.',
    '(espondilitis_anquilosante)': 'Espondilitis anquilosante.',
    '(estiramiento_musc_post)': 'Efectuar estiramientos de la musculatura posterior.',
    '(mitigar_dolor)': 'Aplicar terapia orientada a la mitigación del dolor.',
    '(pedir_radiografia)': 'Pedir una radiografía de la zona',
    '(pedir_resonancia)': 'Pedir una resonancia',
    '(posible_fractura)': 'Es posible que el paciente tenga una fractura en la zona.',
    '(posible_fract_vertebras)': 'Es posible que el paciente tenga una o múltiples fracturas en las vértebras.',
    '(reducir_hematoma)': 'Aplicar una terapia orientada a la reducción del hematoma.',
    '(rice_1)': 'Aplicar tratamiento RICE durante 24 a 48 horas.',
    '(rice_2)': 'Aplicar tratamiento RICE durante 3 a 5 días.',
    '(rice_3)': 'Aplicar tratamiento RICE durante 2 a 4 semanas.',
    '(terapia_mov_pie_apoyo)': 'Aplicar una terapia de movilización y apoyo del pie.',
    '(terapia_mov_articulacion)': 'Aplicar una terapia de movilización de la articulación',
    '(terapia_manual)': 'Aplicar terapia manual.',
    '(termoterapia)': 'Aplicar termoterapia.',
}
deffacts = ['(deffacts hechos']
def main():
    print(INTRO)
    print('Bienvenid@ a FisioterapIA. En cualquier momento puede introducir \'q\' para salir del sistema.')
    
    print('----- DATOS DEL PACIENTE ------')
    try:
        paciente_name = input('Nombre del paciente\n> ')
        if paciente_name == 'q':
            return
    except KeyboardInterrupt:
        return
    while 1:
        try:
            paciente_sexo = input('Sexo del paciente (h/m)\n> ')
            if paciente_sexo == 'q':
                return
            if paciente_sexo == 'h':
                deffacts.append('(hombre)')
                break
            elif paciente_sexo == 'm':
                break
            else:
                print('Opción no válida. Escriba \'h\' para hombre o \'m\' para mujer.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            paciente_edad = input('Edad del paciente\n> ')
            if paciente_edad == 'q':
                return
            paciente_edad = int(paciente_edad)
            if paciente_edad < 14 or paciente_edad > 60:
                print(
                    'Este sistema ha sido diseñado para pacientes de entre 14 y 60 años.' + \
                    ' Es recomendable leer la documentación antes de su uso.')
            break
        except KeyboardInterrupt:
            return
        except ValueError:
            print('Es necesario indicar una edad válida.')
    while 1:
        try:
            tiene_diagnostico = input('Tiene diagnóstico médico de la lesión? (s/n)\n> ')
            if tiene_diagnostico == 'q':
                return
            if tiene_diagnostico == 's':
                deffacts.append('(tiene_diagnostico)')
                break
            elif tiene_diagnostico == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        print('¿Cuál zona es la afectada?')
        try:
            zona_lesion = input('(1) - Tobillo\n(2) - Espalda\n> ')
            if zona_lesion == '1':
                print('Seleccionada la zona del tobillo.')
                with open('CLIPS/run.clp', 'w+') as run_file:
                    run_file.write(RUN_TOBILLO)
                break
            elif zona_lesion == '2':
                print('Seleccionada la zona de la espalda.')
                with open('CLIPS/run.clp', 'w+') as run_file:
                    run_file.write(RUN_ESPALDA)
                break
            elif zona_lesion == 'q':
                print('Saliendo del sistema.')
                return
            else:
                print('Opcion no valida. Escriba el numero correspondiente a la opcion.')
        except KeyboardInterrupt:
            return
        except Exception:
            print('Opcion no valida. Escriba el numero correspondiente a la opcion.')
    
    print('\n\n---------------------------\n')
    print(f'Paciente: {paciente_name.upper()}\nEdad: {paciente_edad}\n')
    if tiene_diagnostico == 's':
        print('Tiene diagnóstico: Sí')
    else:
        print('Tiene diagnóstico: No')
    if zona_lesion == '1':
        print('Zona de la lesión: Tobillo')
        print('\n\n---------------------------\n')
        esguince()
    elif zona_lesion == '2':
        print('Zona de la lesión: Espalda')
        print('\n\n---------------------------\n')
        espondilitis()    
    deffacts.append(')')
    with open('CLIPS/facts.clp', 'w+') as facts_file:
        facts_file.write('\n'.join(deffacts))
    print('Se han guardado correctamente los hechos. Abra Fuzzy CLIPS e introduzca los comandos \'(load run.clp)\' y a continuación \'(inicio)\'')
    while 1:
        try:
            if input('Escriba \'s\' cuando se haya completado el análisis.\n> ') == 's':
                results()
                break
        except FileNotFoundError:
            print('Error al cargar el archivo. Primero debe seguir los pasos en Fuzzy CLIPS.')

def results():
    with open('CLIPS/result.clp', 'r') as res_f:
        facts = res_f.readlines()
    os.remove('CLIPS/result.clp')
    print('\n\n++++++++++++++ RESULTADOS +++++++++++++++\n')
    print('Dados los datos del paciente y los síntomas y signos de la lesión, se han llegado a las siguientes conclusiones:\n\n')
    for fact in facts:
        fact = fact.split(' CF ')
        if fact[0] in FACT_SIGNIF and float(fact[1]) > 0.0:
            print(f'CERTEZA: {float(fact[1])*100}%')
            print(FACT_SIGNIF[fact[0]], '\n')
            
def esguince():
    print('-------- DATOS DE LA LESIÓN --------')
    while 1:
        try:
            inflamacion = input('Indique si la inflamación es (a)normal, (l)eve, (m)edia o (s)sustancial (\'n\' si no hay inflamación)\n> ')
            if inflamacion == 'q':
                return
            elif inflamacion == 'a':
                deffacts.append('(infl_anormal)')
                break
            elif inflamacion == 'l':
                deffacts.append('(infl_leve)')
                break
            elif inflamacion == 'm':
                deffacts.append('(infl_media)')
                break
            elif inflamacion == 's':
                deffacts.append('(infl_sust)')
                break
            elif inflamacion == 'n':
                break
            else:
                print('Opción no válida. Escriba \'a\', \'l\', \'m\' o \'s\' (\'n\' si no hay inflamación).')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            hematoma = input('Indique si el hematoma es (a)normal, (l)eve, (m)edio o (s)sustancial (\'n\' si no hay hematoma)\n> ')
            if hematoma == 'q':
                return
            elif hematoma == 'a':
                deffacts.append('(hematoma_anormal)')
                break
            elif hematoma == 'l':
                deffacts.append('(hematoma_leve)')
                break
            elif hematoma == 'm':
                deffacts.append('(hematoma_media)')
                break
            elif hematoma == 's':
                deffacts.append('(hematoma_sust)')
                break
            elif hematoma == 'n':
                break
            else:
                print('Opción no válida. Escriba \'a\', \'l\', \'m\' o \'s\' (\'n\' si no hay hematoma).')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            sensibilidad = input('Indique si la sensibilidad es (l)eve, (m)edia o (s)sustancial (\'n\' si no hay sensibilidad)\n> ')
            if sensibilidad == 'q':
                return
            elif sensibilidad == 'l':
                deffacts.append('(sens_leve)')
                break
            elif sensibilidad == 'm':
                deffacts.append('(sens_media)')
                break
            elif sensibilidad == 's':
                deffacts.append('(sens_sust)')
                break
            elif sensibilidad == 'n':
                break
            else:
                print('Opción no válida. Escriba \'l\', \'m\' o \'s\'. (\'n\' si no hay sensibilidad)')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            alt_tono_musc_adyacente = input('Existe alteración del tono muscular adyacente? (s/n)\n> ')
            if alt_tono_musc_adyacente == 'q':
                return
            if alt_tono_musc_adyacente == 's':
                deffacts.append('(alt_tono_musc_adyacente)')
                break
            if alt_tono_musc_adyacente == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            temp_alta = input('La zona de la lesión tiene temperatura alta? (s/n)\n> ')
            if temp_alta == 'q':
                return
            if temp_alta == 's':
                deffacts.append('(temp_alta)')
                break
            elif temp_alta == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            inseg_apoyo = input('El paciente tiene inseguridad al apoyar el pie? (s/n)\n> ')
            if inseg_apoyo == 'q':
                return
            elif inseg_apoyo == 's':
                deffacts.append('(inseg_apoyo)')
                break
            elif inseg_apoyo == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            func_anormal = input('El tobillo lesionado muestra un funcionamiento anormal?(s/n)\n> ')
            if func_anormal == 'q':
                return
            elif func_anormal == 's':
                deffacts.append('(func_anormal)')
                break
            elif func_anormal == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            bloqueo_pie = input('Hay bloqueo del pie? (s/n)\n> ')
            if bloqueo_pie == 'q':
                return
            elif bloqueo_pie == 's':
                deffacts.append('(bloqueo_pie)')
                break
            elif bloqueo_pie == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            fract_jones = input('Fractura de Jones? (s/n)\n> ')
            if fract_jones == 'q':
                return
            elif fract_jones == 's':
                deffacts.append('(fract_jones)')
                break
            elif fract_jones == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            fract_maleolo = input('Fractura del maléolo del peroné? (s/n)\n> ')
            if fract_maleolo == 'q':
                return
            elif fract_maleolo == 's':
                deffacts.append('(fract_maleolo)')
                break
            elif fract_maleolo == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    
def espondilitis():
    print('-------- DATOS DE LA LESIÓN --------')
    while 1:
        try:
            espalda_muy_recta = input('Tiene la espalda más recta de lo normal? (s/n)\n> ')
            if espalda_muy_recta == 'q':
                return
            if espalda_muy_recta == 's':
                deffacts.append('(espalda_muy_recta)')
                break
            elif espalda_muy_recta == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_agudo = input('Tiene dolor agudo? (s/n)\n> ')
            if dolor_agudo == 'q':
                return
            if dolor_agudo == 's':
                deffacts.append('(dolor_agudo)')
                break
            elif dolor_agudo == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            rigidez_muy_alta = input('Rigidez muy alta? (s/n)\n> ')
            if rigidez_muy_alta == 'q':
                return
            if rigidez_muy_alta == 's':
                deffacts.append('(rigidez_muy_alta)')
                break
            elif rigidez_muy_alta == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            rigidez_espalda_baja = input('Rigidez en espalda baja? (s/n)\n> ')
            if rigidez_espalda_baja == 'q':
                return
            if rigidez_espalda_baja == 's':
                deffacts.append('(rigidez_espalda_baja)')
                break
            elif rigidez_espalda_baja == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            rigidez_caderas = input('Tiene rigidez en las caderas? (s/n)\n> ')
            if rigidez_caderas == 'q':
                return
            if rigidez_caderas == 's':
                deffacts.append('(tiene_diagnostico)')
                break
            elif rigidez_caderas == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            rigidez_inact = input('Aumenta la rigidez con la inactividad? (s/n)\n> ')
            if rigidez_inact == 'q':
                return
            if rigidez_inact == 's':
                deffacts.append('(rigidez_inact)')
                break
            elif rigidez_inact == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_irrad_piernas = input('Se irradia el dolor a las piernas? (s/n)\n> ')
            if dolor_irrad_piernas == 'q':
                return
            if dolor_irrad_piernas == 's':
                deffacts.append('(dolor_irrad_piernas)')
                break
            elif dolor_irrad_piernas == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            sens_corr_electrica = input('El paciente siente el dolor como una corirente eléctrica? (s/n)\n> ')
            if sens_corr_electrica == 'q':
                return
            if sens_corr_electrica == 's':
                deffacts.append('(sens_corr_electrica)')
                break
            elif sens_corr_electrica == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_lumbar_inesp = input('Dolor lumbar inespecífico? (s/n)\n> ')
            if dolor_lumbar_inesp == 'q':
                return
            if dolor_lumbar_inesp == 's':
                deffacts.append('(dolor_lumbar_inesp)')
                break
            elif dolor_lumbar_inesp == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_inc_inact = input('El dolor incrementa con la inactividad? (s/n)\n> ')
            if dolor_inc_inact == 'q':
                return
            if dolor_inc_inact == 's':
                deffacts.append('(dolor_inc_inact)')
                break
            elif dolor_inc_inact == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_dism_act = input('El dolor disminuye con la actividad? (s/n)\n> ')
            if dolor_dism_act == 'q':
                return
            if dolor_dism_act == 's':
                deffacts.append('(dolor_dism_act)')
                break
            elif dolor_dism_act == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            dolor_caderas = input('Dolor en las caderas? (s/n)\n> ')
            if dolor_caderas == 'q':
                return
            if dolor_caderas == 's':
                deffacts.append('(dolor_dism_act)')
                break
            elif dolor_caderas == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            acort_musc_glutea = input('Existe un acortamiento de la musculatura glútea? (s/n)\n> ')
            if acort_musc_glutea == 'q':
                return
            if acort_musc_glutea == 's':
                deffacts.append('(acort_musc_glutea)')
                break
            elif acort_musc_glutea == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    while 1:
        try:
            acort_musc_isquiotibial = input('Existe un acortamiento de la musculatura isquiotibial? (s/n)\n> ')
            if acort_musc_isquiotibial == 'q':
                return
            if acort_musc_isquiotibial == 's':
                deffacts.append('(acort_musc_isquiotibial)')
                break
            elif acort_musc_isquiotibial == 'n':
                break
            else:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
        except KeyboardInterrupt:
            return
    
if __name__ == '__main__':
    main()
