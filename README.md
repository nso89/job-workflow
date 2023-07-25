# job-workflow
Automate creating job folders and moving your base cover letter and resume.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Documents`, a folder named `Work`.
* Under `Work`, a copy of your base cover letter and resume in one file (`cover-letter-resume.odt`).

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `job-workflow-main.zip`.

**Example**:
```batch
C:\Users\nso89\job-workflow-main\main.py
```

#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `job-workflow-main` folder.

**Example**:
```batch
C:\Users\nso89>cd job-workflow-main
```

2. Start the `main.py` script.

Example:

```batch
C:\Users\nso89\job-workflow-main>python main.py
```

3. It asks you for the `Company Name` and `Position`.

**Example**:
```batch
Company Name: Microsoft
Position: Software Engineer
```

4. The script creates 2 folders, the `Company Name` as the parent and the `Position` as the subfolder. It copies the `cover-letter-resume.odt` to the new folders.

**Example**:
```batch
Copying ...\Documents\Work\cover-letter-resume.odt to ...\Documents\Work\Microsoft\Software Engineer
```

#### <a name="configuration"></a>Configuration
If you need to change the `cover_letter_resume_odt` folder:

1. Open the `main.py` script in any text editor.
2. Locate the `cover_letter_resume_odt` variable.

**Example**:
```python
cover_letter_resume_odt = Path.home().joinpath("Documents\\Work\\cover-letter-resume.odt")
```
3. When you finish changing the variables, save and close the editor.
