from pathlib import Path
import shutil, os


COVER_LETTER_RESUME = Path.home().joinpath("Documents\\Work\\cover-letter-resume.odt")


def verify(parameter: str, name: str) -> None:
    """
    Check the parameter to make sure it isn't empty or that
    it doesn't start or end with an empty space.
    """
    if parameter == "":
        raise ValueError(f"{name} cannot be empty!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot start or end with an empty space!")

    
def main():

    try:

        company_name = input("Company Name: ").strip()
        verify(parameter = company_name, name = "Company Name")
        
        position = input("Position: ").strip().title()
        verify(parameter = position, name = "Position")

        job_file_location = COVER_LETTER_RESUME.parent.joinpath(company_name).joinpath(position)
        job_file_location.mkdir(parents = True, exist_ok =  False)
       
        print(f"Copying {COVER_LETTER_RESUME} -> {job_file_location}")
        os.startfile(shutil.copy(src = COVER_LETTER_RESUME, dst = job_file_location))
    
    except(FileExistsError, FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == '__main__':
    main()
