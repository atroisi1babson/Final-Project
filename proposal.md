# Proposal

## Client Introduction:
Consumer Safety Service, LLC aggregates recall alerts from a variety of governmental sources to inform customers about recent recalls. Consumer Safety Service has operated since 1997 and has amassed a particularly comprehensive database with backlogging to 1980. The website can be reached at [consumersafetyservice.com](consumersafetyservice.com). After discussing the possible implementation of ChatGPT API with legal counsel due to libel concerns, the client has provided me full administrative access and authorization to improve the website with individual discretion. For transparency, I am a closely related family member of the client and have worked with the organization before.

## The Big Idea:
Within this project, I intend to leverage ChatGPT API to actualize the long-term vision of the client to automate summaries with reasonably reduced bias. Simply put, the MVP will create, store, and display weekly news articles that summarize recalls of that particular week within a test environment mimicking the production environment. This MVP implicitly requires a degree of familiarity with the technological infrastructure of Consumer Safety Service, which includes `JavaScript`, `HTML`, `CSS`, `SQL`, in addition to the `Node.js runtime environment`, and the `Playwright library`. The stretch goal surrounds the implementation of my MVP onto the production environment (the live [consumersafetyservice.com](consumersafetyservice.com) website), backlogging previous weeks, and setting up automated scheduling for future weeks. To achieve the stretch goal, due diligence in terms of bug testing, exception handling, and security is required.

## Learning Objectives:
To develop an understanding of ChatGPT API utilization, improve database navigation acumen, further cross-language integration skills, learn about `Node.js` and `Playwright`, and to increase my problem solving ability. These skills will benefit my career in Cybersecurity and Technology Auditing.

## Implementation Plan:
Gain familiarization with the database. Discover method of retrieving database information and assigning it to an object in a readable manner. Use ChatGPT API to summarize individual articles, then use ChatGPT API to summarize all of the individual articles. Discover how to store the generated articles in the database. Discover how to retrieve the database information and configure it to appear on the website. Discover how to schedule the script to run once every week. 	

## Project Schedule:
General Overview: I intend to work in protracted sessions (several hours) per each section within the MVP and Stretch Goal below. This has been the approach I have followed all semester; I understand this is not for everyone. I intend to complete absolutely everything before April 25th or 26th in anticipation of my upcoming graduation.
- MVP: Immediately increase my familiarity with the database and the recall algorithm by reading the source code. Develop the test environment with usage of database samples. Research ChatGPT prompt-engineering for minimized bias. Develop the `Python` script in the test environment. Debug and test the script for errors or exceptions extensively. Visualize the information on the test environment website.
- Stretch Goal: Perform due diligence/unofficial audit testing on the script. Receive client approval through informal demo showcase. Integrate the code on the actual website. Apply the script manually to previous weeks to backlog. Create scheduling rules to ensure automatic script recurrence for new weeks.

## Collaboration Plan:
I am working on this project independently, but will coordinate with the client for understanding purposes or to discuss budgetary constraints, if applicable. I intend to continually refine and improve my code in an incremental manner.

## Risks and Limitations:
I anticipate the most time-consumptive roadblocks will surround cross-language transmission and retrieval. The most significant deterrent to my stretch goal surrounds legal complications associated with libel allegations. In the hopefully unlikely event that ChatGPT is incapable of minimizing bias or if OpenAI decides to restrict API access or prohibit ChatGPT from producing certain summaries due to ethical concerns, this will endanger this project. Consequently, ChatGPT usage poses a high risk to Consumer Safety Service, however, this project is within the organization’s risk tolerance. Finally, I must avoid modifying the production environment to ensure continued functionality of the website.

## Additional Course Content:
Scheduled script execution. ChatGPT API with a small discussion of prompt-engineering.
