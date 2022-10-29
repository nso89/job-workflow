from pathlib import Path
import os, shutil

def write_path_to(file_name: Path, odt_file: str) -> None:
      with open(file_name, "w") as f_obj:
        print(f"Writing {odt_file} to {file_name}")
        f_obj.write(odt_file)

def validate_parameters(validate: str, parameter: str):
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
        write_path_to(file_name = JOB_DETAILS, odt_file = str(destination))
        
    except(ValueError,FileNotFoundError,PermissionError) as e:
        print(e)

if __name__ == "__main__":
    main()
