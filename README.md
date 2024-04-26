# Chatbot-with-Langsmith-dashboard
This repository consist of code to create a chatbot using Langchain framework.

Langsmith, within the context of Langchain, is a development tool specifically designed to aid in the process of taking large language model (LLM) applications from prototype to production  . It offers various functionalities to streamline this process, including:

* **Debugging**: Langsmith facilitates troubleshooting by providing a comprehensive view of the application's inner workings. You can examine the inputs and outputs at each stage, pinpointing the exact cause of errors or unexpected results.
* **Testing**:  Langsmith empowers you to thoroughly evaluate your LLM application's performance. This guarantees that the application functions as intended before deployment.
* **Monitoring**: Langsmith keeps a watchful eye on your LLM application even after it's live. This allows you to detect and address any issues that may arise in production.

In essence, Langsmith acts as a unified platform that empowers developers to confidently build, test, deploy, and monitor their LLM applications.

Prerequisites:
1. Python3 should be installed in your system.
2. Create virtual environment and activate it. Steps can be found on internet according to OS.
3. Developer should have OPENAI(https://openai.com) API KEY and LANGSMITH(https://smith.langchain.com/) API KEY.


Steps to be followed:
1. Download the packages
--> pip install langchain
--> pip install langchain-openai
--> pip install streamlit
--> python -m pip install python-dotenv

2. Create ".env" file with below variables and their correct values.
--> OPENAI_API_KEY="your key"
--> LANGCHAIN_PROJECT="first-project"
--> LANGCHAIN_API_KEY="your key"

3. Create "app.py" files and use the code provided.
4. Run the command in terminal: streamlit run app.py




