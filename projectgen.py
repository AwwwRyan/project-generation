from openai import OpenAI
import openai
import zipfile
import time

api_key1 = '''api key'''
client=OpenAI(api_key=api_key1)

def get_user_input():
    return input("What application do you want to build? ")

def generate_file_structure(prompt):
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are an expert software developer."},
                    {"role": "user", "content": prompt},
                    {"role": "system", "content": "Generate a file structure for the application. Use a maximum of 20 files."},
                    
                ]
            )
            print(response.choices[0].message)
            return response['choices'][0]['message']['content']
        except openai.RateLimitError:
            print(f"Rate limit exceeded while generating {prompt}. Retrying in 60 seconds...")
            time.sleep(60)

def generate_file_content(file_name, context):
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are an expert software developer"},
                    {"role": "system", "content": context},
                    {"role": "user", "content": f"Generate the content for the file: {file_name}"}
                ]
            )
            print(response.choices[0].message)
            return response['choices'][0]['message']['content']
        except openai.error.RateLimitError:
            print(f"Rate limit exceeded while generating {file_name}. Retrying in 60 seconds...")
            time.sleep(60)


def create_files(file_structure, context):
    file_dict = {}
    for file_name in file_structure.split('\n'):
        if file_name.strip():
            file_content = generate_file_content(file_name.strip(), context)
            file_dict[file_name.strip()] = file_content
    return file_dict

def save_files_to_zip(file_dict, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for file_name, content in file_dict.items():
            zipf.writestr(file_name, content)


user_input = get_user_input()
file_structure = generate_file_structure(user_input)
    
file_lines = file_structure.split('\n')
if len(file_lines) > 20:
    file_lines = file_lines[:20]
file_structure = '\n'.join(file_lines)
    
context = f"The user wants to build the following application:\n{user_input}\nHere is the file structure:\n{file_structure}"
file_dict = create_files(file_structure, context)
    
zip_file_name = "generated_application.zip"
save_files_to_zip(file_dict, zip_file_name)
    
print(f"Application files have been generated and saved to {zip_file_name}")