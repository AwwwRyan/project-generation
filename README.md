Application Generator using GPT/AI-
This Python script utilizes GPT (Generative Pre-trained Transformer) to generate applications based on user input. The generated code is then packaged into a zip file for easy distribution.

Assignment Summary-
The purpose of this script is to automate the generation of applications using AI. The script prompts the user for input regarding the type of application they want to build and then leverages AI to generate the necessary file structure and content.

Script Logic-
1. User Input: The script starts by prompting the user to specify the type of application they wish to create.
2. File Structure Generation: The user input is sent to the GPT AI model, which generates a file structure for the application based on the provided prompt. A maximum of 20 files are generated.
3. File Content Generation: Each file in the generated file structure is populated with content by communicating with the AI model. The initial requirements and generated file structure are provided as system context to guide the content generation.
4. Zip File Creation: Once all files are generated and populated, they are packaged into a zip file in the current working directory for easy distribution and storage.
5. Optional Testing: While not mandatory, the script can optionally include testing functionality to ensure the generated application works as expected.

Usage
1. Clone the repository or download the script to your local machine.
2. Ensure you have the necessary dependencies installed, including the OpenAI library.
3. Run the script and follow the prompts to generate your application.
4. Retrieve the generated zip file from the working directory.

Dependencies
1. Python 3.x
2. OpenAI library

Note
1. Ensure you have the required API key for accessing the GPT AI model.
2. This script is designed to handle a maximum of 20 files for generating the application.

Disclaimer
While the generated application files aim to meet the user's requirements, manual review and adjustment may still be necessary for complete functionality.
1
