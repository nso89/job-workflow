# job-workflow
Automate creating job folders and moving your base cover letter and resume.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Cleaning Up](#cleaning-up)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
1. A complete install of `Python 3.x`.
2. Under `Documents`, a folder named `Work`.
3. A copy of your base cover letter and resume in one file (`cover-letter-resume.odt`), in your `Work` folder.

#### <a name="setup"></a>Setup:
Under your `USERPROFILE`, extract `job-workflow-main.zip`.

**Example**:
```
C:\Users\nso89\job-workflow-main\main.py
C:\Users\nso89\job-workflow-main\job-app.bat
```
#### <a name="running-the-script"></a>Running the Script:
1. Open `cmd.exe` and change the directory to the `job-workflow-main` folder.

**Example**:
```batch
C:\Users\nso89>cd job-workflow-main
```
2. Start the `run.bat` script.

**Example**:
```batch
C:\Users\nso89\job-workflow-main>start run.bat
```
3. The `run.bat` script starts the `main.py` script, and asks you for the `Company Name` and `Position`.

**Example**:
```batch
Company Name: Microsoft
Position: Software Engineer
```

4. The script creates 2 folders, with the `Company Name` as the parent, the `Position` as the subfolder. It copies the `cover-letter-resume.odt` to the new folders. 
```batch
...\Documents\Work\cover-letter-resume.odt to ...\Documents\Work\Microsoft\Software Engineer.
```

5. The path will get written to `job-details.txt`, so that the `run.bat` can open it in your default editor. 

**Example**:
```batch
Writing ...\Documents\Work\Microsoft\Software Engineer to job-details.txt.
Opening ...\Documents\Work\Microsoft\Software Engineer\cover-letter-resume.odt.
```

#### <a name="cleaning-up"></a>Cleaning Up:
1. You don't have to delete this file manually, the `run.bat` can do it for you.

**Example**:
```batch
Removing job-details.txt.
```
#### <a name="configuration"></a>Configuration
If you need to change the `source` folder:
1. Open the `main.py` script in any text editor.
2. Locate the `cover_letter_resume_odt` variable.

**Example**:
```python
cover_letter_resume_odt = Path.home().joinpath("")
```
3. When you finish changing the variables, save and close the editor.
