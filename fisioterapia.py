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
def main():
    print(INTRO)
    print('Bienvenid@ a FisioterapIA. En cualquier momento puede introducir \'q\' para salir del sistema.')
    while 1:
        print('----- DATOS DEL PACIENTE ------')
        try:
            paciente_name = input('Nombre del paciente\n> ')
            if paciente_name == 'q':
                return
        except EOFError:
            return
        while 1:
            try:
                paciente_sexo = input('Sexo del paciente (h/m)\n> ')
                if paciente_sexo == 'q':
                    return
                if paciente_sexo not in ['h', 'm']:
                    print('Opción no válida. Escriba \'h\' para hombre o \'m\' para mujer.')
                break
            except EOFError:
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
            except EOFError:
                return
            except ValueError:
                print('Es necesario indicar una edad válida.')
        while 1:
            try:
                tiene_diagnostico = input('Tiene diagnóstico médico de la lesión? (s/n)\n> ')
                if tiene_diagnostico == 'q':
                    return
                if tiene_diagnostico not in ['s', 'n']:
                    print('Opción no válida. Escriba \'s\' o \'n\'.')
                break
            except EOFError:
                return
    while 1:
        print('¿Cuál zona es la afectada?')
        try:
            zona_lesion = input('(1) - Tobillo\n(2) - Espalda\n> ')
            if zona_lesion == '1':
                print('Seleccionada la zona del tobillo.')
                rules_file = 'rules_esguince.clp'
            elif zona_lesion == '2':
                print('Seleccionada la zona de la espalda.')
                rules_file = 'rules_espondilitis.clp'
            elif zona_lesion == 'q':
                print('Saliendo del sistema.')
                return
            else:
                print('Opcion no valida. Escriba el numero correspondiente a la opcion.')
        except EOFError:
            return
        except Exception:
            print('Opcion no valida. Escriba el numero correspondiente a la opcion.')
    
    print(f'Paciente: {paciente_name.upper()}\nEdad: {paciente_edad}\n')
    if tiene_diagnostico == 's':
        print('Tiene diagnóstico: Sí')
    else:
        print('Tiene diagnóstico: No')
    if zona_lesion == '1':
        print('Zona de la lesión: Tobillo')
        esguince()
    else:
        print('Zona de la lesión: Espalda')

def esguince():
    print('-------- DATOS DE LA LESIÓN --------')
    while 1:
        try:
            inflamacion = input('Indique el nivel de inflamación del 1 al 10 (0 si no hay inflamación, 11 si tiene un tamaño anormal)')
            if inflamacion == 'q':
                return
            inflamacion = int(inflamacion)
            break
        except EOFError:
            return
        except ValueError:
            print('Es necesario indicar un número del 1 al 10 (0 si no hay inflamación).')
    while 1:
        try:
            hematoma = input('Indique la gravedad del hematoma del 1 al 10 (0 si no hay hematoma, 11 si tiene color o tamaño anormal)')
            if hematoma == 'q':
                return
            hematoma = int(hematoma)
            break
        except EOFError:
            return
        except ValueError:
            print('Es necesario indicar un número del 1 al 10 (0 si no hay hematoma).')

    while 1:
        try:
            sensibilidad = input('Indique el nivel de sensibilidad del 1 al 10 (0 si no hay sensibilidad)')
            if sensibilidad == 'q':
                return
            sensibilidad = int(sensibilidad)
            break
        except EOFError:
            return
        except ValueError:
            print('Es necesario indicar un número del 1 al 10 (0 si no hay sensibilidad).')
    while 1:
        try:
            alt_tono_musc_adyacente = input('Existe alteración del tono muscular adyacente? (s/n)\n> ')
            if alt_tono_musc_adyacente == 'q':
                return
            if alt_tono_musc_adyacente not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    while 1:
        try:
            temp_alta = input('La zona de la lesión tiene temperatura alta? (s/n)\n> ')
            if temp_alta == 'q':
                return
            if temp_alta not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    while 1:
        try:
            inseg_apoyo = input('El paciente tiene inseguridad al apoyar el pie? (s/n)\n> ')
            if inseg_apoyo == 'q':
                return
            if inseg_apoyo not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    while 1:
        try:
            bloqueo_pie = input('Hay bloqueo del pie? (s/n)\n> ')
            if bloqueo_pie == 'q':
                return
            if bloqueo_pie not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    while 1:
        try:
            fract_jones = input('Fractura de Jones? (s/n)\n> ')
            if fract_jones == 'q':
                return
            if fract_jones not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    while 1:
        try:
            fract_maleolo = input('Fractura del maléolo del peroné? (s/n)\n> ')
            if fract_maleolo == 'q':
                return
            if fract_maleolo not in ['s', 'n']:
                print('Opción no válida. Escriba \'s\' o \'n\'.')
            break
        except EOFError:
            return
    
    facts = '(deffacts hechos\n'

if __name__ == '__main__':
    main()
