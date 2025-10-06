## MEtadaten über Projekt und Abhängigkeiten. Projekt als Paket PyPi möglich 

from setuptools import find_packages, setup
from typing import List  

HYPEN_E_DOT="-e ." 
def get_requirements(file_path:str)->List[str]: 
    '''
    Diese Funktion gibt eine Liste der requirements zurück
    '''
    requirements=[]
    with open(file_path) as file_obj:
        # Lese die Zeilen aus requirements.txt und speichere sie in Liste
        requirements=file_obj.readlines()
        # entferne Leerzeichen die beim Speichern mitgenommen werden
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT) 

    return requirements 

        


setup(
    name='ML Beispielprojekt',
    version='0.0.1',
    author='Kasim',
    author_email='kasimak444@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')

)

