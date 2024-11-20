import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada y salida difusas
vol_trafico = ctrl.Antecedent(np.arange(0, 301, 1), 'vol_trafico')
cond_climaticas = ctrl.Antecedent(np.arange(0, 51, 1), 'cond_climaticas')
h_del_dia = ctrl.Antecedent(np.arange(6, 21, 1), 'h_del_dia') #############FALTA
tiemp_semaforo = ctrl.Consequent(np.arange(1,61,1), 'tiemp_semaforo') 

# Definir las funciones de membresía para las variables de entrada y salida
vol_trafico['bajo'] = fuzz.trapmf(vol_trafico.universe, [0,0,0,100])
vol_trafico['medio'] = fuzz.trimf(vol_trafico.universe, [50,150,200])
vol_trafico['alto'] = fuzz.trapmf(vol_trafico.universe, [150,300,300,300])

cond_climaticas['ligera'] = fuzz.trapmf(cond_climaticas.universe,[0,0,0,5])
cond_climaticas['normal'] = fuzz.trimf(cond_climaticas.universe,[0,10,20])
cond_climaticas['fuerte'] = fuzz.trapmf(cond_climaticas.universe,[10,50,50,50])

h_del_dia['temprano'] = fuzz.trapmf(h_del_dia.universe, [6,6,6,8])
h_del_dia['pico1'] = fuzz.trimf(h_del_dia.universe, [7.5,8.25,9])
h_del_dia['pico2'] = fuzz.trimf(h_del_dia.universe, [17,18,19])
h_del_dia['regular'] = fuzz.trimf(h_del_dia.universe, [8.67,13,17.25])
h_del_dia['tarde/noche'] = fuzz.trapmf(h_del_dia.universe, [18,20,20,20])

tiemp_semaforo['corto'] = fuzz.trapmf(tiemp_semaforo.universe,[1,1,1,25])
tiemp_semaforo['medio'] = fuzz.trimf(tiemp_semaforo.universe,[20,33,45])
tiemp_semaforo['largo'] = fuzz.trapmf(tiemp_semaforo.universe,[40,60,60,60])

# Definir las reglas difusas
regla1 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['ligera'] & h_del_dia['temprano'], tiemp_semaforo['corto'])
regla2 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['ligera'] & h_del_dia['pico1'], tiemp_semaforo['corto'])
regla3 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['ligera'] & h_del_dia['pico2'], tiemp_semaforo['corto'])
regla4 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['ligera'] & h_del_dia['regular'], tiemp_semaforo['corto'])
regla5 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['ligera'] & h_del_dia['tarde/noche'], tiemp_semaforo['corto'])

regla6 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['normal'] & h_del_dia['temprano'], tiemp_semaforo['corto'])
regla7 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['normal'] & h_del_dia['pico1'], tiemp_semaforo['medio'])
regla8 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['normal'] & h_del_dia['pico2'], tiemp_semaforo['medio'])
regla9 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['normal'] & h_del_dia['regular'], tiemp_semaforo['corto'])
regla10 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['normal'] & h_del_dia['tarde/noche'], tiemp_semaforo['corto'])

regla11 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['fuerte'] & h_del_dia['temprano'], tiemp_semaforo['medio'])
regla12 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['fuerte'] & h_del_dia['pico1'], tiemp_semaforo['medio'])
regla13 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['fuerte'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla14 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['fuerte'] & h_del_dia['regular'], tiemp_semaforo['medio'])
regla15 = ctrl.Rule(vol_trafico['bajo'] & cond_climaticas['fuerte'] & h_del_dia['tarde/noche'], tiemp_semaforo['medio'])

regla16 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['ligera'] & h_del_dia['temprano'], tiemp_semaforo['medio'])
regla17 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['ligera'] & h_del_dia['pico1'], tiemp_semaforo['medio'])
regla18 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['ligera'] & h_del_dia['pico2'], tiemp_semaforo['medio'])
regla19 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['ligera'] & h_del_dia['regular'], tiemp_semaforo['corto'])
regla20 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['ligera'] & h_del_dia['tarde/noche'], tiemp_semaforo['corto'])

regla21 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['normal'] & h_del_dia['temprano'], tiemp_semaforo['medio'])
regla22 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['normal'] & h_del_dia['pico1'], tiemp_semaforo['medio'])
regla23 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['normal'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla24 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['normal'] & h_del_dia['regular'], tiemp_semaforo['medio'])
regla25 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['normal'] & h_del_dia['tarde/noche'], tiemp_semaforo['medio'])

regla26 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['fuerte'] & h_del_dia['temprano'], tiemp_semaforo['medio'])
regla27 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['fuerte'] & h_del_dia['pico1'], tiemp_semaforo['largo'])
regla28 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['fuerte'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla29 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['fuerte'] & h_del_dia['regular'], tiemp_semaforo['medio'])
regla30 = ctrl.Rule(vol_trafico['medio'] & cond_climaticas['fuerte'] & h_del_dia['tarde/noche'], tiemp_semaforo['medio'])

regla31 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['ligera'] & h_del_dia['temprano'], tiemp_semaforo['largo'])
regla32 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['ligera'] & h_del_dia['pico1'], tiemp_semaforo['largo'])
regla33 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['ligera'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla34 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['ligera'] & h_del_dia['regular'], tiemp_semaforo['medio'])
regla35 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['ligera'] & h_del_dia['tarde/noche'], tiemp_semaforo['medio'])

regla36 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['normal'] & h_del_dia['temprano'], tiemp_semaforo['largo'])
regla37 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['normal'] & h_del_dia['pico1'], tiemp_semaforo['largo'])
regla38 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['normal'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla39 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['normal'] & h_del_dia['regular'], tiemp_semaforo['medio'])
regla40 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['normal'] & h_del_dia['tarde/noche'], tiemp_semaforo['medio'])

regla41 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['fuerte'] & h_del_dia['temprano'], tiemp_semaforo['largo'])
regla42 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['fuerte'] & h_del_dia['pico1'], tiemp_semaforo['largo'])
regla43 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['fuerte'] & h_del_dia['pico2'], tiemp_semaforo['largo'])
regla44 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['fuerte'] & h_del_dia['regular'], tiemp_semaforo['largo'])
regla45 = ctrl.Rule(vol_trafico['alto'] & cond_climaticas['fuerte'] & h_del_dia['tarde/noche'], tiemp_semaforo['largo'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1,regla2,regla3,regla4,regla5,regla6,regla7,regla8,regla9,regla10,regla11,regla12,regla13,regla14,regla15,regla16,regla17,regla18,regla19,regla20,regla21,regla22,regla23,regla24,regla25,regla26,regla27,regla28,regla29,regla30,regla31,regla32,regla33,regla34,regla35,regla36,regla37,regla38,regla39,regla40,regla41,regla42,regla43,regla44,regla45])
sistema_control_difuso = ctrl.ControlSystemSimulation(sistema_control)

# Asignar valores de entrada al sistema de control difuso
sistema_control_difuso.input['vol_trafico'] = 128
sistema_control_difuso.input['cond_climaticas'] = 22
sistema_control_difuso.input['h_del_dia'] = 8

# Activar el sistema de control difuso
sistema_control_difuso.compute()

# Obtener el valor de salida del sistema de control difuso
tiempo_del_semaforo = sistema_control_difuso.output['tiemp_semaforo']

# Mostrar el resultado
print("Valor de tiempo del semaforo:", tiempo_del_semaforo)

# Graficar las funciones de membresía y la salida
vol_trafico.view(sim=sistema_control_difuso)
cond_climaticas.view(sim=sistema_control_difuso)
h_del_dia.view(sim=sistema_control_difuso)
tiemp_semaforo.view(sim=sistema_control_difuso)