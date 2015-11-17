from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os 
import subprocess
import configparser
import os
import json

"""
This Python script uses Tkinter to create a GUI for opening Jupyter (IPython) notebooks using different Python environments and working directories.

Made by: Ties de Kok
Contact: T.C.J.dekok@tilburguniversity.edu
License: MIT
Version: 0.1.0
"""

class GUI:
    def __init__(self, rootWindow):
        
        self._config_dir = os.path.join(os.environ['APPDATA'], 'notebook_opener')
        self._config_file = os.path.join(self._config_dir, 'config.ini')
        self.config = configparser.ConfigParser()
        
        self.check_config_dir()
        self.config.read(self._config_file)
        
        self.home = os.path.expanduser("~")
        
        self.button_notebook = IntVar()
        self.button_notebook.set(1)

        self.check1 = Checkbutton(rootWindow, text="Open notebook", variable=self.button_notebook, onvalue=1, offvalue=0)
        self.check1.grid(row=9, column=10, columnspan=2)
        
        self.label = Label(rootWindow, text='Jupyter (IPython) Notebook Opener')
        self.label.grid(row=0, column=6, columnspan=6, pady=10)

        self.button1 = Button(rootWindow, text="Start", command=self.enter)
        self.button1.grid(row=8, column=10, columnspan=2)
        
        self.button2 = Button(rootWindow, text="Browse", command=self.getDir)
        self.button2.grid(row=6, column=6)
        
        self.button3 = Button(rootWindow, text='Add', command=self.add)
        self.button3.grid(row=9, column=3, pady=5)
        
        self.button4 = Button(rootWindow, text='Remove', command=self.remove)
        self.button4.grid(row=9, column=4, pady=5)
        
        self.button5 = Button(rootWindow, text='Add', command=self.add_1)
        self.button5.grid(row=9, column=0, pady=5)
        
        self.button6 = Button(rootWindow, text='Remove', command=self.remove_1)
        self.button6.grid(row=9, column=1, pady=5)
        
        self.label1 = Label(rootWindow, text='Python environments')
        self.label1.grid(row=0, column=0, columnspan=2)
        self.label2 = Label(rootWindow, text='Saved directories')
        self.label2.grid(row=0, column=3, columnspan=2)
        
        self.label_about = Label(rootWindow, text='Made by Ties de Kok  |  GitHub: https://github.com/TiesdeKok/')
        self.label_about.grid(row=10, column=0, columnspan=5, pady=5)
        
        self.listbox = Listbox(rootWindow, width = 30, selectmode=SINGLE)
        self.listbox.grid(row=1, column=3, columnspan=2, rowspan=8, padx=10)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        
        self.lbpython = Listbox(rootWindow, width = 30, selectmode=SINGLE)
        self.lbpython.grid(row=1, column=0, columnspan=2, rowspan=8, padx=10)
        self.lbpython.bind('<<ListboxSelect>>', self.onselect_1)
        
        self.text = Entry(rootWindow, width=80, background="ivory")
        self.text.grid(row=6, column=7, columnspan=5, padx=8)
        
        self.label_python = Label(rootWindow, text='Current Python selection:')
        self.label_python.grid(row=8, column=6, columnspan=2)
        self.label_env = Label(rootWindow, text='No selection.')
        self.label_env.grid(row=8, column=8, columnspan=2, sticky=W)
        
        self.label_description = Label(rootWindow, text = 'After selecting a Python environment and a working directory click Start to launch the notebook. \n'
                                      '   It is possible to save the environment and working directory using the Add / Remove buttons.')
        self.label_description.grid(row=1, column=6, columnspan=6, rowspan=5, ipady=7)
        
        self.label_error = Label(rootWindow, text = '', foreground='red', font = "TkDefaultFont 14 bold")
        self.label_error.grid(row=9, column=6, columnspan=4)
        
        self.load_stored()
        
        rootWindow.bind("<Return>", lambda event: self.enter())
        rootWindow.wm_title("Notebook Opener")
    
    def add(self):
        def process():
            self.listbox.insert(END, name.get())
            self.listbox_dict[name.get()] = self.text.get()
            temp = self.listbox_to_dict(self.listbox_dict, self.listbox)
            self.config.set('Stored dictionaries', 'dirs', json.dumps(temp))
            self.update_config()
            toplevel.destroy()
            
        toplevel = Toplevel()
        toplevel.attributes('-topmost', True)
        toplevel.attributes('-topmost', False)
        label = Label(toplevel, text='Provide a name:')
        label.grid(row=0, pady=5)
        name = Entry(toplevel, width = 30, background='ivory')
        name.grid(row=1, pady=5, padx=10)
        name.focus()
        button = Button(toplevel, text='Submit', command=process)
        button.grid(row=2, pady=5)
        toplevel.bind("<Return>", lambda event: process())
        
    def add_1(self):
        def process():
            self.lbpython.insert(END, name.get())
            self.lbpython_dict[name.get()] = script.get()
            temp = self.listbox_to_dict(self.lbpython_dict, self.lbpython)
            self.config.set('Stored dictionaries', 'python_env', json.dumps(temp))
            self.update_config()
            toplevel.destroy()
            
        def getFile():
            fileName = filedialog.askopenfilename(initialdir=self.home, filetypes=[('Batch script', '*.bat')], title='Select your script file:', parent=toplevel)
            script.delete(0, 'end')
            script.insert(INSERT, fileName)
            name.focus()
            
        toplevel = Toplevel()
        toplevel.attributes('-topmost', True)
        toplevel.attributes('-topmost', False)
        label = Label(toplevel, text='Provide the script path:')
        label.grid(row=0, pady=5)
        script = Entry(toplevel, width = 80, background='ivory')
        script.grid(row=1, pady=5, padx=10)
        script.focus()
        button_1 = Button(toplevel, text='Browse', command=getFile)
        button_1.grid(row=2, pady=5)
        label_1 = Label(toplevel, text='Provide a name:')
        label_1.grid(row=3, pady=5)
        name = Entry(toplevel, width = 30, background='ivory')
        name.grid(row=4, pady=5)
        button = Button(toplevel, text='Submit', command=process)
        button.grid(row=5, pady=5)
        toplevel.bind("<Return>", lambda event: process())
        
    def remove(self):
        if not len(self.listbox_dict) == 0:
            index = self.listbox.curselection()[0]
            self.listbox_dict.pop(self.listbox.get(index))
            self.listbox.delete(index)
            temp = self.listbox_to_dict(self.listbox_dict, self.listbox)
            self.config.set('Stored dictionaries', 'dirs', json.dumps(temp))
            self.update_config()
        
    def remove_1(self):
        if not len(self.lbpython_dict) == 0:
            if not self.lbpython.get(self.lbpython.curselection()[0]) == 'Default Python':
                index = self.lbpython.curselection()[0]
                self.lbpython_dict.pop(self.lbpython.get(index))
                self.lbpython.delete(index)
                temp = self.listbox_to_dict(self.lbpython_dict, self.lbpython)
                self.config.set('Stored dictionaries', 'python_env', json.dumps(temp))
                self.update_config()
        
    def enter(self):
        if self.text.get() == '':
            work_dir = self.home
        else:
            work_dir = self.text.get()
            
        if not self.check_python() == 'failed':
            if self.button_notebook.get() == 1:
                version = self.check_version()
                if not version == "failed":
                    if version >= 4:
                        command = 'cmd.exe /k %s && cd /d %s && jupyter notebook' % (self.current_python, work_dir)
                    else:
                        command = 'cmd.exe /k %s && cd /d %s && ipython notebook' % (self.current_python, work_dir)
                    subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
                    self.label_error.config(text = '')
                else:
                    self.label_error.config(text = 'Error: IPython could not be found.')
            else:
                command = 'cmd.exe /k %s && cd /d %s' % (self.current_python, work_dir)
                subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
                self.label_error.config(text = '')
        else:
            self.label_error.config(text = 'Error: Python environment not valid.')
        
    def onselect(self, arg):
        if not len(self.listbox_dict) == 0:
            index = self.listbox.curselection()[0]
            value = self.listbox_dict[self.listbox.get(index)]
            self.text.delete(0, 'end')
            self.text.insert(INSERT, value)
            
    def onselect_1(self, arg):
        if not len(self.lbpython_dict) == 0:
            index = self.lbpython.curselection()[0]
            value = self.lbpython_dict[self.lbpython.get(index)]
            self.label_env.config(text = self.lbpython.get(index))
            self.current_python = value
        
    def getDir(self):
        dirName = filedialog.askdirectory(initialdir=self.home)
        self.text.delete(0, 'end')
        self.text.insert(INSERT, dirName)
    
    def check_version(self):
        if self.label_env.cget("text") == 'Default Python':
            cmd = ['cmd.exe', '/k', 'python', '-c', "import IPython; print('findme' + IPython.__version__)"]
        else:
            cmd = ['cmd.exe', '/k', self.current_python, '&&' 'python', '-c', "import IPython; print('findme' + IPython.__version__)"]
        p = subprocess.Popen(cmd, creationflags= 0x08000000, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
        output = ' '.join([x.decode('utf-8') if x != None else "" for x in p.communicate()])
        try:
            version = int(re.search('(?<=findme).', output).group(0))
            return version
        except:
            return "failed"
    
    def check_python(self):
        cmd = ['cmd.exe', '/k', self.current_python, '||', 'ECHO', 'statusfailed']
        p = subprocess.Popen(cmd, creationflags= 0x08000000, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
        output = p.communicate()[0].decode("utf-8")
        if re.search('statusfailed', output):
            return "failed"
        else:
            return "success"       
    
    def check_config_dir(self):
        if not os.path.exists(self._config_dir):
            os.makedirs(self._config_dir)
        if not os.path.isfile(self._config_file):
            with open(self._config_file, 'w') as configfile:
                self.config.add_section('Stored dictionaries')
                self.config.set('Stored dictionaries', 'python_env', '{"Default Python": [0, "ECHO Default"]}')
                self.config.set('Stored dictionaries', 'dirs', '{}')
                self.config.write(configfile)
                
    def ConfigSectionMap(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                dict1[option] = None
        return dict1
    
    def listbox_to_dict(self, lb_dict, lb):
        out_dict = {}
        if len(lb_dict) > 0:
            for x in range(0, len(lb_dict)):
                out_dict[lb.get(x)] = x
            return_dict = {a : (b, c) for a, b, c in zip(list(lb_dict.keys()), list(out_dict.values()), list(lb_dict.values()))}
            return return_dict
        else:
            pass
        
    def update_config(self):
        with open(self._config_file, 'w') as configfile:
            self.config.write(configfile)
            
    def load_stored(self):
        temp_env = json.loads(self.ConfigSectionMap("Stored dictionaries")['python_env'])
        self.lbpython_dict = {x : y[1] for x, y in temp_env.items()}
        for x, y in temp_env.items():
            self.lbpython.insert(y[0], x)
        self.current_python = self.lbpython_dict['Default Python']
        self.label_env.config(text = 'Default Python')
            
        temp_dirs = json.loads(self.ConfigSectionMap("Stored dictionaries")['dirs'])
        if len(temp_dirs) > 0:
            self.listbox_dict = {x : y[1] for x, y in temp_dirs.items()}
            for x, y in temp_dirs.items():
                self.listbox.insert(y[0], x)
        else:
            self.listbox_dict = {}        

if __name__ == '__main__':
    rootWindow = Tk()
    gui = GUI(rootWindow)
    rootWindow.mainloop()