# Daily Contribution Bot

This Python script automates random contributions to a GitHub repository. It makes random changes to files within the repository, simulating activity that could be beneficial for maintaining an active GitHub profile. 

# Insp

i developed this because some1 was mocking me by comparing his & mine contributions in our workspace . i checked his profile and it was kinda SUS..



<img src="https://github.com/user-attachments/assets/0f706ddb-96f2-4e36-9e87-794634f0e094" alt="random" width="150" height="200">



## Features

- Randomly modifies files in a specified GitHub repository with in 10 contribution.
- Can be scheduled to run daily for consistent contributions.

## Setup Instructions

### 1. Generate a GitHub Personal Access Token

To allow the script to make changes to your repository, you need to generate a Personal Access Token (PAT):

- Go to your GitHub account settings.
- Navigate to **Developer settings** > **Personal access tokens**.
- Click on **Generate new token** (classic).
- Select the necessary scopes (e.g., `repo` for full control of private repositories).
- Copy the generated token and keep it secure.

### 2. Create a Private Repository

- Create a new private repository on GitHub where the script will make contributions.
- Note the repository name and owner, as you will need to specify these in the code.

### 3. Configure the Script

- Open the script and locate the configuration section.
- Update the repository details and insert your Personal Access Token.

### 4. Running the Script

You can run the script manually or set it up to run automatically:

- **Manual Execution**: Run the script using Python.
 ```
git clone https://github.com/noob6t5/daily_conti

cd daily_conti

nano contri.py
 ```
Save and exit with `Ctrl+X then Y`  Make Changes to your repo,username ,PAT as showed in Image..
![confi's](https://github.com/user-attachments/assets/d8904b9f-b415-4619-9d38-f11c9cac02b2)

```
python3 contri.py

or python
```
![succ](https://github.com/user-attachments/assets/1234418a-c179-4151-8bda-de1caebbb78c)

 
- **Automated Execution**: Host the script as a Telegram Bot or use a task scheduler (like cron jobs) to run it daily.

## Important Notes

- Use this tool responsibly and ensure that your contributions comply with GitHub's terms of service.
- This script is intended for educational purposes and should not be used to manipulate contribution graphs inappropriately.

# Further updates

As I am not planning to update this further, But If you want to PR in  feature's like

1. Adding rate limit's
2. Auto running
3. Filling the graph of previous year's
4. Integrating with other bot's
5. Run on Startup
6. You can also make seperate file for Configuration's.

As well If u have other idea's You can share ...
