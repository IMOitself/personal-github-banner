> [!TIP]
> sometimes, <code><image src="https://github.githubassets.com/images/gravatars/gravatar-user-420.png" width=15 height=15></image> **IMO's Bot**</code> is way too lazy. only updating banners whenever it feels like it. *its mostly github's fault. but i wanna blame the bot for the sake of lore :D*

<div align="center">

![main banner](banner-main.svg)
[![recent repo banner](banner-recent-repo.svg)](http://htmlpreview.github.io/?https://github.com/IMOitself/personal-github-banner/blob/master/redirect-to-recent-repo.html)

## strictly no vibe coding:D 
made from scratch! my own personalized banners for displaying anything github related to boost productivity

<br><br>

<table>
<tr>
<td>

<details>
<summary><h2>concept art</h2></summary>
<div align="center">
<img height="300" src="https://github.com/user-attachments/assets/bf5726d8-0f0e-4c3f-9bd2-5b7003ec2cdf" alt="banner">
</div>
</details>

<details>
<summary><h2>usage</h2></summary>
    
##### TODO: steps on how to actually use this repository for other people to use.
involves:
- forking this repository
- setting up github actions secret
- running `main.py` to generate `banner-main.svg` and `banner-recent-repo.svg`
- linking banners to your `README.md` or somewhere else
- setting link of `banner-recent-repo.svg` on your `README.md` to dynamically redirect to displayed repo (optional)
- running `make_all_mini_repo_banners.py` to generate mini repo banners (optional)

if u figure out how to do it urself then congratulations.<br>
else, idk am lazy to create step by step guide :D

<details>
<summary><h2>using locally</h2></summary>

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
    python main.py
    ```
- **(optional)** for installing autocomplete and intellisense when editing graphql files:
    <br>install [GraphQL: Language Feature Support](https://open-vsx.org/vscode/item?itemName=GraphQL.vscode-graphql) extension.

</details>

</details>


## resources i used: 
[vscode-material-icon-theme](https://github.com/material-extensions/vscode-material-icon-theme)
[jetbrains mono](https://www.jetbrains.com/lp/mono/)

</td>
</tr>
</table>

</div>
