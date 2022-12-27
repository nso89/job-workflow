from pathlib import Path
import shutil


JOB_DETAILS = "job-details.txt"
COVER_LETTER_RESUME = Path.home().joinpath("Documents\\Work\\cover-letter-resume.odt")


def write_word_to(file_name: Path, word: str) -> None:
    """
    Write a string to a file.
    
    Args:
        file_name: str
        word : str
    
    Returns:
        None
    """
    with open(file_name, "w") as f_obj:
        print(f"Writing {word} to {file_name}")
        f_obj.write(word)

        
def validate_parameters(validate: str, parameter: str) -> None:
    """
    Verify if validate is blank, if so, raise ValueError 
    indicating the parameter cannot be blank.
    
    Args:
        validate: str - the string we're checking.
        parameter: str - what validate represents.
    
    Returns:
        None
    """
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")
    if validate.startswith(" ") or validate.endswith(" "):
        raise ValueError(f"{parameter} cannot be blank!")

        
def main():
   
    try:
        
        company_name = input("Company Name: ").strip()
        position = input("Position: ").strip()

        validate_parameters(company_name, "Company Name")
        validate_parameters(position, "Position")

        company_name_position = Path(company_name.title()).joinpath(position.title())
        destination = Path(COVER_LETTER_RESUME.parent).joinpath(company_name_position)
        destination.mkdir(parents = True)

        print(f"Copying {COVER_LETTER_RESUME} to {destination}.")
        shutil.copy(src = COVER_LETTER_RESUME, dst = destination)
        write_word_to(file_name = JOB_DETAILS, word = str(destination))
        
    except(ValueError, FileNotFoundError, FileExistsError, PermissionError) as e:
        print(e)

if __name__ == "__main__":
    main()
