# Auto_Tractor

## Map_Provider
Nella cartella sono inserite la mappa 2D e la mappa 3D che vengono create nella repository Auto_Tractor.
Per la mappa 2D vengono generati due file: mymap2d.pgm e mymap2d.yaml. Il primo rappresenta un'immagine della mappa, mentre il secondo 
è utile per visualizzare la mappa su Rviz per simulazioni successive. Per la mappa 3D è presente un unico file map3d.bt 

## Robot_Laser
In src sono presenti due codici in Python: robot_laser.py e robot_vel.py. Grazie al primo si è in grado di visualizzare su terminale la distanza frontale e laterale del robot dagli ostacoli in tempo reale. Con il secondo si è imposta al trattore una velocità in una certa direzione e la distanza massima che il trattore può avere da un possibile ostacolo, oltre la quale si ferma. Su terminale viene visualizzata la distanza frontale dall'ostacolo.
Per rendere eseguibili i due codici si utilizza il seguente comando:

> chmod +x ./nomefile

Attraverso i file launch è possibile avviare i due codici con i comandi:

> roslaunch robot_laser robot_laser.launch

> roslaunch robot_laser robot_vel.launch
