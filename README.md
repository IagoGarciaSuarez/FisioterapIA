# FisioterapIA
FisioterapIA es un sistema basado en conocimiento experto dedicado al campo de la fisioterapia musculoesquelética en población adulta.

En el mismo repositorio se puede encontrar el archivo PDF relativo a su documentación, con nombre "FisioterapIA_documentacion.pdf".

## Instalación
Para poder utilizar el sistema, se necesitarán instalar las dependencias indicadas en "requirements.txt" si no lo estaban previamente (si el archivo está vacío, no es necesario seguir este paso):
```sh
pip install -r requirements.txt
```
Una vez instaladas, se podrá ejecutar el archivo "fisioterapia.py" con Python 3.9:
```sh
python fisioterapia.py
```

## Funcionamiento
El sistema permitirá al usuario indicar los hechos relativos al paciente, tanto los síntomas como los signos, y una vez hecho se creará un archivo "hechos.clp" y uno con nombre "run.clp" en el directorio "CLIPS/".

A continuación se podrá ejecutar Fuzzy CLIPS (localizado en "CLIPS/FuzzyClips.exe") y se deberá introducir los siguientes comandos en su interfaz:
```sh
(load run.clp)
(inicio)
```
Si todo ha ido correctamente, se habrá creado un archivo llamado "result.clp" en el mismo directorio.

Volviendo a FisioterapIA, habrá que indicar que el archivo se ha creado, y si es así se mostrará el resultado final.
