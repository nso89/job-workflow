# job-workflow
Automate creating job folders and moving your base cover letter and resume.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Cleaning Up](#cleaning-up)

#### <a name="prerequisites"></a>Prerequisites
1. A complete install of `Python 3.x`.
2. A folder labelled `Work` under your `Documents` folder.
3. A copy of your base cover letter and resume in one file, saved as a `.odt` file in your `Work` folder.

#### <a name="setup"></a>Setup:
Under your `USERPROFILE`, extract `job-workflow.zip`.

**Example**:
```
C:\Users\nso89\job-workflow\main.py
C:\Users\nso89\job-workflow\job-app.bat
```
#### <a name="running-the-script"></a>Running the Script:
1. Open `cmd.exe` and change the directory to the `job-workflow` folder.

**Example**:
```batch
C:\Users\nso89>cd job-workflow
```
2. Start the `run.bat` script.

**Example**:
```batch
C:\Users\nso89\job-workflow>start run.bat
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

5. The path will get written to `job-details.txt`, so that the `run.bat` can open it in our default editor. 

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
