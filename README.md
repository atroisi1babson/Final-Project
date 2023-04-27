# Recall Alert Project
## Please Note: A different version of the code that removes certain comments was published to the [website](https://alexandertroisi.com/recall-alert-project). Those files can be located on the [demo section](https://alexandertroisi.com/demo-newspaper), which can also be navigated to using the former link.
 

# Table of Contents
## Navigation Links
* [Statement of Purpose](#purpose)
* [Prerequsities](#prerequisites)
* [Usage](#usage)
* [Results](#results)
* [Attribution](#attribution)
* [Disclaimer](#disclaimer)

# Purpose
To harness `ChatGPT API` to generate both summaries and weekly recall newsletters based on an initial CSV file. This code provides a turnkey PDF file for injection into a weekly scheduler.

# Prerequisites
## Installation of Libraries
The code is best suited for Windows users, but can work with other operating systems. These below libraries must be installed by executing the following commands individually in the `Command Prompt` prior to running the code:

> pip install pandas
>
> pip install openai
>
> pip install reportlab
>
> pip install requests
>
> pip install beautifulsoup4
>
> pip install python-csv
>
> pip install unoconv

## Important Use Information

This code makes use of `ChatGPT API`. In order to run the code, an API key must be generated. The API key does not work properly until credit card information is provided to [OpenAI](https://openai.com/pricing).

# Usage
1. Download the code onto your device and open the folder in your preferred integrated development environment, such as Visual Studio Code.

2. Once an activated `ChatGPT API` key has been obtained, open the `config.py` file and replace your "YOUR KEY" with your API key:

> CHATGPT_KEY = "YOUR KEY" 

3. Ensure the `demo_recalls.csv` file has been included. This demonstration file has been created using samples from the actual database.

4. Navigate to the `main.py` file and execute the code. 

Although the dataset was designed specifically for the company, coders can modify the `read_file()` method of the `summaries_generation.py` file to suit individual use cases. Coders can further modify the prompts given to `ChatGPT API` within the `prompt` variable in the `summarize()` methods from both the `summaries_generation.py` and `newsarticle_generation.py` files for specific use cases.

# Results
Additional information on the project can be located at the following [website](https://alexandertroisi.com/recall-alert-project).

# Attribution
## Consumer Safety Service, LLC
I used assets authorized by [Consumer Safety Service, LLC](https://consumersafetyservice.com), and modified some of these assets, with permission, to create a demo file for proof of concept.

## Open AI
I generated components of this project in part with [GPT-3.5 Turbo](https://platform.openai.com/docs/models), OpenAI's large-scale language-generation model. I reviewed the `ChatGPT API` output and take responsibility for said output insofar as no further modifications to the code occur. I further reviewed `ChatGPT` code suggestions for debugging purposes and implemented modified versions of these suggestions using my individual discretion. Components of this specific message were modified from Open AI's [Sharing and Publication Policy](https://openai.com/policies/sharing-publication-policy)

# Disclaimer
I do not condone the usage of these files to perpetuate misinformation. I do not take responsibility for the modification of these files.