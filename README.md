<div align="center">

![main banner](banner-main.svg)![recent repo banner](banner-recent-repo.svg)
</div>

**strictly no vibe coding:D** 

- this project is meant to automatically run on github actions to change the banner. see [main.yml](.github/workflows/main.yml)

<details>
<summary>
        
## running locally
        
</summary>

- create a `.env` file
- put this into your `.env` file and change `your_access_token_here` to your access token:
    ```
    ACCESS_TOKEN=your_access_token_here
    ```
- run this to install dependencies
    ```
    pip install requests python-dotenv pathlib
    ```
- run the python file
    ```
    python test.py
    ```
- **(optional)** for installing autocomplete and intellisense when editing graphql files:
    <br>install [GraphQL: Language Feature Support](https://open-vsx.org/vscode/item?itemName=GraphQL.vscode-graphql) extension.

</details>
    
<br>

## concept art
<details>
    <summary>click to view</summary>
    <img height="300" src="https://github.com/user-attachments/assets/bf5726d8-0f0e-4c3f-9bd2-5b7003ec2cdf" alt="banner">
</details>

