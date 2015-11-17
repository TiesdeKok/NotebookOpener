# Jupyter (IPython) Notebook Opener

Utility (GUI) to open and manage Jupyter (IPython) notebooks using different Python environments and working directories. 

![Notebook Opener](https://raw.githubusercontent.com/TiesdeKok/NotebookOpener/master/example.png)

**Author:**   Ties de Kok *(t.c.j.dekok@tilburguniversity.edu)*  
**Twitter:** [@TiesdeKok](https://twitter.com/TiesdeKok/)  
**Homepage:**    https://github.com/TiesdeKok/NotebookOpener  

## Practical information:

####**You can use the Notebook Opener in two ways:**

Use the standalone executable:
> 1. Download notebook_opener.zip from this GitHub depository.   [**[Download link]**](https://github.com/TiesdeKok/NotebookOpener/raw/master/notebook_opener.zip)
> 2. Extract the *notebook_opener* folder in the .zip file to a folder of your choice.
> 3. Run the Notebook Opener using *notebook_opener.exe*
> [Tip] Create a shortcut to this executable or drag the .exe onto your taskbar for easy access.

Run it yourself using Python 3:
> 1. download notebook_opener.py
> 2. start it using your Python 3 environment

#### **Add your own Python environments**
This tool is inspired by the shortcuts provided with the Anaconda and Canopy Python distributions. 
These shortcuts work by starting a command prompt and running a batch file to select the appropriate Python environment. The *Notebook Opener* copies this technique and thus requires a batch (.bat) file to define the environment. 

1. Find or create the batch file that specifies your Python environment.
	* Default directories for Anaconda and Canopy are:
		- Anaconda (Python 2.7):
			- C:\Users\ **USERNAME** \Anaconda\Scripts\ **anaconda.bat**
		- Anaconda (Python 3.x):
			-   C:\Users\ **USERNAME** \Anaconda3\Scripts\ **anaconda.bat**
		- Canopy
			- C:\Users\ **USERNAME** \AppData\Local\Enthought\Canopy\User\Scripts\ **activate.bat**
2. Click the *Add* button under the *Python environments* box.

![Notebook Opener](https://raw.githubusercontent.com/TiesdeKok/NotebookOpener/master/example_1.png)

#### **Save a working directory**
It is possible to Add/Remove working directories (very convenient if you have multiple projects at the same time!).

1. Select your working directory (folder) using the *Browse* button.
2. To save this working directory click the *Add* button under the *Saved directories* box. 

#### **Additional features**
> * Works with both IPython 3 and IPython 4 (automatically detects the notebook command to use)
> * Select *Default Python* as an environment to start the default Python environment (no .bat file needed)
> * Deselect *Open notebook* to only start a command prompt with the Python environment.
> * Invalid .bat files and missing IPython installations trigger a warning to be displayed in the program. 
> * Environments and directories are saved to *notebook_opener/config.ini* in the *appdata* folder. 

Have additional feature requests / suggestions? Feel free to open an issue! 