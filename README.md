# bsu\_seg\_chapter
Boise State University SEG Student Chapter

This repository contains a collection of Python-based Jupyter Notebooks for educational lessons. 

If you want to update your conda to the latest version, run the following from the command line.

	$ conda update -n base conda

Note that conda has changed the environment activation command. They now use

	$ conda activate env_name
	
instead of the deprecated

	$ source activate env_name

After activating your environment, remember that you need to install the jupyter notebook module before you can run a notebook. You only need to do this once, and you can do it with the following line of code.

	$ conda install jupyter notebook

For the e-packages, we need to install the ipywidget module. This is not in the standard conda distribution, so we need to add one more argument to the installation command. Run the following to install the ipython widget.

	$ conda install -c conda-forge ipywidgets
	
Note that if you use conda, the notebook extension is enabled automatically. This is not the case if you use pip to install ipywidgets. You can read more about that [here](https://ipywidgets.readthedocs.io/en/stable/user_install.html).

You will also need to install the matplotlib and scipy modules.

	$ conda install matplotlib
	$ conda install scipy

The numpy module will be installed automatically with matplotlib.
	 