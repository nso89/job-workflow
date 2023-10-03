from pathlib import Path
import shutil


COVER_LETTER_RESUME = Path.home().joinpath(r"Documents\Work\main.tex")


def verify(parameter: str, name: str) -> None:
    """
    Verify if parameter is blank, if so, raise ValueError.
    """
    if not parameter or parameter.isspace():
        raise ValueError(f"{name} cannot be blank!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot begin or end with an empty space!")

    
def main():

    try:

        company_name = input("Company Name: ").strip()
        verify(parameter = company_name, name = "Company Name")
        
        position = input("Position: ").strip().title()
        verify(parameter = position, name = "Position")

        job_file_location = COVER_LETTER_RESUME.parent.joinpath(company_name).joinpath(position)
        job_file_location.mkdir(parents = True, exist_ok =  False)
       
        print(f"Copying {COVER_LETTER_RESUME} -> {job_file_location}")
        shutil.copy(src = COVER_LETTER_RESUME, dst = job_file_location)
    
    except(FileExistsError, FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == '__main__':
    main()
