""" Prueba de regex
Itera sobre una lista de descriciones comerciales de importacion, intenta obtener 
su concentracion, unidad, presentacion y forma farmacologica(10 mg 20 tabletas)
de dicha descripcion.

variables
---------
    descripciones:
        Es una lista de descripciones comerciales de ciertas importaciones de ciertos medicamentos
    expresion_x:
        expresiones regulares
        
JC 31/7/22
"""
import re

UNIDAD_CONCENTRACION = ['mg','µG']
FORMA_FARMA = ['tabletas', 'capsulas','comprimidos','solucion inyectable', 'solucion oral']

descripciones = [
    'giotrif 30mg (afatinib) 30 tabletas (medicamento de uso humano)',
    'medicamento trazimera (trastuzumab) caja de carton con un frasco ampula con 440 mg de polvo liofilizado y un frasco ampula con 20 ml de diluyente e instructivo anexo',
    'medicamentos (keytruda[pembrolizumab 100mg/4ml]en caja con frasco con solucion inyectable para infusion intravenosa).',
    'tafinlar 75 mg 28capsulas (dabrafenib)',
    'jakavi 15 mg 60 tabletas (ruxolitinib)',
    'votrient 400 mg 60 tabletas (pazopanib)',
    'mekinist 0.5 mg  30 comprimidos (trametinib)',
    'afinitor 5 mg  30 comprimidos (everolimus)',
    'tykerb 250 mg tabletas (lapatinib)',
    'tasigna 200 mg capsulas (nilotinib)',
    'afinitor 10 mg  30 comprimidos (everolimus)'
]

#giotrif 30mg (afatinib) 30 tabletas (medicamento de uso humano)
expresion_1_1 = '\d+\.?\d*\s*mg.{0,40}\d{1,4}\s*(tabletas|capsulas|comprimido|solucion inyectable|solucion oral)'

#avastin  100 mg/4 ml solucion inyectable (bevacizumab)
expresion_soluciones = '\d+\.?\d*\s*mg.{0,30}\s*(solucion inyectable|solucion oral)'

#mvasi (bevacizumab) ampula con 100 mg/ 4.0 ml (medicamento de uso humano)
expresion_4 = '(frasco ampula|vial|ampula|jeringa)\s*.{0,5}\d+\s*mg'


for desc_comer in descripciones:
    match = re.search(expresion_1_1, desc_comer)#'\d+\.?\d*\s*mg.{0,40}\d{1,4}\s*(tabletas|capsulas|comprimidos|solucion inyectable|solucion oral)'
    if match:#100 mg/4 ml solucion inyectable
        info = match.group()
        c_uc =  re.search("\d+\.?\d*\s*mg", info).group()
        concentracion = re.search("\d+\.?\d*", c_uc).group()
        unidad_concentracion = "mg"
        p_ff = re.search("\d{1,4}\s*(tabletas|capsulas|comprimido|solucion inyectable|solucion oral)", info).group()
        presentacion =  re.search("\d{1,4}", p_ff).group()
        forma_farma = re.search("(tabletas|capsulas|comprimido|solucion inyectable|solucion oral)", p_ff).group()
        forma_farma = 'comprimidos' if  'comrpimido' in forma_farma else forma_farma
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue

    match = re.search(expresion_soluciones, desc_comer)#'\d+\.?\d*\s*mg.{0,30}\s*(solucion inyectable|solucion oral)'
    if match:#100 mg/4 ml solucion inyectable
        info = match.group()
        concentracion = re.search("\d+\.?\d*", info).group()
        unidad_concentracion = 'mg'
        presentacion = '1'
        forma_farma = re.search("(tabletas|tab|capsulas|comprimidos|solucion inyectable|solucion oral)", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue

    match = re.search(expresion_4, desc_comer)#'(frasco ampula|vial|ampula|jeringa)\s*.{0,15}\d+\.?\d*\s*mg'
    if match:#ampula con 100 mg  
        info = match.group()
        c_uc = re.search("\d+\.?\d*\s*mg", info).group()
        concentracion = re.search("\d+\.?\d*", c_uc).group()
        unidad_concentracion = 'mg'
        presentacion = '1'
        forma_farma = re.search("(frasco ampula|vial|ampula|jeringa)", info).group()
        print(concentracion, unidad_concentracion, presentacion, forma_farma)
        continue
    
    print(f"No se pudo obtener datos de: {desc_comer}")