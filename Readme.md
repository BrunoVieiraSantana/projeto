
<span align="center">

##  Sistema de Gestão Financeira Pessoal 💵

</span>

<p align="center">
  Aplicação de gerenciamento financeiro pessoal com integração à um banco de dados
relacional.
  



## 💻 Instalação
<strong>Bibliotecas necessárias</strong><br />
+ Bibliotecas necessarias para a interface gráfica<br />
  - python -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip"<br />
  - pip install https://github.com/kivymd/KivyMD/archive/master.zip<br />

+ Bibliotecas necessarias para criação de gráficos<br />
  - pip install kivy-garden<br />
  - garden install graph<br />
  - pip install matplotlib<br />

___



<strong>Comandos utilizados para a criação de um ambiente virtual:</strong><br />
python -m venv venv<br />
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned<br />
.\venv\Scripts\Activate.ps1<br />

___

</p>
<strong>Teste de bibliotecas:</strong><br />
pip install kivy-garden<br />
garden install matplotlib<br />
pip install matplotlib<br />
</p>
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')<br />
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy, FigureCanvasKivyAgg<br />
from matplotlib.figure import Figure<br />
import matplotlib.pyplot as plt<br />
