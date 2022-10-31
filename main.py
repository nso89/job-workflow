from pathlib import Path
import shutil

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

def validate_parameters(validate: str, parameter: str):
    """
    Verify if validate is blank, if so, raise ValueError 
    indicating the parameter cannot be blank.
    
    Args:
    validate: str - the string we're checking.
    parameter: str - what the str represents.
    
    Returns:
    None
    """
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")

def main():

    JOB_DETAILS = "job-details.txt"
    cover_letter_resume_odt = Path.home().joinpath("Documents\\Work\\cover-letter-resume.odt")
    
    try:
        
        company_name = input("Company Name: ")
        position = input("Position: ")

        company_name = company_name.strip()
        position = position.strip()

        validate_parameters(company_name, "Company Name")
        validate_parameters(position, "Position")

        company_name_position = Path(company_name.title()).joinpath(position.title())
        destination = Path(cover_letter_resume_odt.parent).joinpath(company_name_position)
        destination.mkdir(parents = True)

        print(f"Copying {cover_letter_resume_odt} to {destination}.")
        shutil.copy(src = cover_letter_resume_odt, dst = destination)
        write_word_to(file_name = JOB_DETAILS, word = str(destination))
        
    except(ValueError,FileNotFoundError,PermissionError) as e:
        print(e)

if __name__ == "__main__":
    main()
