Directories stucture (for reference):
-------------------------------------
.. code:: bash

    (root)
      |- ibeis
        |- db
        |- dev
        |- docs
        |- dtool
        |- flukematch
        |- futures_actors
        |- guitool_ibeis
        |- ibeis
            |- pydarknet
        |- plottool_ibeis
        |- requirements
        |- test
        |- utool
        |- vtool_ibeis_ext


Setup steps
-----------

1. Setup python virtual env & OpenCV, follow this `guide <https://pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/>`_

2. Setup Qt5, refer to this `guide <https://forums.developer.nvidia.com/t/jetson-nano-and-qt5/76870/>`_

3. numpy 1.19.5 will cause error: Illegal instruction (core dumped)

.. code:: bash

    pip install numpy==1.19.4

4. Pydarknet — very old libraries. Code related to OpenCV has been remove, 
as the code referring to very old OpenCV version 2.
   - use this `repo <https://github.com/chancsc/ibeis-pydarknet>`_

.. code:: bash

    cd pydarknet
    python3 setup.py develop


5. install additional modules (to put into part of requirements modules)

.. code:: bash

    pip install utool
    pip install flask Pillow lockfile simplejson
    pip install tornado pyzmq
    pip install pynmea2
    pip install psutil
    pip install Lasagne
    pip install -U flask-cors


6. vtool_ibeis_ext, pyflann_ibeis, pyhesaff

Method 1: install using pip

.. code:: bash

    pip install vtool_ibeis_ext  pyflann_ibeis pyhesaff

Method 2: build it. e.g.

.. code:: bash

    git clone <URL>
    cd pyhesaff
    mkdir build
    cd build
    cmake ..
    make
    sudo make install

7. Install vext.pyqt5, this module is to link to the system level pyqt5, 
otherwise install of pyqt5 will keep failing

.. code:: bash

    pip install vext.pyqt5

8. Install Theano

.. code:: bash

  git clone https://github.com/Theano/Theano.git
  git checkout rel-0.8.2
  python setup.py develop

9. Install various ibeis modules
guitool_ibeis, plottool_ibeis, dtool_ibeis, vtool_ibeis, pyhesaff

.. code:: bash

  cd guitool_ibeis
  pip install -e .

10. Install pyflann_ibeis

.. code:: bash

      (py3cv3) nano@jetson:~/vibeis/pyflann_ibeis/$ python setup.py develop

11. Checkout & make the flukematch:

.. code:: bash

      ibeis-flukematch-module
      cd ibeis-flukematch-module
      make
      mv flukematch_lib.so ibeis_flukematch\
      python3 setup.py develop

12. Copy the following folders into the \ibeis   (refer to the directories structure above)

.. code:: bash

    \vtool_ibeis\vtool_ibeis as vtool
    \dtool_ibeis\dtool_ibeis as dtool
    \plottool_ibeis\plottool_ibeis as plottool
    \futures_actors\futures_actors as futures_actors

13. to run ibeis:

.. code:: bash

    (py3cv3) nano@jetson:~/vibeis/ibeis$ python3 -m ibeis

